# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_motor_nochannel.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_motor(object):
    def setupUi(self, MainWindow_motor):
        MainWindow_motor.setObjectName("MainWindow_motor")
        MainWindow_motor.resize(234, 418)
        MainWindow_motor.setMinimumSize(QtCore.QSize(234, 418))
        MainWindow_motor.setMaximumSize(QtCore.QSize(234, 418))
        MainWindow_motor.setStyleSheet("\n"
"                QFrame#frame_motor > PyDMLabel{\n"
"                  color: rgb(255, 255, 255);\n"
"                }\n"
"\n"
"                QPushButton#PyDMPushButton_stop{\n"
"                  color: rgb(255, 0, 0);\n"
"                }\n"
"\n"
"                QFrame#frame_motor{\n"
"                  background-color: rgb(20, 20, 20);\n"
"                }\n"
"\n"
"                QFrame#frame_controls{\n"
"                  background-color: rgb(255, 255, 255);\n"
"                }\n"
"\n"
"                QCheckBox#check_set{\n"
"                  color: rgb(0, 0, 0);\n"
"                }\n"
"        ")
        self.centralwidget = QtWidgets.QWidget(MainWindow_motor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.PyDMPushButton_stop = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_stop.setToolTip("")
        self.PyDMPushButton_stop.setObjectName("PyDMPushButton_stop")
        self.gridLayout_9.addWidget(self.PyDMPushButton_stop, 2, 2, 1, 1)
        self.PyDMPushButton_move = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_move.setToolTip("")
        self.PyDMPushButton_move.setObjectName("PyDMPushButton_move")
        self.gridLayout_9.addWidget(self.PyDMPushButton_move, 2, 0, 1, 1)
        self.PyDMDrawingCircle = PyDMDrawingCircle(self.centralwidget)
        self.PyDMDrawingCircle.setToolTip("")
        self.PyDMDrawingCircle.setObjectName("PyDMDrawingCircle")
        self.gridLayout_9.addWidget(self.PyDMDrawingCircle, 2, 1, 1, 1)
        self.msg_error = QtWidgets.QLabel(self.centralwidget)
        self.msg_error.setObjectName("msg_error")
        self.gridLayout_9.addWidget(self.msg_error, 3, 0, 1, 3)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dSB_s = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dSB_s.setMinimum(0.1)
        self.dSB_s.setMaximum(50.0)
        self.dSB_s.setSingleStep(0.1)
        self.dSB_s.setObjectName("dSB_s")
        self.gridLayout_2.addWidget(self.dSB_s, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dSB_accl = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dSB_accl.setMinimum(0.1)
        self.dSB_accl.setMaximum(200.0)
        self.dSB_accl.setSingleStep(0.1)
        self.dSB_accl.setObjectName("dSB_accl")
        self.gridLayout.addWidget(self.dSB_accl, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dSB_reduction = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dSB_reduction.setMinimum(1.0)
        self.dSB_reduction.setMaximum(100000.0)
        self.dSB_reduction.setProperty("value", 8000.0)
        self.dSB_reduction.setObjectName("dSB_reduction")
        self.gridLayout_3.addWidget(self.dSB_reduction, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dSB_eff = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dSB_eff.setMinimum(1.0)
        self.dSB_eff.setMaximum(100.0)
        self.dSB_eff.setSingleStep(0.1)
        self.dSB_eff.setProperty("value", 100.0)
        self.dSB_eff.setObjectName("dSB_eff")
        self.gridLayout_4.addWidget(self.dSB_eff, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.cb_Dir = QtWidgets.QComboBox(self.centralwidget)
        self.cb_Dir.setObjectName("cb_Dir")
        self.cb_Dir.addItem("")
        self.cb_Dir.addItem("")
        self.gridLayout_5.addWidget(self.cb_Dir, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 3, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dSB_gpa = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dSB_gpa.setMaximum(200.0)
        self.dSB_gpa.setSingleStep(0.01)
        self.dSB_gpa.setObjectName("dSB_gpa")
        self.gridLayout_6.addWidget(self.dSB_gpa, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_6.addWidget(self.checkBox, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 4, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 5, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.dSB_graus = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dSB_graus.setMinimum(-1000.0)
        self.dSB_graus.setMaximum(1000.0)
        self.dSB_graus.setSingleStep(0.1)
        self.dSB_graus.setProperty("value", 1.0)
        self.dSB_graus.setObjectName("dSB_graus")
        self.gridLayout_7.addWidget(self.dSB_graus, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_7.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 6, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 0, 1, 3)
        self.PyDMPushButton_restart = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_restart.setMaximumSize(QtCore.QSize(60, 20))
        self.PyDMPushButton_restart.setToolTip("")
        self.PyDMPushButton_restart.setObjectName("PyDMPushButton_restart")
        self.gridLayout_9.addWidget(self.PyDMPushButton_restart, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        MainWindow_motor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_motor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 234, 20))
        self.menubar.setObjectName("menubar")
        MainWindow_motor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_motor)
        self.statusbar.setObjectName("statusbar")
        MainWindow_motor.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_motor)
        self.cb_Dir.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_motor)

    def retranslateUi(self, MainWindow_motor):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_motor.setWindowTitle(_translate("MainWindow_motor", "Motor Interface"))
        self.PyDMPushButton_stop.setWhatsThis(_translate("MainWindow_motor", "\n"
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
        self.PyDMPushButton_stop.setText(_translate("MainWindow_motor", "Stop"))
        self.PyDMPushButton_move.setWhatsThis(_translate("MainWindow_motor", "\n"
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
        self.PyDMPushButton_move.setText(_translate("MainWindow_motor", "Move"))
        self.PyDMDrawingCircle.setWhatsThis(_translate("MainWindow_motor", "\n"
"    A widget with a circle drawn in it.\n"
"    This class inherits from PyDMDrawing.\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    init_channel : str, optional\n"
"        The channel to be used by the widget.\n"
"    "))
        self.msg_error.setText(_translate("MainWindow_motor", "Message "))
        self.label_2.setText(_translate("MainWindow_motor", "Velocity (rev/s)"))
        self.label.setText(_translate("MainWindow_motor", "Accel.Time (s)"))
        self.label_4.setText(_translate("MainWindow_motor", "GB Reduction"))
        self.label_5.setText(_translate("MainWindow_motor", "GB efficiency (%)"))
        self.label_3.setText(_translate("MainWindow_motor", "Direction"))
        self.cb_Dir.setItemText(0, _translate("MainWindow_motor", "Positive : Tightening"))
        self.cb_Dir.setItemText(1, _translate("MainWindow_motor", "Negative : Loosening"))
        self.label_6.setText(_translate("MainWindow_motor", "Set desired pressure (GPa)"))
        self.checkBox.setText(_translate("MainWindow_motor", "Select to move"))
        self.label_7.setText(_translate("MainWindow_motor", "Set desired adjustment (°)"))
        self.checkBox_2.setText(_translate("MainWindow_motor", "Select to move"))
        self.PyDMPushButton_restart.setWhatsThis(_translate("MainWindow_motor", "\n"
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
        self.PyDMPushButton_restart.setText(_translate("MainWindow_motor", "Restart"))

from pydm.widgets.drawing import PyDMDrawingCircle
from pydm.widgets.pushbutton import PyDMPushButton

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_motor = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_motor()
    ui.setupUi(MainWindow_motor)
    MainWindow_motor.show()
    sys.exit(app.exec_())

