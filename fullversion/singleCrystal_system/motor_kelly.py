# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motor_kelly.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QMotor = QMotor(self.centralwidget)
        self.QMotor.setGeometry(QtCore.QRect(80, 60, 295, 181))
        self.QMotor.setToolTip("")
        self.QMotor.setObjectName("QMotor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QMotor.setWhatsThis(_translate("MainWindow", "\n"
"    Widget based on EPICS motor record\n"
"    Details about motor record parameters are found at: https://www3.aps.anl.gov/bcda/synApps/motor/R6-9/motorRecord.html\n"
"    "))
        self.QMotor.setProperty("channel", _translate("MainWindow", "ca://dmc:galil:test:A"))

from singleCrystal_system.sol_widgets.widgets.motor import QMotor

if __name__ == "__main__":
    import sys
    from pydm import PyDMApplication as PyDMApplicationPYDM
    #app = QtWidgets.QApplication(sys.argv)
    app = PyDMApplicationPYDM(use_main_window=False)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.establish_widget_connections(widget = MainWindow)
    sys.exit(app.exec_())

