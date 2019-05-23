# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_PVnames.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_PVnames(object):
    def setupUi(self, MainWindow_PVnames):
        MainWindow_PVnames.setObjectName("MainWindow_PVnames")
        MainWindow_PVnames.resize(299, 429)
        MainWindow_PVnames.setMinimumSize(QtCore.QSize(299, 429))
        MainWindow_PVnames.setMaximumSize(QtCore.QSize(299, 429))
        MainWindow_PVnames.setStyleSheet("background-color: rgb(65,65, 65);\n"
"color: rgb(240, 240, 240);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow_PVnames)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setMinimumSize(QtCore.QSize(0, 16))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_2.setStyleSheet("color: rgb(240, 240, 240);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.label_spec = QtWidgets.QLabel(self.centralwidget)
        self.label_spec.setObjectName("label_spec")
        self.gridLayout.addWidget(self.label_spec, 2, 0, 1, 1)
        self.lineEdit_spec = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spec.setEnabled(True)
        self.lineEdit_spec.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(60, 60, 60);")
        self.lineEdit_spec.setObjectName("lineEdit_spec")
        self.gridLayout.addWidget(self.lineEdit_spec, 3, 0, 1, 1)
        self.label_motor = QtWidgets.QLabel(self.centralwidget)
        self.label_motor.setObjectName("label_motor")
        self.gridLayout.addWidget(self.label_motor, 4, 0, 1, 1)
        self.lineEdit_motor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_motor.setEnabled(True)
        self.lineEdit_motor.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(60, 60, 60);")
        self.lineEdit_motor.setObjectName("lineEdit_motor")
        self.gridLayout.addWidget(self.lineEdit_motor, 5, 0, 1, 1)
        self.label_LS = QtWidgets.QLabel(self.centralwidget)
        self.label_LS.setObjectName("label_LS")
        self.gridLayout.addWidget(self.label_LS, 6, 0, 1, 1)
        self.lineEdit_LS = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_LS.setEnabled(True)
        self.lineEdit_LS.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(60, 60, 60);")
        self.lineEdit_LS.setObjectName("lineEdit_LS")
        self.gridLayout.addWidget(self.lineEdit_LS, 7, 0, 1, 1)
        self.label_SG = QtWidgets.QLabel(self.centralwidget)
        self.label_SG.setObjectName("label_SG")
        self.gridLayout.addWidget(self.label_SG, 8, 0, 1, 1)
        self.lineEdit_sg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sg.setEnabled(True)
        self.lineEdit_sg.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(60, 60, 60);")
        self.lineEdit_sg.setObjectName("lineEdit_sg")
        self.gridLayout.addWidget(self.lineEdit_sg, 9, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(0, 16))
        self.line.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line.setStyleSheet("color: rgb(240, 240, 240);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 10, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 11, 0, 1, 1)
        MainWindow_PVnames.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_PVnames)
        self.statusbar.setObjectName("statusbar")
        MainWindow_PVnames.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_PVnames)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_PVnames)

    def retranslateUi(self, MainWindow_PVnames):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_PVnames.setWindowTitle(_translate("MainWindow_PVnames", "Edit: PV names"))
        self.label.setText(_translate("MainWindow_PVnames", "PV names of each system"))
        self.label_spec.setText(_translate("MainWindow_PVnames", "Spectrometer of Pressure system"))
        self.lineEdit_spec.setText(_translate("MainWindow_PVnames", "SOL3"))
        self.label_motor.setText(_translate("MainWindow_PVnames", "Motor of pressure system"))
        self.lineEdit_motor.setText(_translate("MainWindow_PVnames", "SOL:galil:test:A"))
        self.label_LS.setText(_translate("MainWindow_PVnames", "DAC temperature system "))
        self.lineEdit_LS.setText(_translate("MainWindow_PVnames", "XDS:LS"))
        self.label_SG.setText(_translate("MainWindow_PVnames", "Motor of Single Crystal"))
        self.lineEdit_sg.setText(_translate("MainWindow_PVnames", "dmc:galil:test:A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_PVnames = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_PVnames()
    ui.setupUi(MainWindow_PVnames)
    MainWindow_PVnames.show()
    sys.exit(app.exec_())

