import sys
import os
import time
import platform
import subprocess

import pyqtgraph as pg

from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ReportSetup import Ui_EmailReportDialog

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
		self.email_report_cb.toggled.connect(self.emailReportToggle)
		
		# Read/parse dashboard coniguration file
		
		# Read/parse RMS configuration file
		
	def openDataDir(self):
		path = '/home/lcam'
		if platform.system() == "Windows":
			os.startfile(path)
		elif platform.system() == "Darwin":
			subprocess.Popen(["open", path])
		else:
			subprocess.Popen(["xdg-open", path])
	
	def startCapture(self):
		print('Starting capture...')
		subprocess.Popen(['x-terminal-emulator', '-e', 'python -m RMS.StartCapture -c ~/source/ConfigFiles/CAWE01.config'])
		
	def killCapture(self):
		print('Killing StartCapture...')
		subprocess.run(['sudo', 'killall', 'StartCapture'])
		
	def reprocessData(self):
		print('Reprocessing data...')
		
	def editConfig(self):
		print('Opening config file for editing...')
		
		file = '/home/lcam/source/LCAM/.config'
		if platform.system() == 'Windows':
			os.startfile(file)
		elif platform.system() == "Darwin":
			subprocess.Popen(["open", file])
		else:
			subprocess.Popen(["xdg-open", file])
		
	def openLastNightDir(self):
		print('Opening the data directory from last night.')
		
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
		subprocess.run(['x-terminal-emulator', '-e', '~/source/LCAM/Scripts/CMNbinViewer.sh'])

	def emailReportToggle(self):
		print('Test')
	
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Ui()
	app.exec()
