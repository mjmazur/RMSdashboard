#!/usr/bin/python
import os, glob
import sys, shutil
import traceback
import subprocess, platform
import datetime
import logging
import email, smtplib, ssl, time
import numpy as np

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from string import Template

def checkNTP():
    cmd = ['timedatectl', 'timesync-status']
    ntp_message = subprocess.check_output(cmd)
    ntp_message = ntp_message.decode().split('\n')
    return ntp_message

def pingOk(host):
    try:
        output = subprocess.check_output('ping -{} 1 {}'.format('n' if platform.system().lower()=='windows' else 'c', host), shell=True)
    except:
        return False
    return True

def getUptime():
    with open('/proc/uptime', 'r') as f:
        uptime_s = float(f.readline().split()[0])
    return uptime_s

def getContacts(filename):
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for contact in contacts_file:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names, emails

def readTemplate(filename):
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def getDetectionCount(capture_dir):
    # print('Capture directory: %s' % capture_dir)
    try:
        with open(os.path.join(capture_dir, 'FTPdetectinfo_' + os.path.basename(capture_dir) + '.txt')) as detection_file:
            detection_list = detection_file.read().splitlines()
            detection_count = int(detection_list[0].split()[3])
            # print('Hi! %s' % detection_count)
    except:
        detection_count = 'N/A'
    return detection_count

def getSysstat(flag='-u'):
    cmd = ['sar', flag]

    if flag == '-u':
        col = 3
    elif flag == '-r':
        col = 5

    try:
        with open('sysstat.tmp', 'w') as f:
            return_code = subprocess.call(cmd, stdout=f)

        with open('sysstat.tmp', 'r') as f: 
            lines = f.readlines()

        stats = []

        for i in range(3, len(lines)-1):
            c = float(lines[i].split()[col])
            stats.append(c)
    except:
        stats = [999]
    return stats

def getMultiRMSDirs(camera_list):
    """ Returns a list of the most recent camera data directories

        Arguments:
            camera_list: 
    """

    current_data_dirs = []

    for camera in camera_list:
        camera = camera.split('.')[0]
        data_dirs = glob.glob('~/RMS_data/CapturedFiles/' + camera + '*')
        data_dirs.sort()
        try:
            current_data_dirs.append(data_dirs[-1])
        except:
            print('Nada')

def rmsExternal(captured_night_dir, archived_night_dir, config):
	# create lock file to avoid RMS rebooting the system
    rebootlockfile = os.path.join(config.data_dir, config.reboot_lock_file)

    try:
        with open(rebootlockfile, 'w') as _:
            print('Created reboot lockfile at %s' % rebootlockfile)
            pass
    except:
        print('Could not create reboot lockfile at %s' % rebootlockfile)
        pass

    # Create a list of cameras based on their config files
    camera_list = []
    for root, dirs, files in os.walk('~/source/ConfigFiles'):
        for name in files:
            # print(name)
            camera_list.append(name)

    # Get the latest capture directory created by each camera
    current_data_dirs = getMultiRMSDirs(camera_list)

    num_cameras_locked = len(camera_list)-1

    while num_cameras_locked > 1:
        num_cameras_locked = 1
        for camera in camera_list:
            camera = camera.split('.')[0]
            print(os.path.join(config.data_dir,camera+'.lock'))
            if os.path.isfile(os.path.join(config.data_dir,camera+'.lock')):
                print('Lockfile exists!')
                num_cameras_locked += 1
                print('%s cameras are locked!' % num_cameras_locked)
            else:
                print('Lockfile does not exist!')

        print('Waiting 5 seconds to check for lock files again.')
        time.sleep(5)

    # Get total number of detections
    detect_dict = {}

    for i in range(len(current_data_dirs)):
        # print(captured_night_dir)
        print(current_data_dirs[i])
        detect_dict['detection_count{0}'.format(i+1)] = getDetectionCount(current_data_dirs[i])

    try:
        detection_count1 = detect_dict['detection_count1']
    except:
        detection_count1 = 'N/A'
    try:
        detection_count2 = detect_dict['detection_count2']
    except:
        detection_count2 = 'N/A'
    try:
        detection_count3 = detect_dict['detection_count3']
    except:
        detection_count3 = 'N/A'
    try:
        detection_count4 = detect_dict['detection_count4']
    except:
        detection_count4 = 'N/A'

    # Get number of meteors detected
    satellite_count1 = 'N/A'
    satellite_count2 = 'N/A'
    satellite_count3 = 'N/A'
    satellite_count4 = 'N/A'

    # Get number of meteors detected
    meteor_count1 = 'N/A'
    meteor_count2 = 'N/A'
    meteor_count3 = 'N/A'
    meteor_count4 = 'N/A'

	# Get system stats from sysstat
    cpu_stats = getSysstat()
    mem_stats = getSysstat('-r')

    # Check uptime
    uptime = getUptime() / (3600*24)

    # Check free space
    total, used, free = shutil.disk_usage('/')
    free = free // (2**30)

    # Check NTP status...
    ntp_message = checkNTP()


    # Send email to user
    server_address = 'xox.xox.xox.xox'
    port = 25
    sender_email = "rms@me.teor.ca"
    subject = "RMS Summary"

    # Open contacts text file and email template
    names, emails = getContacts('./RMScontacts.txt')
    message_template = readTemplate('./RMSreporttemplate.txt')

     # Send email to users. Loop through contacts list.
    for name, email in zip(names, emails):

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = subject
        # message["Cc"] = cc_email
        # recipients = cc_email.split(',') + [receiver_email]
        # recipients = [receiver_email]

        body = message_template.safe_substitute(PERSON_NAME=name.title(), \
            CAM1_CHECK=cam1_ping, CAM2_CHECK=cam2_ping, CAM3_CHECK=cam3_ping, \
            CAM4_CHECK=cam4_ping, CAM5_CHECK=cam5_ping, CAM6_CHECK=cam6_ping, \
            CAM7_CHECK=cam7_ping, CAM8_CHECK=cam8_ping, UPTIME=round(uptime,2), FREE_SPACE=free, \
            NUM_CORES=config.num_cores, WIDTH=config.width, HEIGHT=config.height, \
            FPS=config.fps, DATA_DIR=config.data_dir, UPLOAD_ENABLED=config.upload_enabled, \
            ANG_VEL_MIN=config.ang_vel_min, ANG_VEL_MAX=config.ang_vel_max, \
            ML_FILTER=config.ml_filter, \
            NUM_DETECTIONS_CAM1=detection_count1, NUM_DETECTIONS_CAM2=detection_count2, \
            NUM_DETECTIONS_CAM3=detection_count3, NUM_DETECTIONS_CAM4=detection_count4, \
            NUM_SATS_CAM1=satellite_count1, NUM_SATS_CAM2=satellite_count2, \
            NUM_SATS_CAM3=satellite_count3, NUM_SATS_CAM4=satellite_count4, \
            NUM_METEORS_CAM1=meteor_count1, NUM_METEORS_CAM2=meteor_count2, \
            NUM_METEORS_CAM3=meteor_count3, NUM_METEORS_CAM4=meteor_count4, \
            MAX_LOAD=np.max(cpu_stats), MAX_MEMORY=np.max(mem_stats), \
            MIN_LOAD=np.min(cpu_stats), MIN_MEMORY=np.min(mem_stats), \
            AVE_LOAD=round(np.mean(cpu_stats),2), AVE_MEMORY=round(np.mean(mem_stats),2), \
            NTP_SERVER=ntp_message[0], NTP_STRATUM=ntp_message[4], NTP_OFFSET=ntp_message[8], \
            NTP_JITTER=ntp_message[10])

        message.attach(MIMEText(body, "plain"))

        # filestograb = ("*Satellites.*","*meteors.*","CA*_DETECTED_thumbs.jpg","CA*.png","CA*.csv","*Timelapse.mp4")
        # filestograb = ("*Satellites.jpg","*meteors.jpg","CA*.png","CA*.csv")
        filestograb = ("*meteors.jpg","CA*.png","CA*.csv")
        filenames = []

        try:
            for files in filestograb:
                filenames.extend(glob.glob(captured_night_dir + "/" + files))
        except:
            pass

        try:
            for dd in current_data_dirs:
                filenames.extend(glob.glob(os.path.join(dd, "*Satellites.csv")))
        except:
            pass

        for f in filenames:
            fhead, ftail = os.path.split(f)
            attachment = MIMEApplication(open(f, "rb").read())
            attachment.add_header("Content-Disposition", "attachment", filename=ftail, )
            message.attach(attachment)

        text = message.as_string()

        context = ssl.create_default_context()

        with smtplib.SMTP(server_address, port) as server:
            server.starttls()
            server.sendmail(sender_email, email, text)

        del message

    print('The email has been sent...')

    # relase lock file so RMS is authorized to reboot, if needed
    try:
        os.remove(rebootlockfile)
        print('Removed %s' % rebootlockfile)
    except:
        print('No reboot lockfile to remove... %s' % rebootlockfile)