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
        MainWindow.resize(380, 481)
        MainWindow.setMinimumSize(QtCore.QSize(380, 481))
        MainWindow.setMaximumSize(QtCore.QSize(380, 481))
        MainWindow.setStyleSheet("background-color: rgb(80,80,80);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.QMotor = QMotor(self.centralwidget)
        self.QMotor.setToolTip("")
        self.QMotor.setProperty("channel", "")
        self.QMotor.setObjectName("QMotor")
        self.gridLayout_4.addWidget(self.QMotor, 2, 0, 1, 2)
        self.PyDMDrawingLine = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine.setProperty("brush", brush)
        self.PyDMDrawingLine.setObjectName("PyDMDrawingLine")
        self.gridLayout_4.addWidget(self.PyDMDrawingLine, 6, 0, 1, 2)
        self.PyDMCheckbox_msg = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_msg.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PyDMCheckbox_msg.setFont(font)
        self.PyDMCheckbox_msg.setToolTip("")
        self.PyDMCheckbox_msg.setStyleSheet("")
        self.PyDMCheckbox_msg.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PyDMCheckbox_msg.setIconSize(QtCore.QSize(16, 16))
        self.PyDMCheckbox_msg.setCheckable(True)
        self.PyDMCheckbox_msg.setAutoExclusive(False)
        self.PyDMCheckbox_msg.setTristate(False)
        self.PyDMCheckbox_msg.setProperty("channel", "")
        self.PyDMCheckbox_msg.setObjectName("PyDMCheckbox_msg")
        self.gridLayout_4.addWidget(self.PyDMCheckbox_msg, 7, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_step = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_step.setMinimumSize(QtCore.QSize(80, 25))
        self.doubleSpinBox_step.setMaximumSize(QtCore.QSize(80, 25))
        self.doubleSpinBox_step.setObjectName("doubleSpinBox_step")
        self.gridLayout_3.addWidget(self.doubleSpinBox_step, 2, 2, 1, 1)
        self.PyDMPushButton_Measure = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_Measure.setToolTip("")
        self.PyDMPushButton_Measure.setStyleSheet("\n"
"color: rgb(255, 125, 17);")
        self.PyDMPushButton_Measure.setProperty("alarmSensitiveBorder", False)
        self.PyDMPushButton_Measure.setProperty("precisionFromPV", False)
        self.PyDMPushButton_Measure.setProperty("channel", "")
        self.PyDMPushButton_Measure.setObjectName("PyDMPushButton_Measure")
        self.gridLayout_3.addWidget(self.PyDMPushButton_Measure, 3, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_enableMarccd = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_enableMarccd.setObjectName("checkBox_enableMarccd")
        self.gridLayout_2.addWidget(self.checkBox_enableMarccd, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMSpinbox_a0 = PyDMSpinbox(self.centralwidget)
        self.PyDMSpinbox_a0.setEnabled(True)
        self.PyDMSpinbox_a0.setMinimumSize(QtCore.QSize(80, 25))
        self.PyDMSpinbox_a0.setMaximumSize(QtCore.QSize(80, 25))
        self.PyDMSpinbox_a0.setToolTip("")
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
        self.gridLayout_3.addWidget(self.PyDMSpinbox_a0, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 3, 1, 1)
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
        self.gridLayout_3.addWidget(self.PyDMSpinbox_aF, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.PyDMByteIndicator_integrated = PyDMByteIndicator(self.centralwidget)
        self.PyDMByteIndicator_integrated.setToolTip("")
        self.PyDMByteIndicator_integrated.setProperty("alarmSensitiveBorder", False)
        self.PyDMByteIndicator_integrated.setProperty("precisionFromPV", False)
        self.PyDMByteIndicator_integrated.setProperty("showLabels", True)
        self.PyDMByteIndicator_integrated.setProperty("circles", True)
        self.PyDMByteIndicator_integrated.setProperty("labels", ['Reading'])
        self.PyDMByteIndicator_integrated.setObjectName("PyDMByteIndicator_integrated")
        self.gridLayout_3.addWidget(self.PyDMByteIndicator_integrated, 3, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 4, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 2)
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
        self.QMotor.setWhatsThis(_translate("MainWindow", "\n"
"    Widget based on EPICS motor record\n"
"    Details about motor record parameters are found at: https://www3.aps.anl.gov/bcda/synApps/motor/R6-9/motorRecord.html\n"
"    "))
        self.PyDMDrawingLine.setWhatsThis(_translate("MainWindow", "\n"
"    A widget with a line drawn in it.\n"
"    This class inherits from PyDMDrawing.\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    init_channel : str, optional\n"
"        The channel to be used by the widget.\n"
"    "))
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
        self.PyDMCheckbox_msg.setText(_translate("MainWindow", "No motion is detected."))
        self.label.setText(_translate("MainWindow", "Manual Adjustment"))
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
        self.PyDMPushButton_Measure.setText(_translate("MainWindow", "Measure"))
        self.checkBox_enableMarccd.setText(_translate("MainWindow", "Integrated "))
        self.label_6.setText(_translate("MainWindow", "Step angle (Graus):"))
        self.label_5.setText(_translate("MainWindow", "Final angle (Graus):"))
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
        self.label_4.setText(_translate("MainWindow", "Inicial angle (Graus):"))
        self.PyDMByteIndicator_integrated.setWhatsThis(_translate("MainWindow", "\n"
"    Widget for graphical representation of bits from an integer number\n"
"    with support for Channels and more from PyDM\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    init_channel : str, optional\n"
"        The channel to be used by the widget.\n"
"    "))
        self.label_3.setText(_translate("MainWindow", "Automatic experiment"))
        self.label_2.setText(_translate("MainWindow", "Single Crystal"))

from pydm.widgets.byte import PyDMByteIndicator
from pydm.widgets.checkbox import PyDMCheckbox
from pydm.widgets.drawing import PyDMDrawingLine
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

