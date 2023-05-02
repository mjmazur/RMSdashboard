# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmailReportDialog(object):
    def setupUi(self, EmailReportDialog):
        EmailReportDialog.setObjectName("EmailReportDialog")
        EmailReportDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EmailReportDialog.resize(400, 312)
        self.horizontalLayoutWidget = QtWidgets.QWidget(EmailReportDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(EmailReportDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 270, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.report_setup_save_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.report_setup_save_btn.setObjectName("report_setup_save_btn")
        self.horizontalLayout.addWidget(self.report_setup_save_btn)
        self.report_setup_cancel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.report_setup_cancel_btn.setObjectName("report_setup_cancel_btn")
        self.horizontalLayout.addWidget(self.report_setup_cancel_btn)

        self.retranslateUi(EmailReportDialog)
        QtCore.QMetaObject.connectSlotsByName(EmailReportDialog)

    def retranslateUi(self, EmailReportDialog):
        _translate = QtCore.QCoreApplication.translate
        EmailReportDialog.setWindowTitle(_translate("EmailReportDialog", "Reporting Setup"))
        self.label.setText(_translate("EmailReportDialog", "To:"))
        self.label_4.setText(_translate("EmailReportDialog", "CC:"))
        self.label_5.setText(_translate("EmailReportDialog", "Subject:"))
        self.label_2.setText(_translate("EmailReportDialog", "SMTP Address:"))
        self.label_3.setText(_translate("EmailReportDialog", "SMTP Password:"))
        self.checkBox.setText(_translate("EmailReportDialog", "Attach timelapse video"))
        self.checkBox_2.setText(_translate("EmailReportDialog", "Attach diagnostic images"))
        self.report_setup_save_btn.setText(_translate("EmailReportDialog", "Save"))
        self.report_setup_cancel_btn.setText(_translate("EmailReportDialog", "Cancel"))
