import sys
import os, glob
import time
import platform
import subprocess

import pyqtgraph as pg


from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ReportSetup import Ui_EmailReportDialog
from SystemSetup import Ui_SystemSetupDialog

# import ConfigReader as cr

try:
	# Python 3
	from configparser import NoOptionError, RawConfigParser
except:
	# Python 2
	from ConfigParser import NoOptionError, RawConfigParser

class Ui(QtWidgets.QDialog):
	def __init__(self, *args, **kwargs):
		# Call inherited classes
		super(Ui, self).__init__(*args, **kwargs)
		
		# Load the .ui file
		uic.loadUi('RMSdashboard.ui', self)
		self.title = 'RMS Dashboard'
		
		#print(self.image1_gv.scene())
		#self.scene1 = QGraphicsScene()
		#self.image1_gv.setScene(self.scene1)
		#self.image1_qt = QImage('./test1.jpg')
		#im1 = QGraphicsPixmapItem()
		#im1.setPixmap(QPixmap.fromImage(self.image1_qt))
		#self.scene1.setSceneRect(0,0,320,180)
		#print(self.scene)
		#self.scene1.addItem(im1)
		
		im1 = QPixmap('./test1.jpg')
		im2 = QPixmap('./test2.png')
		im3 = QPixmap('./test3.png')
		im4 = QPixmap('./test4.jpg')
		
		self.image1_lbl.setPixmap(im1)
		self.image2_lbl.setPixmap(im2)
		self.image3_lbl.setPixmap(im3)
		self.image4_lbl.setPixmap(im4)
		
		# Display the GUI
		self.show()
		
		# Button triggers
		self.start_capture_btn.clicked.connect(self.startCapture)
		self.kill_capture_btn.clicked.connect(self.killCapture)
		self.ff_viewer_btn.clicked.connect(self.openFFbinViewer)
		self.reprocess_btn.clicked.connect(self.reprocessData)
		self.edit_config_btn.clicked.connect(self.editConfig)
		self.last_night_data_btn.clicked.connect(self.openLastNightDir)
		self.data_dir_btn.clicked.connect(self.openDataDir)
		self.reboot_btn.clicked.connect(self.rebootSystem)
		# self.setup_reporting_btn.clicked.connect(self.reportingSetup)
		self.setup_system_btn.clicked.connect(self.systemSetup)

		self.getLatestImages()

		# print(config.config_list[0])
		# print(config.station_list[0])

		# Get the latest capture directory created by each camera
		current_data_dirs = self.getMultiRMSDirs(config.station_list)
		
		# print("1")
		# print(current_data_dirs)

		for dir in current_data_dirs:
			print('dir: %s' % dir)

			if config.station_list[0] in dir:
				image_list = glob.glob(dir + "/*.jpg")
				for image in image_list:
					if "meteor" in image:
						im1 = QPixmap(dir + "/" + image)
						print(image)

	def getMultiRMSDirs(self, camera_list):
		""" Returns a list of the most recent camera data directories

			Arguments:
				camera_list: 
		"""

		current_data_dirs = []

		for camera in camera_list:
			camera = camera.split('.')[0]
			data_dirs = glob.glob(config.data_dir + '/' + camera + '*')

			print(config.data_dir + '/' + camera)
			data_dirs.sort()
			try:
				current_data_dirs.append(data_dirs[-1])
			except:
				print('Nada')

		return(current_data_dirs)

	def getLatestImages(self):
		print(config.data_dir)

	def openDataDir(self):
		path = config.data_dir
		if platform.system() == "Windows":
			os.startfile(path)
		elif platform.system() == "Darwin":
			subprocess.Popen(["open", path])
		else:
			subprocess.Popen(["xdg-open", path])
	
	def startCapture(self):
		print('Starting capture...')
		subprocess.Popen(['x-terminal-emulator', '-e', 'python -m RMS.StartCapture -c ~/source/RMS/.config'])
		
	def killCapture(self):
		print('Killing StartCapture...')
		subprocess.run(['sudo', 'killall', 'StartCapture'])
		
	def reprocessData(self):
		print('Reprocessing data...')
		
	def editConfig(self):
		print('Opening config file for editing...')
		
		file = '/home/lcam/source/RMS/.config'
		if platform.system() == 'Windows':
			os.startfile(file)
		elif platform.system() == "Darwin":
			subprocess.Popen(["open", file])
		else:
			subprocess.Popen(["xdg-open", file])
		
	def openLastNightDir(self):
		print('Opening the data directory from last night.')
		print(config.tab_names)
		print(config.config_list)
		
	def rebootSystem(self):
		qm = QtGui.QMessageBox
		ret = qm.question(self, '', 'Are you sure that you want to reboot the system?', qm.Yes | qm.No)
		
		if ret == qm.Yes:
			for i in range(10,0,-1):               
				print(f'Rebooting system in {i} seconds...', end='\r', flush=True)
				time.sleep(1)
			print('Rebootng now!                     ')
		else:
			print('Phew! Narrowly averted a disaster!')
		
	def openFFbinViewer(self):
		print('opening ff viewer')
		subprocess.run(['x-terminal-emulator', '-e', '~/source/RMS/Scripts/CMNbinViewer.sh'])

	# def reportingSetup(self):
	# 	self.window = QtWidgets.QMainWindow()
	# 	self.ui = Ui_EmailReportDialog()
	# 	self.ui.setupUi(self.window)
	# 	self.ui.cancel_report_setup_btn.clicked.connect(self.window.close)
	# 	self.window.show()

	def systemSetup(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_SystemSetupDialog()
		self.ui.setupUi(self.window)
		self.ui.cancel_setup_btn.clicked.connect(self.window.close)
		self.window.show()

def handleVisibleChanged():
	if not QtGui.QGuiApplication.inputMethod().isVisible():
		return
	for w in QtGui.QGuiApplication.allWindows():
		if w.metaObject().className() == "QtVirtualKeyboard::InputView":
			keyboard = w.findChild(QtCore.QObject, "keyboard")
			if keyboard is not None:
				r = w.geometry()
				r.moveTop(keyboard.property("y"))
				w.setMask(QtGui.QRegion(r))
				return

class Config:
	def __init__(self):

		# # Get the package root directory
		# self.rms_root_dir = os.path.abspath(os.path.join(os.path.dirname(RMS.__file__), os.pardir))

		# default config file absolute path
		self.config_file_name = os.path.join('.', 'dash.config')

		##### System
		self.user_home = "/home/pi"
		self.config_list = ["~/source/RMS/.config"]
		self.station_list = ["CAWE01"]

		##### Tabs
		self.tab_names = ["tab1","tab2"]

		##### Data
		self.data_dir = "~/RMS_data"

		##### Reporting
		self.email_report = False
		self.email_to = ""
		self.email_cc = ""
		self.email_subject = "Test Subject"
		self.smtp_address = "xox.xox.xox.xox"
		self.smtp_passwd = "password"

		##### Look
		self.dark_theme = False
	
def removeInlineComments(cfgparser, delimiter):
	""" Removes inline comments from config file. """
	for section in cfgparser.sections():
		[cfgparser.set(section, item[0], item[1].split(delimiter)[0].strip()) for item in cfgparser.items(section)]

def parse(path, strict=True):
	""" Parses config file at the given path and returns the corresponding Config object.

	Arguments:
		path: [str] path to file (.config or dfnstation.cfg)
		strict: [bool]

	Returns:
		config: [Config]

	"""

	delimiter = ";"

	try:
		# Python 3
		parser = RawConfigParser(inline_comment_prefixes=(delimiter), strict=strict)

	except:
		# Python 2
		parser = RawConfigParser()

	print(type(path))
	parser.read(path)


	# Remove inline comments
	removeInlineComments(parser, delimiter)
	
	config = Config()

	# Store parsed config file name
	config.config_file_name = path

	# Parse an RMS config file
	if os.path.basename(path).endswith('.config'):
		parseConfigFile(config, parser)

	else:
		raise RuntimeError('Unknown config file name: {}'.format(os.path.basename(path)))
	
	return config

def parseConfigFile(config, parser):
	parseSystem(config, parser)
	parseTabs(config, parser)
	parseData(config, parser)
	parseReporting(config, parser)
	parseLook(config, parser)

def parseSystem(config, parser):
	section = "System"
	if not parser.has_section(section):
		raise RuntimeError("Not configured!")
	
	if parser.has_option(section, "user_home"):
		config.user_home = parser.get(section, "user_home")

	if parser.has_option(section, "config_list"):
		config.config_list = parser.get(section, "config_list").split(",")

	if parser.has_option(section, "station_list"):
		config.station_list = parser.get(section, "station_list").split(",")

def parseTabs(config, parser):
	section = "Tabs"
	if not parser.has_section(section):
		raise RuntimeError("Not configured!")

	if parser.has_option(section, "tab_names"):
		config.tab_names = parser.get(section, "tab_names").split(",")

def parseData(config, parser):
	section = "Data"
	if not parser.has_section(section):
		raise RuntimeError("Not configured!")

	if parser.has_option(section, "data_dir"):
		config.data_dir = parser.get(section, "data_dir")


	# if parser.has_option(section, "longitude"):
	# 	config.longitude = parser.getfloat(section, "longitude")

	# if parser.has_option(section, "elevation"):
	# 	config.elevation = parser.getfloat(section, "elevation")

def parseReporting(config, parser):
	section = "Reporting"
	if not parser.has_section(section):
		raise RuntimeError("Not configured!")

	if parser.has_option(section, "email_report"):
		config.email_report = parser.getboolean(section, "email_report")

	if parser.has_option(section, "email_to"):
		config.email_to = parser.get(section, "email_to")

	if parser.has_option(section, "email_cc"):
		config.email_cc = parser.get(section, "email_cc")

	if parser.has_option(section, "email_subject"):
		config.email_subject = parser.get(section, "email_subject")

	if parser.has_option(section, "smtp_address"):
		config.smtp_address = parser.get(section, "smtp_address")

	if parser.has_option(section, "smtp_passwd"):
		config.smtp_passwd = parser.get(section, "smtp_passwd")

def parseLook(config, parser):
	section = "Look"
	if not parser.has_section(section):
		raise RuntimeError("Not configured")

	if parser.has_option(section, "dark_theme"):
		config.dark_theme = parser.getboolean(section, "dark_theme")

if __name__ == "__main__":
	os.environ['QT_IM_MODULE'] = 'qtvirtualkeyboard'
	app = QtWidgets.QApplication(sys.argv)

	try:
		QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)
	except:
		print("There's a problem with QT Virtual Keyboard. Is it installed?")

	# Read/parse dashboard configuration file
	config_path = "dash.config"
	config = parse(config_path)

	window = Ui()
	app.exec()
