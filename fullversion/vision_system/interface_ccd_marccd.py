# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_marccd_2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ui_MainWindow_marccd(object):
    def setupUi(self, Ui_MainWindow_marccd):
        Ui_MainWindow_marccd.setObjectName("Ui_MainWindow_marccd")
        Ui_MainWindow_marccd.resize(575, 500)
        Ui_MainWindow_marccd.setMinimumSize(QtCore.QSize(575, 500))
        Ui_MainWindow_marccd.setMaximumSize(QtCore.QSize(575, 500))
        Ui_MainWindow_marccd.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(Ui_MainWindow_marccd)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.PyDMDrawingLine_9 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_9.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_9.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_9.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(0, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_9.setProperty("brush", brush)
        self.PyDMDrawingLine_9.setObjectName("PyDMDrawingLine_9")
        self.gridLayout.addWidget(self.PyDMDrawingLine_9, 0, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PyDMLabel = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel.setFont(font)
        self.PyDMLabel.setToolTip("")
        self.PyDMLabel.setWhatsThis("")
        self.PyDMLabel.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel.setObjectName("PyDMLabel")
        self.verticalLayout_2.addWidget(self.PyDMLabel, 0, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_IP = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel_IP.setFont(font)
        self.PyDMLabel_IP.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_IP.setObjectName("PyDMLabel_IP")
        self.verticalLayout_2.addWidget(self.PyDMLabel_IP, 0, QtCore.Qt.AlignHCenter)
        self.PyDMDrawingLine_11 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_11.setMinimumSize(QtCore.QSize(15, 15))
        self.PyDMDrawingLine_11.setMaximumSize(QtCore.QSize(15, 15))
        self.PyDMDrawingLine_11.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(0, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_11.setProperty("brush", brush)
        self.PyDMDrawingLine_11.setObjectName("PyDMDrawingLine_11")
        self.verticalLayout_2.addWidget(self.PyDMDrawingLine_11, 0, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_exposureOne = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel_exposureOne.setFont(font)
        self.PyDMLabel_exposureOne.setToolTip("")
        self.PyDMLabel_exposureOne.setWhatsThis("")
        self.PyDMLabel_exposureOne.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_exposureOne.setObjectName("PyDMLabel_exposureOne")
        self.verticalLayout_2.addWidget(self.PyDMLabel_exposureOne, 0, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_count = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel_count.setFont(font)
        self.PyDMLabel_count.setToolTip("")
        self.PyDMLabel_count.setWhatsThis("")
        self.PyDMLabel_count.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_count.setObjectName("PyDMLabel_count")
        self.verticalLayout_2.addWidget(self.PyDMLabel_count, 0, QtCore.Qt.AlignHCenter)
        self.label_cumulative = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_cumulative.setFont(font)
        self.label_cumulative.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_cumulative.setObjectName("label_cumulative")
        self.verticalLayout_2.addWidget(self.label_cumulative, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_IP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_IP.setMinimumSize(QtCore.QSize(90, 23))
        self.lineEdit_IP.setMaximumSize(QtCore.QSize(90, 23))
        self.lineEdit_IP.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.verticalLayout.addWidget(self.lineEdit_IP, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_Port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Port.setMinimumSize(QtCore.QSize(90, 0))
        self.lineEdit_Port.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lineEdit_Port.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.verticalLayout.addWidget(self.lineEdit_Port, 0, QtCore.Qt.AlignHCenter)
        self.PyDMDrawingLine_10 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_10.setMinimumSize(QtCore.QSize(15, 15))
        self.PyDMDrawingLine_10.setMaximumSize(QtCore.QSize(15, 15))
        self.PyDMDrawingLine_10.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(0, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_10.setProperty("brush", brush)
        self.PyDMDrawingLine_10.setObjectName("PyDMDrawingLine_10")
        self.verticalLayout.addWidget(self.PyDMDrawingLine_10, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_Exposureone = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEdit_Exposureone.setMinimumSize(QtCore.QSize(90, 0))
        self.lineEdit_Exposureone.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lineEdit_Exposureone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_Exposureone.setDecimals(4)
        self.lineEdit_Exposureone.setMinimum(0.0001)
        self.lineEdit_Exposureone.setMaximum(100000.0)
        self.lineEdit_Exposureone.setProperty("value", 10.0)
        self.lineEdit_Exposureone.setObjectName("lineEdit_Exposureone")
        self.verticalLayout.addWidget(self.lineEdit_Exposureone, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_count = QtWidgets.QSpinBox(self.centralwidget)
        self.lineEdit_count.setMinimumSize(QtCore.QSize(90, 0))
        self.lineEdit_count.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lineEdit_count.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_count.setMinimum(1)
        self.lineEdit_count.setProperty("value", 2)
        self.lineEdit_count.setObjectName("lineEdit_count")
        self.verticalLayout.addWidget(self.lineEdit_count, 0, QtCore.Qt.AlignHCenter)
        self.spinBox_cumulative = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_cumulative.setMinimumSize(QtCore.QSize(90, 0))
        self.spinBox_cumulative.setMaximumSize(QtCore.QSize(90, 16777215))
        self.spinBox_cumulative.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.spinBox_cumulative.setMinimum(1)
        self.spinBox_cumulative.setMaximum(256)
        self.spinBox_cumulative.setObjectName("spinBox_cumulative")
        self.verticalLayout.addWidget(self.spinBox_cumulative, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 1)
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
        self.gridLayout.addLayout(self.gridLayout_12, 1, 2, 1, 1)
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
        self.gridLayout_3.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.binning, 2, 2, 1, 1)
        self.PyDMDrawingLine_8 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_8.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_8.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(0, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_8.setProperty("brush", brush)
        self.PyDMDrawingLine_8.setObjectName("PyDMDrawingLine_8")
        self.gridLayout.addWidget(self.PyDMDrawingLine_8, 3, 0, 1, 3)
        self.PyDMDrawingLine_5 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_5.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_5.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(0, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_5.setProperty("brush", brush)
        self.PyDMDrawingLine_5.setObjectName("PyDMDrawingLine_5")
        self.gridLayout.addWidget(self.PyDMDrawingLine_5, 6, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PyDMPushButton_imagesequence = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_imagesequence.setMinimumSize(QtCore.QSize(210, 23))
        self.PyDMPushButton_imagesequence.setMaximumSize(QtCore.QSize(210, 23))
        self.PyDMPushButton_imagesequence.setToolTip("")
        self.PyDMPushButton_imagesequence.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);")
        self.PyDMPushButton_imagesequence.setObjectName("PyDMPushButton_imagesequence")
        self.horizontalLayout.addWidget(self.PyDMPushButton_imagesequence)
        spacerItem2 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.PyDMPushButton_abort = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_abort.setMinimumSize(QtCore.QSize(115, 23))
        self.PyDMPushButton_abort.setMaximumSize(QtCore.QSize(115, 23))
        self.PyDMPushButton_abort.setToolTip("")
        self.PyDMPushButton_abort.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);")
        self.PyDMPushButton_abort.setObjectName("PyDMPushButton_abort")
        self.horizontalLayout.addWidget(self.PyDMPushButton_abort)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 3)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.PyDMLabel_Filename = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel_Filename.setFont(font)
        self.PyDMLabel_Filename.setToolTip("")
        self.PyDMLabel_Filename.setWhatsThis("")
        self.PyDMLabel_Filename.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_Filename.setObjectName("PyDMLabel_Filename")
        self.gridLayout_9.addWidget(self.PyDMLabel_Filename, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filename.setMinimumSize(QtCore.QSize(100, 23))
        self.lineEdit_filename.setMaximumSize(QtCore.QSize(400, 23))
        self.lineEdit_filename.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.horizontalLayout_2.addWidget(self.lineEdit_filename)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(40, 16))
        self.label.setMaximumSize(QtCore.QSize(40, 16))
        self.label.setStyleSheet("color: rgb(240, 240, 240);")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.spinBox_filename = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_filename.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_filename.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_filename.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.spinBox_filename.setMaximum(999)
        self.spinBox_filename.setObjectName("spinBox_filename")
        self.gridLayout_4.addWidget(self.spinBox_filename, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.sufix = QtWidgets.QLabel(self.centralwidget)
        self.sufix.setMinimumSize(QtCore.QSize(0, 0))
        self.sufix.setMaximumSize(QtCore.QSize(400, 16777215))
        self.sufix.setStyleSheet("color: rgb(240, 240, 240);")
        self.sufix.setObjectName("sufix")
        self.gridLayout_4.addWidget(self.sufix, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout_9.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_9, 4, 0, 1, 3)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
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
        self.PyDMLabel_path = PyDMLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PyDMLabel_path.setFont(font)
        self.PyDMLabel_path.setToolTip("")
        self.PyDMLabel_path.setWhatsThis("")
        self.PyDMLabel_path.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_path.setObjectName("PyDMLabel_path")
        self.gridLayout_7.addWidget(self.PyDMLabel_path, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_7, 5, 0, 1, 3)
        self.PyDMLabel_msgerror = PyDMLabel(self.centralwidget)
        self.PyDMLabel_msgerror.setMinimumSize(QtCore.QSize(299, 0))
        self.PyDMLabel_msgerror.setMaximumSize(QtCore.QSize(800, 16777215))
        self.PyDMLabel_msgerror.setToolTip("")
        self.PyDMLabel_msgerror.setWhatsThis("")
        self.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_msgerror.setObjectName("PyDMLabel_msgerror")
        self.gridLayout.addWidget(self.PyDMLabel_msgerror, 8, 0, 1, 3)
        Ui_MainWindow_marccd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_MainWindow_marccd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 20))
        self.menubar.setObjectName("menubar")
        Ui_MainWindow_marccd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_MainWindow_marccd)
        self.statusbar.setObjectName("statusbar")
        Ui_MainWindow_marccd.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_MainWindow_marccd)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow_marccd)

    def retranslateUi(self, Ui_MainWindow_marccd):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow_marccd.setWindowTitle(_translate("Ui_MainWindow_marccd", "X-Ray detector communication"))
        self.PyDMDrawingLine_9.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMLabel_IP.setText(_translate("Ui_MainWindow_marccd", "CCD server Port:"))
        self.PyDMDrawingLine_11.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMLabel_count.setText(_translate("Ui_MainWindow_marccd", "Multread image:"))
        self.label_cumulative.setText(_translate("Ui_MainWindow_marccd", "Cumulative reading:"))
        self.lineEdit_IP.setText(_translate("Ui_MainWindow_marccd", "10.2.18.38"))
        self.lineEdit_Port.setText(_translate("Ui_MainWindow_marccd", "2222"))
        self.PyDMDrawingLine_10.setWhatsThis(_translate("Ui_MainWindow_marccd", "\n"
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
        self.PyDMLabel_Filename.setText(_translate("Ui_MainWindow_marccd", "Write a filename to your image of diffraction:"))
        self.lineEdit_filename.setText(_translate("Ui_MainWindow_marccd", "lab6_0p00GPa_300K_300s_2mr_1cm"))
        self.label.setText(_translate("Ui_MainWindow_marccd", "Suffix:"))
        self.sufix.setText(_translate("Ui_MainWindow_marccd", "_n000.tiff"))
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
        self.PyDMLabel_path.setText(_translate("Ui_MainWindow_marccd", "Write directory path where files wiil be saved: "))
        self.PyDMLabel_msgerror.setText(_translate("Ui_MainWindow_marccd", "Mensagem error"))

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

