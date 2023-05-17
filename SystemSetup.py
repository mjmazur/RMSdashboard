# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SystemSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SystemSetupDialog(object):
    def setupUi(self, SystemSetupDialog):
        SystemSetupDialog.setObjectName("SystemSetupDialog")
        SystemSetupDialog.resize(400, 312)
        self.verticalLayoutWidget = QtWidgets.QWidget(SystemSetupDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SystemSetupDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(SystemSetupDialog)
        QtCore.QMetaObject.connectSlotsByName(SystemSetupDialog)

    def retranslateUi(self, SystemSetupDialog):
        _translate = QtCore.QCoreApplication.translate
        SystemSetupDialog.setWindowTitle(_translate("SystemSetupDialog", "System Setup"))
        self.label.setText(_translate("SystemSetupDialog", "Camera List:"))
        self.lineEdit.setText(_translate("SystemSetupDialog", "CA0001,CA0002,CA0003,CA0004"))
        self.label_2.setText(_translate("SystemSetupDialog", "Clients:"))
        self.label_3.setText(_translate("SystemSetupDialog", "TextLabel"))
        self.lineEdit_2.setText(_translate("SystemSetupDialog", "localhost,localhost,192.168.0.101,192.168.0.102"))
        self.checkBox.setText(_translate("SystemSetupDialog", "This is the host machine"))
        self.checkBox_2.setText(_translate("SystemSetupDialog", "CheckBox"))
        self.pushButton.setText(_translate("SystemSetupDialog", "Save"))
        self.pushButton_2.setText(_translate("SystemSetupDialog", "Cancel"))

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
    QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)


if __name__ == "__main__":
    import sys
    os.environ['QT_IM_MODULE'] = 'qtvirtualkeyboard'
    app = QtWidgets.QApplication(sys.argv)

    QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)

    SystemSetupDialog = QtWidgets.QDialog()

    ui = Ui_SystemSetupDialog()
    ui.setupUi(SystemSetupDialog)
    
    SystemSetupDialog.show()
    
    sys.exit(app.exec_())
