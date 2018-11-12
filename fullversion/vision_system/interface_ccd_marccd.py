# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_ccd_marccd_3.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ui_MainWindow_marccd(object):
    def setupUi(self, Ui_MainWindow_marccd):
        Ui_MainWindow_marccd.setObjectName("Ui_MainWindow_marccd")
        Ui_MainWindow_marccd.resize(672, 294)
        Ui_MainWindow_marccd.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow_marccd.setMaximumSize(QtCore.QSize(672, 294))
        Ui_MainWindow_marccd.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(Ui_MainWindow_marccd)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.PyDMPushButton_abort = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_abort.setMinimumSize(QtCore.QSize(115, 23))
        self.PyDMPushButton_abort.setMaximumSize(QtCore.QSize(115, 23))
        self.PyDMPushButton_abort.setToolTip("")
        self.PyDMPushButton_abort.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);")
        self.PyDMPushButton_abort.setObjectName("PyDMPushButton_abort")
        self.gridLayout_9.addWidget(self.PyDMPushButton_abort, 7, 3, 1, 1)
        self.PyDMDrawingLine_8 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_8.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_8.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_8.setProperty("brush", brush)
        self.PyDMDrawingLine_8.setObjectName("PyDMDrawingLine_8")
        self.gridLayout_9.addWidget(self.PyDMDrawingLine_8, 4, 0, 1, 4)
        self.PyDMLabel_Filename = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel_Filename.setFont(font)
        self.PyDMLabel_Filename.setToolTip("")
        self.PyDMLabel_Filename.setWhatsThis("")
        self.PyDMLabel_Filename.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_Filename.setObjectName("PyDMLabel_Filename")
        self.gridLayout_9.addWidget(self.PyDMLabel_Filename, 1, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.PyDMDrawingLine_6 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_6.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_6.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_6.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_6.setProperty("brush", brush)
        self.PyDMDrawingLine_6.setObjectName("PyDMDrawingLine_6")
        self.gridLayout_9.addWidget(self.PyDMDrawingLine_6, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PyDMLabel = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.PyDMLabel.setFont(font)
        self.PyDMLabel.setToolTip("")
        self.PyDMLabel.setWhatsThis("")
        self.PyDMLabel.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel.setObjectName("PyDMLabel")
        self.gridLayout.addWidget(self.PyDMLabel, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_IP.setMinimumSize(QtCore.QSize(90, 23))
        self.lineEdit_IP.setMaximumSize(QtCore.QSize(90, 23))
        self.lineEdit_IP.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.gridLayout.addWidget(self.lineEdit_IP, 1, 1, 1, 1)
        self.PyDMDrawingLine_3 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_3.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_3.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_3.setProperty("brush", brush)
        self.PyDMDrawingLine_3.setObjectName("PyDMDrawingLine_3")
        self.gridLayout.addWidget(self.PyDMDrawingLine_3, 0, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.PyDMLabel_exposureOne = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.PyDMLabel_exposureOne.setFont(font)
        self.PyDMLabel_exposureOne.setToolTip("")
        self.PyDMLabel_exposureOne.setWhatsThis("")
        self.PyDMLabel_exposureOne.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_exposureOne.setObjectName("PyDMLabel_exposureOne")
        self.gridLayout_5.addWidget(self.PyDMLabel_exposureOne, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_Exposureone = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEdit_Exposureone.setMinimumSize(QtCore.QSize(70, 0))
        self.lineEdit_Exposureone.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_Exposureone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_Exposureone.setDecimals(0)
        self.lineEdit_Exposureone.setMaximum(10000.0)
        self.lineEdit_Exposureone.setProperty("value", 10.0)
        self.lineEdit_Exposureone.setObjectName("lineEdit_Exposureone")
        self.gridLayout_5.addWidget(self.lineEdit_Exposureone, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_9.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.PyDMLabel_msgerror = PyDMLabel(self.centralwidget)
        self.PyDMLabel_msgerror.setMinimumSize(QtCore.QSize(299, 0))
        self.PyDMLabel_msgerror.setMaximumSize(QtCore.QSize(299, 16777215))
        self.PyDMLabel_msgerror.setToolTip("")
        self.PyDMLabel_msgerror.setWhatsThis("")
        self.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_msgerror.setObjectName("PyDMLabel_msgerror")
        self.gridLayout_9.addWidget(self.PyDMLabel_msgerror, 7, 1, 1, 2)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.PyDMLabel_connectstatus = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel_connectstatus.setFont(font)
        self.PyDMLabel_connectstatus.setToolTip("")
        self.PyDMLabel_connectstatus.setWhatsThis("")
        self.PyDMLabel_connectstatus.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_connectstatus.setObjectName("PyDMLabel_connectstatus")
        self.gridLayout_12.addWidget(self.PyDMLabel_connectstatus, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMPushButton_connect = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_connect.setMinimumSize(QtCore.QSize(150, 0))
        self.PyDMPushButton_connect.setMaximumSize(QtCore.QSize(150, 16777215))
        self.PyDMPushButton_connect.setToolTip("")
        self.PyDMPushButton_connect.setStyleSheet("\n"
"background-color: rgb(75, 75, 75);\n"
"color: rgb(255, 255, 255);")
        self.PyDMPushButton_connect.setObjectName("PyDMPushButton_connect")
        self.gridLayout_12.addWidget(self.PyDMPushButton_connect, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_9.addLayout(self.gridLayout_12, 0, 2, 1, 2)
        self.PyDMDrawingLine_5 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_5.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_5.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_5.setProperty("brush", brush)
        self.PyDMDrawingLine_5.setObjectName("PyDMDrawingLine_5")
        self.gridLayout_9.addWidget(self.PyDMDrawingLine_5, 6, 0, 1, 4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(40, 16))
        self.label.setMaximumSize(QtCore.QSize(40, 16))
        self.label.setStyleSheet("color: rgb(240, 240, 240);")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_filename = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_filename.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_filename.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_filename.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.spinBox_filename.setMaximum(999)
        self.spinBox_filename.setObjectName("spinBox_filename")
        self.gridLayout_4.addWidget(self.spinBox_filename, 0, 3, 1, 1)
        self.sufix = QtWidgets.QLabel(self.centralwidget)
        self.sufix.setMinimumSize(QtCore.QSize(0, 0))
        self.sufix.setMaximumSize(QtCore.QSize(400, 16777215))
        self.sufix.setStyleSheet("color: rgb(240, 240, 240);")
        self.sufix.setObjectName("sufix")
        self.gridLayout_4.addWidget(self.sufix, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_9.addLayout(self.gridLayout_4, 3, 2, 1, 2)
        self.PyDMDrawingLine = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine.setProperty("brush", brush)
        self.PyDMDrawingLine.setObjectName("PyDMDrawingLine")
        self.gridLayout_9.addWidget(self.PyDMDrawingLine, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.PyDMLabel_count = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.PyDMLabel_count.setFont(font)
        self.PyDMLabel_count.setToolTip("")
        self.PyDMLabel_count.setWhatsThis("")
        self.PyDMLabel_count.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_count.setObjectName("PyDMLabel_count")
        self.gridLayout_6.addWidget(self.PyDMLabel_count, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_count = QtWidgets.QSpinBox(self.centralwidget)
        self.lineEdit_count.setMinimumSize(QtCore.QSize(70, 0))
        self.lineEdit_count.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_count.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_count.setProperty("value", 2)
        self.lineEdit_count.setObjectName("lineEdit_count")
        self.gridLayout_6.addWidget(self.lineEdit_count, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_9.addLayout(self.gridLayout_6, 3, 0, 1, 1)
        self.lineEdit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filename.setMinimumSize(QtCore.QSize(100, 23))
        self.lineEdit_filename.setMaximumSize(QtCore.QSize(210, 23))
        self.lineEdit_filename.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.gridLayout_9.addWidget(self.lineEdit_filename, 2, 2, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PyDMLabel_IP = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.PyDMLabel_IP.setFont(font)
        self.PyDMLabel_IP.setToolTip("")
        self.PyDMLabel_IP.setWhatsThis("")
        self.PyDMLabel_IP.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_IP.setObjectName("PyDMLabel_IP")
        self.gridLayout_2.addWidget(self.PyDMLabel_IP, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_Port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Port.setMinimumSize(QtCore.QSize(90, 23))
        self.lineEdit_Port.setMaximumSize(QtCore.QSize(90, 23))
        self.lineEdit_Port.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.gridLayout_2.addWidget(self.lineEdit_Port, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PyDMDrawingLine_4 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_4.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_4.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_4.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_4.setProperty("brush", brush)
        self.PyDMDrawingLine_4.setObjectName("PyDMDrawingLine_4")
        self.gridLayout_2.addWidget(self.PyDMDrawingLine_4, 0, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.binning = QtWidgets.QWidget(self.centralwidget)
        self.binning.setMinimumSize(QtCore.QSize(173, 58))
        self.binning.setMaximumSize(QtCore.QSize(1000, 100))
        self.binning.setStyleSheet("border-color: rgb(200, 200, 200);\n"
"border-width : 0.8px;\n"
"border-style:outset;")
        self.binning.setObjectName("binning")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.binning)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.PyDMCheckbox_512 = PyDMCheckbox(self.binning)
        self.PyDMCheckbox_512.setToolTip("")
        self.PyDMCheckbox_512.setStyleSheet("color: rgb(240, 240, 240);\n"
"border-color: rgb(65, 65, 65);\n"
"border-width : 1.0px;\n"
"border-style:inset;")
        self.PyDMCheckbox_512.setObjectName("PyDMCheckbox_512")
        self.gridLayout_8.addWidget(self.PyDMCheckbox_512, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PyDMCheckbox_1024 = PyDMCheckbox(self.binning)
        self.PyDMCheckbox_1024.setToolTip("")
        self.PyDMCheckbox_1024.setStyleSheet("color: rgb(240, 240, 240);\n"
"border-color: rgb(65, 65, 65);\n"
"border-width : 1.0px;\n"
"border-style:inset;")
        self.PyDMCheckbox_1024.setObjectName("PyDMCheckbox_1024")
        self.gridLayout_8.addWidget(self.PyDMCheckbox_1024, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PyDMCheckbox_2 = PyDMCheckbox(self.binning)
        self.PyDMCheckbox_2.setToolTip("")
        self.PyDMCheckbox_2.setAutoFillBackground(False)
        self.PyDMCheckbox_2.setStyleSheet("color: rgb(240, 240, 240);\n"
"border-color: rgb(65, 65, 65);\n"
"border-width : 1.0px;\n"
"border-style:inset;\n"
"\n"
"")
        self.PyDMCheckbox_2.setChecked(True)
        self.PyDMCheckbox_2.setObjectName("PyDMCheckbox_2")
        self.gridLayout_8.addWidget(self.PyDMCheckbox_2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PyDMLabel_size = PyDMLabel(self.binning)
        self.PyDMLabel_size.setToolTip("")
        self.PyDMLabel_size.setWhatsThis("")
        self.PyDMLabel_size.setStyleSheet("color: rgb(240, 240, 240);\n"
"border-color: rgb(65, 65, 65);\n"
"border-width : 1.0px;\n"
"border-style:inset;")
        self.PyDMLabel_size.setObjectName("PyDMLabel_size")
        self.gridLayout_8.addWidget(self.PyDMLabel_size, 0, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.gridLayout_3.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.binning, 2, 1, 2, 1)
        self.PyDMPushButton_imagesequence = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_imagesequence.setMinimumSize(QtCore.QSize(210, 23))
        self.PyDMPushButton_imagesequence.setMaximumSize(QtCore.QSize(210, 23))
        self.PyDMPushButton_imagesequence.setToolTip("")
        self.PyDMPushButton_imagesequence.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);")
        self.PyDMPushButton_imagesequence.setObjectName("PyDMPushButton_imagesequence")
        self.gridLayout_9.addWidget(self.PyDMPushButton_imagesequence, 7, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.PyDMLabel_path = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.PyDMLabel_path.setFont(font)
        self.PyDMLabel_path.setToolTip("")
        self.PyDMLabel_path.setWhatsThis("")
        self.PyDMLabel_path.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_path.setObjectName("PyDMLabel_path")
        self.gridLayout_7.addWidget(self.PyDMLabel_path, 0, 0, 1, 1)
        self.lineEdit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_path.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_path.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lineEdit_path.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.gridLayout_7.addWidget(self.lineEdit_path, 1, 0, 1, 1)
        self.PyDMPushButtonSelect = PyDMPushButton(self.centralwidget)
        self.PyDMPushButtonSelect.setToolTip("")
        self.PyDMPushButtonSelect.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);")
        self.PyDMPushButtonSelect.setObjectName("PyDMPushButtonSelect")
        self.gridLayout_7.addWidget(self.PyDMPushButtonSelect, 1, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 5, 0, 1, 4)
        self.binning.raise_()
        self.PyDMDrawingLine.raise_()
        self.PyDMDrawingLine_5.raise_()
        self.PyDMDrawingLine_6.raise_()
        self.PyDMDrawingLine_8.raise_()
        self.PyDMPushButton_imagesequence.raise_()
        self.PyDMPushButton_abort.raise_()
        self.PyDMLabel_msgerror.raise_()
        self.PyDMLabel_Filename.raise_()
        self.label.raise_()
        self.spinBox_filename.raise_()
        self.lineEdit_filename.raise_()
        Ui_MainWindow_marccd.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ui_MainWindow_marccd)
        self.statusbar.setObjectName("statusbar")
        Ui_MainWindow_marccd.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Ui_MainWindow_marccd)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(Ui_MainWindow_marccd)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow_marccd)

    def retranslateUi(self, Ui_MainWindow_marccd):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow_marccd.setWindowTitle(_translate("Ui_MainWindow_marccd", "Marccd: Image Capture"))
        self.PyDMPushButton_abort.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMPushButton_abort.setText(_translate("Ui_MainWindow_marccd", "Abort acquisition"))
        self.PyDMDrawingLine_8.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMLabel_Filename.setText(_translate("Ui_MainWindow_marccd", "Image filename"))
        self.PyDMDrawingLine_6.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMLabel.setText(_translate("Ui_MainWindow_marccd", "CCD server IP: "))
        self.lineEdit_IP.setText(_translate("Ui_MainWindow_marccd", "10.2.18.32"))
        self.PyDMDrawingLine_3.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMLabel_exposureOne.setText(_translate("Ui_MainWindow_marccd", "Exposure (s):"))
        self.PyDMLabel_msgerror.setText(_translate("Ui_MainWindow_marccd", "Mensagem error"))
        self.PyDMLabel_connectstatus.setText(_translate("Ui_MainWindow_marccd", "Connection status: OFF"))
        self.PyDMPushButton_connect.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMPushButton_connect.setText(_translate("Ui_MainWindow_marccd", "Connect to Marccd"))
        self.PyDMDrawingLine_5.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.label.setText(_translate("Ui_MainWindow_marccd", "Suffix:"))
        self.sufix.setText(_translate("Ui_MainWindow_marccd", "_n000.tiff"))
        self.PyDMDrawingLine.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMLabel_count.setText(_translate("Ui_MainWindow_marccd", "Multread image:"))
        self.lineEdit_filename.setText(_translate("Ui_MainWindow_marccd", "lab6_3p20GPa_300K_300s"))
        self.PyDMLabel_IP.setText(_translate("Ui_MainWindow_marccd", "CCD server Port:"))
        self.lineEdit_Port.setText(_translate("Ui_MainWindow_marccd", "2222"))
        self.PyDMDrawingLine_4.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMCheckbox_512.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMCheckbox_512.setText(_translate("Ui_MainWindow_marccd", "8x8"))
        self.PyDMCheckbox_1024.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMCheckbox_1024.setText(_translate("Ui_MainWindow_marccd", "4x4"))
        self.PyDMCheckbox_2.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMCheckbox_2.setText(_translate("Ui_MainWindow_marccd", "2x2"))
        self.PyDMLabel_size.setText(_translate("Ui_MainWindow_marccd", "Pixel Binning"))
        self.PyDMPushButton_imagesequence.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMPushButton_imagesequence.setText(_translate("Ui_MainWindow_marccd", "Capture calibration image"))
        self.PyDMLabel_path.setText(_translate("Ui_MainWindow_marccd", "Write directory path where files wiil be saved: "))
        self.lineEdit_path.setText(_translate("Ui_MainWindow_marccd", "/home/ABTLUS/rodrigo.guercio/workspace/ema/ema/ema_software/"))
        self.PyDMPushButtonSelect.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMPushButtonSelect.setText(_translate("Ui_MainWindow_marccd", "Select"))
        self.actionOpen.setText(_translate("Ui_MainWindow_marccd", "Open"))

from pydm.widgets.checkbox import PyDMCheckbox
from pydm.widgets.drawing import PyDMDrawingLine
from pydm.widgets.label import PyDMLabel
from pydm.widgets.pushbutton import PyDMPushButton

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow_marccd = QtWidgets.QMainWindow()
    ui = Ui_Ui_MainWindow_marccd()
    ui.setupUi(Ui_MainWindow_marccd)
    Ui_MainWindow_marccd.show()
    sys.exit(app.exec_())

