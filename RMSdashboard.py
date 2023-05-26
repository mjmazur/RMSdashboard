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
from SystemSetup import Ui_SystemSetupDialog

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
		

		# Read/parse dashboard coniguration file
		dashconfig = 1

		# Read/parse RMS configuration file


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


	    parser.read(path)


	    # Remove inline comments
	    removeInlineComments(parser, delimiter)
	    
	    config = Config()

	    # Store parsed config file name
	    config.config_file_name = path

	    # Parse an RMS config file
	    if os.path.basename(path).endswith('.config'):
	        parseConfigFile(config, parser)

	    # Parse a DFN config file
	    elif os.path.basename(path) == 'dfnstation.cfg':
	        parseDFNStation(config, parser)

	    else:
	        raise RuntimeError('Unknown config file name: {}'.format(os.path.basename(path)))
	    
	    return config
		
	def parseSystemConfigFile(config, parser):
	    parseSystem(config, parser)
	    parseTabs(config, parser)
	    parseData(config, parser)
	    parseReporting(config, parser)
	    parseLook(config, parser)

	def parseSystemConfigFile(config, parser):
	    parseSystem(config, parser)
	    parseTabs(config, parser)
	    parseData(config, parser)
	    parseReporting(config, parser)
	    parseLook(config, parser)

	def parseConfigFile(config, parser):
	    parseSystem(config, parser)
	    parseCapture(config, parser)
	    parseBuildArgs(config, parser)
	    parseUpload(config, parser)
	    parseCompression(config, parser)
	    parseFireballDetection(config, parser)
	    parseMeteorDetection(config, parser)
	    parseStarExtraction(config, parser)
	    parseCalibration(config, parser)
	    parseThumbnails(config, parser)
	    parseStack(config, parser)
	    parseColors(config, parser)

	def openDataDir(self):
		path = '~/RMS_data'
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
	
if __name__ == "__main__":
	os.environ['QT_IM_MODULE'] = 'qtvirtualkeyboard'
	app = QtWidgets.QApplication(sys.argv)

	try:
		QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)
	except:
		print("There's a problem with QT Virtual Keyboard. Is it installed?")

	window = Ui()
	app.exec()
