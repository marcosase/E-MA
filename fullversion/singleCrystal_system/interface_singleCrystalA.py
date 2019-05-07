# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motor_kelly_sg.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 504)
        MainWindow.setMinimumSize(QtCore.QSize(380, 504))
        MainWindow.setMaximumSize(QtCore.QSize(381, 504))
        MainWindow.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"color: rgb(240, 240,240);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.QMotor = QMotor(self.centralwidget)
        self.QMotor.setToolTip("")
        self.QMotor.setProperty("channel", "")
        self.QMotor.setObjectName("QMotor")
        self.gridLayout.addWidget(self.QMotor, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.PyDMCheckbox_msg = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_msg.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PyDMCheckbox_msg.setFont(font)
        self.PyDMCheckbox_msg.setToolTip("")
        self.PyDMCheckbox_msg.setAutoFillBackground(False)
        self.PyDMCheckbox_msg.setStyleSheet("")
        self.PyDMCheckbox_msg.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PyDMCheckbox_msg.setText("")
        self.PyDMCheckbox_msg.setIconSize(QtCore.QSize(16, 16))
        self.PyDMCheckbox_msg.setCheckable(True)
        self.PyDMCheckbox_msg.setAutoExclusive(False)
        self.PyDMCheckbox_msg.setTristate(False)
        self.PyDMCheckbox_msg.setProperty("channel", "")
        self.PyDMCheckbox_msg.setObjectName("PyDMCheckbox_msg")
        self.horizontalLayout.addWidget(self.PyDMCheckbox_msg)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(130, 0))
        self.label_4.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.PyDMSpinbox_a0 = PyDMSpinbox(self.centralwidget)
        self.PyDMSpinbox_a0.setEnabled(True)
        self.PyDMSpinbox_a0.setMinimumSize(QtCore.QSize(80, 25))
        self.PyDMSpinbox_a0.setMaximumSize(QtCore.QSize(80, 25))
        self.PyDMSpinbox_a0.setToolTip("")
        self.PyDMSpinbox_a0.setStyleSheet("")
        self.PyDMSpinbox_a0.setDecimals(2)
        self.PyDMSpinbox_a0.setMinimum(-360.0)
        self.PyDMSpinbox_a0.setMaximum(360.0)
        self.PyDMSpinbox_a0.setSingleStep(0.1)
        self.PyDMSpinbox_a0.setProperty("alarmSensitiveContent", True)
        self.PyDMSpinbox_a0.setProperty("alarmSensitiveBorder", False)
        self.PyDMSpinbox_a0.setProperty("precisionFromPV", False)
        self.PyDMSpinbox_a0.setProperty("precision", 0)
        self.PyDMSpinbox_a0.setProperty("channel", "")
        self.PyDMSpinbox_a0.setProperty("showStepExponent", False)
        self.PyDMSpinbox_a0.setObjectName("PyDMSpinbox_a0")
        self.horizontalLayout_2.addWidget(self.PyDMSpinbox_a0)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(130, 0))
        self.label_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.PyDMSpinbox_aF = PyDMSpinbox(self.centralwidget)
        self.PyDMSpinbox_aF.setEnabled(True)
        self.PyDMSpinbox_aF.setMinimumSize(QtCore.QSize(80, 25))
        self.PyDMSpinbox_aF.setMaximumSize(QtCore.QSize(80, 25))
        self.PyDMSpinbox_aF.setToolTip("")
        self.PyDMSpinbox_aF.setDecimals(2)
        self.PyDMSpinbox_aF.setMinimum(-360.0)
        self.PyDMSpinbox_aF.setMaximum(360.0)
        self.PyDMSpinbox_aF.setSingleStep(0.1)
        self.PyDMSpinbox_aF.setProperty("alarmSensitiveContent", True)
        self.PyDMSpinbox_aF.setProperty("alarmSensitiveBorder", False)
        self.PyDMSpinbox_aF.setProperty("precisionFromPV", False)
        self.PyDMSpinbox_aF.setProperty("precision", 0)
        self.PyDMSpinbox_aF.setProperty("channel", "")
        self.PyDMSpinbox_aF.setProperty("showStepExponent", False)
        self.PyDMSpinbox_aF.setObjectName("PyDMSpinbox_aF")
        self.horizontalLayout_3.addWidget(self.PyDMSpinbox_aF)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(130, 0))
        self.label_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.doubleSpinBox_step = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_step.setMinimumSize(QtCore.QSize(80, 25))
        self.doubleSpinBox_step.setMaximumSize(QtCore.QSize(80, 25))
        self.doubleSpinBox_step.setMinimum(-99.0)
        self.doubleSpinBox_step.setObjectName("doubleSpinBox_step")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_step)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 2)
        self.checkBox_enableMarccd = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_enableMarccd.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.117949 rgba(60,60, 60, 255), stop:0.225641 rgba(60, 60, 60, 255));")
        self.checkBox_enableMarccd.setObjectName("checkBox_enableMarccd")
        self.gridLayout.addWidget(self.checkBox_enableMarccd, 7, 0, 1, 2)
        self.PyDMPushButton_Measure = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_Measure.setToolTip("")
        self.PyDMPushButton_Measure.setStyleSheet("color: rgb(0, 240, 240);")
        self.PyDMPushButton_Measure.setProperty("alarmSensitiveBorder", False)
        self.PyDMPushButton_Measure.setProperty("precisionFromPV", False)
        self.PyDMPushButton_Measure.setProperty("channel", "")
        self.PyDMPushButton_Measure.setObjectName("PyDMPushButton_Measure")
        self.gridLayout.addWidget(self.PyDMPushButton_Measure, 8, 0, 1, 2)
        self.msg = QtWidgets.QLabel(self.centralwidget)
        self.msg.setObjectName("msg")
        self.gridLayout.addWidget(self.msg, 9, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Single Crystal - Motor"))
        self.label.setText(_translate("MainWindow", "Manual Adjustment"))
        self.QMotor.setWhatsThis(_translate("MainWindow", "\n"
"    Widget based on EPICS motor record\n"
"    Details about motor record parameters are found at: https://www3.aps.anl.gov/bcda/synApps/motor/R6-9/motorRecord.html\n"
"    "))
        self.label_3.setText(_translate("MainWindow", "Motion status:"))
        self.PyDMCheckbox_msg.setWhatsThis(_translate("MainWindow", "\n"
"    A QCheckbox with support for Channels and more from PyDM\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    init_channel : str, optional\n"
"        The channel to be used by the widget.\n"
"\n"
"    "))
        self.label_4.setText(_translate("MainWindow", "Inicial angle (Graus):"))
        self.PyDMSpinbox_a0.setWhatsThis(_translate("MainWindow", "\n"
"    A QDoubleSpinBox with support for Channels and more from PyDM.\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    init_channel : str, optional\n"
"        The channel to be used by the widget.\n"
"    "))
        self.label_5.setText(_translate("MainWindow", "Final angle (Graus):"))
        self.PyDMSpinbox_aF.setWhatsThis(_translate("MainWindow", "\n"
"    A QDoubleSpinBox with support for Channels and more from PyDM.\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    init_channel : str, optional\n"
"        The channel to be used by the widget.\n"
"    "))
        self.label_6.setText(_translate("MainWindow", "Step angle (Graus):"))
        self.checkBox_enableMarccd.setText(_translate("MainWindow", "Integrated with X-ray detector"))
        self.PyDMPushButton_Measure.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMPushButton_Measure.setText(_translate("MainWindow", "Capture image and rotate the sample"))
        self.msg.setText(_translate("MainWindow", "Check the box to integrate with X-ray detector"))
        self.label_2.setText(_translate("MainWindow", "Single Crystal"))

from pydm.widgets.checkbox import PyDMCheckbox
from pydm.widgets.pushbutton import PyDMPushButton
from pydm.widgets.spinbox import PyDMSpinbox
#from sol_widgets.widgets.motor import QMotor
from singleCrystal_system.sol_widgets.widgets.motor import QMotor

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

