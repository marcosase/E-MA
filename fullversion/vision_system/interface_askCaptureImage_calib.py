# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_askCaptureImage_calib.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_askCalibCCD(object):
    def setupUi(self, MainWindow_askCalibCCD):
        MainWindow_askCalibCCD.setObjectName("MainWindow_askCalibCCD")
        MainWindow_askCalibCCD.resize(488, 82)
        MainWindow_askCalibCCD.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_askCalibCCD)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.PyDMLabel_question = PyDMLabel(self.centralwidget)
        self.PyDMLabel_question.setToolTip("")
        self.PyDMLabel_question.setWhatsThis("")
        self.PyDMLabel_question.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.PyDMLabel_question.setObjectName("PyDMLabel_question")
        self.gridLayout.addWidget(self.PyDMLabel_question, 0, 0, 1, 2)
        self.PyDMPushButton_YES = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_YES.setToolTip("")
        self.PyDMPushButton_YES.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_YES.setObjectName("PyDMPushButton_YES")
        self.gridLayout.addWidget(self.PyDMPushButton_YES, 1, 0, 1, 1)
        self.PyDMPushButton_NO = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_NO.setToolTip("")
        self.PyDMPushButton_NO.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_NO.setObjectName("PyDMPushButton_NO")
        self.gridLayout.addWidget(self.PyDMPushButton_NO, 1, 1, 1, 1)
        MainWindow_askCalibCCD.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_askCalibCCD)
        self.statusbar.setObjectName("statusbar")
        MainWindow_askCalibCCD.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_askCalibCCD)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_askCalibCCD)

    def retranslateUi(self, MainWindow_askCalibCCD):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_askCalibCCD.setWindowTitle(_translate("MainWindow_askCalibCCD", "Image Capture"))
        self.PyDMLabel_question.setText(_translate("MainWindow_askCalibCCD", "Do you want to capture images from MARCCD device?"))
        self.PyDMPushButton_YES.setWhatsThis(_translate("MainWindow_askCalibCCD", "\n"
"    Basic PushButton to send a fixed value.\n"
"\n"
"    The PyDMPushButton is meant to hold a specific value, and send that value\n"
"    to a channel when it is clicked, much like the MessageButton does in EDM.\n"
"    The PyDMPushButton works in two different modes of operation, first, a\n"
"    fixed value can be given to the :attr:`.pressValue` attribute, whenever the\n"
"    button is clicked a signal containing this value will be sent to the\n"
"    connected channel. This is the default behavior of the button. However, if\n"
"    the :attr:`.relativeChange` is set to True, the fixed value will be added\n"
"    to the current value of the channel. This means that the button will\n"
"    increment a channel by a fixed amount with every click, a consistent\n"
"    relative move\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QObject, optional\n"
"        Parent of PyDMPushButton\n"
"\n"
"    label : str, optional\n"
"        String to place on button\n"
"\n"
"    icon : QIcon, optional\n"
"        An Icon to display on the PyDMPushButton\n"
"\n"
"    pressValue : int, float, str\n"
"        Value to be sent when the button is clicked\n"
"\n"
"    relative : bool, optional\n"
"        Choice to have the button perform a relative put, instead of always\n"
"        setting to an absolute value\n"
"\n"
"    init_channel : str, optional\n"
"        ID of channel to manipulate\n"
"\n"
"    "))
        self.PyDMPushButton_YES.setText(_translate("MainWindow_askCalibCCD", "Yes"))
        self.PyDMPushButton_NO.setWhatsThis(_translate("MainWindow_askCalibCCD", "\n"
"    Basic PushButton to send a fixed value.\n"
"\n"
"    The PyDMPushButton is meant to hold a specific value, and send that value\n"
"    to a channel when it is clicked, much like the MessageButton does in EDM.\n"
"    The PyDMPushButton works in two different modes of operation, first, a\n"
"    fixed value can be given to the :attr:`.pressValue` attribute, whenever the\n"
"    button is clicked a signal containing this value will be sent to the\n"
"    connected channel. This is the default behavior of the button. However, if\n"
"    the :attr:`.relativeChange` is set to True, the fixed value will be added\n"
"    to the current value of the channel. This means that the button will\n"
"    increment a channel by a fixed amount with every click, a consistent\n"
"    relative move\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QObject, optional\n"
"        Parent of PyDMPushButton\n"
"\n"
"    label : str, optional\n"
"        String to place on button\n"
"\n"
"    icon : QIcon, optional\n"
"        An Icon to display on the PyDMPushButton\n"
"\n"
"    pressValue : int, float, str\n"
"        Value to be sent when the button is clicked\n"
"\n"
"    relative : bool, optional\n"
"        Choice to have the button perform a relative put, instead of always\n"
"        setting to an absolute value\n"
"\n"
"    init_channel : str, optional\n"
"        ID of channel to manipulate\n"
"\n"
"    "))
        self.PyDMPushButton_NO.setText(_translate("MainWindow_askCalibCCD", "No"))
    '''
        self.__setFlowControl(MainWindow_askCalibCCD)
        
    def __setFlowControl(self,MainWindow_askCalibCCD):
        #self.PyDMPushButton_YES.clicked.connect(self.open_calibInterface)
        self.PyDMPushButton_NO.clicked.connect(MainWindow_askCalibCCD.close) 
        self.PyDMPushButton_YES.clicked.connect(MainWindow_askCalibCCD.close)
         
    def open_calibInterface(self):    
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Ui_MainWindow_marccd()
        self.ui.setupUi(self.window)
        self.window.show()
    '''
                
from pydm.widgets.label import PyDMLabel
from pydm.widgets.pushbutton import PyDMPushButton
from vision_system.interface_ccd_marccd import Ui_Ui_MainWindow_marccd

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_askCalibCCD = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_askCalibCCD()
    ui.setupUi(MainWindow_askCalibCCD)
    MainWindow_askCalibCCD.show()
    sys.exit(app.exec_())

