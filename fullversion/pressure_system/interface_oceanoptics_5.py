# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_oceanoptics_full.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ui_MainWindow_Ocean(object):
    def setupUi(self, Ui_MainWindow_Ocean):
        Ui_MainWindow_Ocean.setObjectName("Ui_MainWindow_Ocean")
        Ui_MainWindow_Ocean.resize(1026, 813)
        Ui_MainWindow_Ocean.setMinimumSize(QtCore.QSize(1026, 813))
        Ui_MainWindow_Ocean.setMaximumSize(QtCore.QSize(1026, 813))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Ui_MainWindow_Ocean.setPalette(palette)
        Ui_MainWindow_Ocean.setStyleSheet("background-color: rgb(80,80,80);\n"
"color: rgb(240, 240, 240);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Ui_MainWindow_Ocean)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.wvRaw = PyDMWaveformPlot(self.centralwidget)
        self.wvRaw.setMinimumSize(QtCore.QSize(501, 440))
        self.wvRaw.setMaximumSize(QtCore.QSize(501, 440))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wvRaw.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        self.wvRaw.setFont(font)
        self.wvRaw.setToolTip("")
        self.wvRaw.setWhatsThis("")
        self.wvRaw.setStyleSheet("")
        self.wvRaw.setLineWidth(3)
        self.wvRaw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.wvRaw.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.wvRaw.setForegroundBrush(brush)
        self.wvRaw.setInteractive(True)
        self.wvRaw.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.wvRaw.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.wvRaw.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.wvRaw.setShowXGrid(True)
        self.wvRaw.setShowYGrid(False)
        self.wvRaw.setBackgroundColor(QtGui.QColor(255, 255, 255))
        self.wvRaw.setAxisColor(QtGui.QColor(0, 0, 0))
        self.wvRaw.setProperty("title", "")
        self.wvRaw.setProperty("maxRedrawRate", 30)
        self.wvRaw.setCurves([])
        self.wvRaw.setAutoRangeX(True)
        self.wvRaw.setAutoRangeY(True)
        self.wvRaw.setProperty("curveColor", QtGui.QColor(255, 255, 255))
        self.wvRaw.setProperty("yChannel", "")
        self.wvRaw.setProperty("xChannel", "")
        self.wvRaw.setObjectName("wvRaw")
        self.gridLayout_2.addWidget(self.wvRaw, 1, 0, 1, 2)
        self.wvDark = PyDMWaveformPlot(self.centralwidget)
        self.wvDark.setMinimumSize(QtCore.QSize(501, 440))
        self.wvDark.setMaximumSize(QtCore.QSize(501, 440))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wvDark.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.wvDark.setFont(font)
        self.wvDark.setToolTip("")
        self.wvDark.setWhatsThis("")
        self.wvDark.setStyleSheet("")
        self.wvDark.setInputMethodHints(QtCore.Qt.ImhNone)
        self.wvDark.setLineWidth(3)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.wvDark.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.wvDark.setForegroundBrush(brush)
        self.wvDark.setShowXGrid(True)
        self.wvDark.setShowYGrid(False)
        self.wvDark.setBackgroundColor(QtGui.QColor(255, 255, 255))
        self.wvDark.setAxisColor(QtGui.QColor(0, 0, 0))
        self.wvDark.setProperty("title", "")
        self.wvDark.setShowLegend(False)
        self.wvDark.setCurves([])
        self.wvDark.setAutoRangeX(True)
        self.wvDark.setAutoRangeY(True)
        self.wvDark.setProperty("curveColor", QtGui.QColor(255, 255, 255))
        self.wvDark.setProperty("yChannel", "")
        self.wvDark.setProperty("xChannel", "")
        self.wvDark.setObjectName("wvDark")
        self.gridLayout_2.addWidget(self.wvDark, 1, 2, 1, 1)
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setMinimumSize(QtCore.QSize(501, 190))
        self.toolBox.setMaximumSize(QtCore.QSize(501, 190))
        self.toolBox.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"color: rgb(240, 240,240);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.117949 rgba(60,60, 60, 255), stop:0.225641 rgba(60, 60, 60, 255));")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 501, 132))
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.lblAcquiring = PyDMLabel(self.page)
        self.lblAcquiring.setMinimumSize(QtCore.QSize(80, 20))
        self.lblAcquiring.setMaximumSize(QtCore.QSize(80, 20))
        self.lblAcquiring.setToolTip("")
        self.lblAcquiring.setWhatsThis("")
        self.lblAcquiring.setStyleSheet("")
        self.lblAcquiring.setObjectName("lblAcquiring")
        self.horizontalLayout_2.addWidget(self.lblAcquiring)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.chkDark = PyDMCheckbox(self.page)
        self.chkDark.setEnabled(True)
        self.chkDark.setMinimumSize(QtCore.QSize(138, 0))
        self.chkDark.setMaximumSize(QtCore.QSize(138, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.chkDark.setFont(font)
        self.chkDark.setToolTip("")
        self.chkDark.setStyleSheet("")
        self.chkDark.setChecked(False)
        self.chkDark.setProperty("alarmSensitiveContent", False)
        self.chkDark.setProperty("alarmSensitiveBorder", True)
        self.chkDark.setProperty("precisionFromPV", True)
        self.chkDark.setProperty("channel", "")
        self.chkDark.setObjectName("chkDark")
        self.gridLayout_13.addWidget(self.chkDark, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.Enable_motor = QtWidgets.QCheckBox(self.page)
        self.Enable_motor.setMinimumSize(QtCore.QSize(111, 21))
        self.Enable_motor.setMaximumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.Enable_motor.setFont(font)
        self.Enable_motor.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Enable_motor.setAcceptDrops(False)
        self.Enable_motor.setAutoFillBackground(False)
        self.Enable_motor.setStyleSheet("")
        self.Enable_motor.setObjectName("Enable_motor")
        self.gridLayout_13.addWidget(self.Enable_motor, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addLayout(self.gridLayout_13, 0, 1, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.lblProgress = PyDMLabel(self.page)
        self.lblProgress.setMinimumSize(QtCore.QSize(80, 20))
        self.lblProgress.setMaximumSize(QtCore.QSize(80, 20))
        self.lblProgress.setToolTip("")
        self.lblProgress.setWhatsThis("")
        self.lblProgress.setStyleSheet("")
        self.lblProgress.setObjectName("lblProgress")
        self.horizontalLayout_3.addWidget(self.lblProgress)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.chkTrigger = PyDMCheckbox(self.page)
        self.chkTrigger.setMinimumSize(QtCore.QSize(111, 21))
        self.chkTrigger.setMaximumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.chkTrigger.setFont(font)
        self.chkTrigger.setToolTip("")
        self.chkTrigger.setStyleSheet("")
        self.chkTrigger.setTristate(False)
        self.chkTrigger.setProperty("alarmSensitiveContent", False)
        self.chkTrigger.setProperty("alarmSensitiveBorder", True)
        self.chkTrigger.setProperty("precisionFromPV", True)
        self.chkTrigger.setProperty("channel", "")
        self.chkTrigger.setObjectName("chkTrigger")
        self.gridLayout_15.addWidget(self.chkTrigger, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.chkAuto = QtWidgets.QCheckBox(self.page)
        self.chkAuto.setMinimumSize(QtCore.QSize(138, 0))
        self.chkAuto.setMaximumSize(QtCore.QSize(138, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.chkAuto.setFont(font)
        self.chkAuto.setStyleSheet("")
        self.chkAuto.setChecked(True)
        self.chkAuto.setObjectName("chkAuto")
        self.gridLayout_15.addWidget(self.chkAuto, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_15, 1, 1, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.edtIntegration = QtWidgets.QDoubleSpinBox(self.page)
        self.edtIntegration.setMinimumSize(QtCore.QSize(70, 0))
        self.edtIntegration.setMaximumSize(QtCore.QSize(70, 16777215))
        self.edtIntegration.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(50, 50, 50);")
        self.edtIntegration.setDecimals(2)
        self.edtIntegration.setMinimum(0.01)
        self.edtIntegration.setMaximum(20.0)
        self.edtIntegration.setSingleStep(0.1)
        self.edtIntegration.setProperty("value", 0.3)
        self.edtIntegration.setObjectName("edtIntegration")
        self.horizontalLayout_4.addWidget(self.edtIntegration, 0, QtCore.Qt.AlignRight)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.btnAcquireStop = PyDMPushButton(self.page)
        self.btnAcquireStop.setToolTip("")
        self.btnAcquireStop.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.btnAcquireStop.setObjectName("btnAcquireStop")
        self.gridLayout_4.addWidget(self.btnAcquireStop, 3, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_36 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_6.addWidget(self.label_36, 0, QtCore.Qt.AlignHCenter)
        self.doubleSpinBox_lblTemp = QtWidgets.QDoubleSpinBox(self.page)
        self.doubleSpinBox_lblTemp.setMinimumSize(QtCore.QSize(70, 0))
        self.doubleSpinBox_lblTemp.setMaximumSize(QtCore.QSize(70, 16777215))
        self.doubleSpinBox_lblTemp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.doubleSpinBox_lblTemp.setMouseTracking(False)
        self.doubleSpinBox_lblTemp.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(50, 50, 50);")
        self.doubleSpinBox_lblTemp.setMinimum(0.01)
        self.doubleSpinBox_lblTemp.setMaximum(100000.0)
        self.doubleSpinBox_lblTemp.setProperty("value", 300.0)
        self.doubleSpinBox_lblTemp.setObjectName("doubleSpinBox_lblTemp")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_lblTemp)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.btnAcquire = PyDMPushButton(self.page)
        self.btnAcquire.setEnabled(True)
        self.btnAcquire.setMinimumSize(QtCore.QSize(0, 0))
        self.btnAcquire.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnAcquire.setToolTip("")
        self.btnAcquire.setWhatsThis("")
        self.btnAcquire.setStyleSheet("color: rgb(255, 69, 0);\n"
"background-color: rgb(70, 70, 70);\n"
"")
        self.btnAcquire.setProperty("channel", "")
        self.btnAcquire.setObjectName("btnAcquire")
        self.gridLayout_4.addWidget(self.btnAcquire, 3, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.cmbAcquisition = PyDMEnumComboBox(self.page)
        self.cmbAcquisition.setMinimumSize(QtCore.QSize(135, 0))
        self.cmbAcquisition.setMaximumSize(QtCore.QSize(135, 16777215))
        self.cmbAcquisition.setToolTip("")
        self.cmbAcquisition.setProperty("alarmSensitiveBorder", False)
        self.cmbAcquisition.setObjectName("cmbAcquisition")
        self.horizontalLayout_7.addWidget(self.cmbAcquisition, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 2, 1, 1, 3)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 501, 132))
        self.page_2.setObjectName("page_2")
        self.PyDMPushButton_stop = PyDMPushButton(self.page_2)
        self.PyDMPushButton_stop.setGeometry(QtCore.QRect(260, 90, 95, 23))
        self.PyDMPushButton_stop.setToolTip("")
        self.PyDMPushButton_stop.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.PyDMPushButton_stop.setObjectName("PyDMPushButton_stop")
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(361, 79, 110, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.dSB_eff = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.dSB_eff.setMinimumSize(QtCore.QSize(80, 0))
        self.dSB_eff.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dSB_eff.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(50, 50, 50);")
        self.dSB_eff.setMinimum(1.0)
        self.dSB_eff.setMaximum(100.0)
        self.dSB_eff.setSingleStep(0.1)
        self.dSB_eff.setProperty("value", 2.0)
        self.dSB_eff.setObjectName("dSB_eff")
        self.gridLayout_28.addWidget(self.dSB_eff, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_28.addWidget(self.label_28, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(13, 3, 458, 70))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.dSB_graus = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.dSB_graus.setMinimumSize(QtCore.QSize(80, 0))
        self.dSB_graus.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dSB_graus.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(50, 50, 50);")
        self.dSB_graus.setDecimals(2)
        self.dSB_graus.setMinimum(-8000.0)
        self.dSB_graus.setMaximum(8000.0)
        self.dSB_graus.setSingleStep(0.01)
        self.dSB_graus.setProperty("value", 5.0)
        self.dSB_graus.setObjectName("dSB_graus")
        self.gridLayout_24.addWidget(self.dSB_graus, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.checkBox_degrees = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_degrees.setStyleSheet("")
        self.checkBox_degrees.setObjectName("checkBox_degrees")
        self.gridLayout_24.addWidget(self.checkBox_degrees, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_26.addLayout(self.gridLayout_24, 1, 1, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.dSB_gpa = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.dSB_gpa.setMinimumSize(QtCore.QSize(80, 0))
        self.dSB_gpa.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dSB_gpa.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(50, 50, 50);")
        self.dSB_gpa.setMinimum(0.01)
        self.dSB_gpa.setMaximum(200.0)
        self.dSB_gpa.setSingleStep(0.1)
        self.dSB_gpa.setProperty("value", 1.0)
        self.dSB_gpa.setObjectName("dSB_gpa")
        self.gridLayout_19.addWidget(self.dSB_gpa, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.checkBox_Gpa = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_Gpa.setStyleSheet("")
        self.checkBox_Gpa.setChecked(True)
        self.checkBox_Gpa.setObjectName("checkBox_Gpa")
        self.gridLayout_19.addWidget(self.checkBox_Gpa, 0, 1, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_19, 1, 0, 1, 1)
        self.PyDMDrawingLine_4 = PyDMDrawingLine(self.layoutWidget1)
        self.PyDMDrawingLine_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.PyDMDrawingLine_4.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_4.setProperty("brush", brush)
        self.PyDMDrawingLine_4.setObjectName("PyDMDrawingLine_4")
        self.gridLayout_26.addWidget(self.PyDMDrawingLine_4, 2, 0, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_26.setStyleSheet("border-color: rgb(240, 240, 240);\n"
"border-width : 1.0px;\n"
"border-style:inset;")
        self.label_26.setObjectName("label_26")
        self.gridLayout_26.addWidget(self.label_26, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_24.setStyleSheet("border-color: rgb(240, 240, 240);\n"
"border-width : 1.0px;\n"
"border-style:inset;")
        self.label_24.setObjectName("label_24")
        self.gridLayout_26.addWidget(self.label_24, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.layoutWidget2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(13, 79, 95, 46))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_27.addWidget(self.label_27, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dSB_s = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.dSB_s.setMinimumSize(QtCore.QSize(80, 0))
        self.dSB_s.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dSB_s.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(50, 50, 50);")
        self.dSB_s.setDecimals(2)
        self.dSB_s.setMinimum(0.1)
        self.dSB_s.setMaximum(80.0)
        self.dSB_s.setSingleStep(0.1)
        self.dSB_s.setProperty("value", 5.0)
        self.dSB_s.setObjectName("dSB_s")
        self.gridLayout_27.addWidget(self.dSB_s, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMDrawingCircle = PyDMDrawingCircle(self.page_2)
        self.PyDMDrawingCircle.setGeometry(QtCore.QRect(214, 82, 40, 40))
        self.PyDMDrawingCircle.setMaximumSize(QtCore.QSize(40, 40))
        self.PyDMDrawingCircle.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingCircle.setProperty("brush", brush)
        self.PyDMDrawingCircle.setObjectName("PyDMDrawingCircle")
        self.PyDMPushButton_move = PyDMPushButton(self.page_2)
        self.PyDMPushButton_move.setGeometry(QtCore.QRect(114, 90, 94, 23))
        self.PyDMPushButton_move.setToolTip("")
        self.PyDMPushButton_move.setStyleSheet("color: rgb(255, 69, 0);\n"
"background-color: rgb(70, 70, 70);")
        self.PyDMPushButton_move.setObjectName("PyDMPushButton_move")
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout_2.addWidget(self.toolBox, 2, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(501, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(501, 260))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(60, 60, 60);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_32 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setObjectName("label_32")
        self.gridLayout_8.addWidget(self.label_32, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.PyDMLabel_19 = PyDMLabel(self.tab)
        self.PyDMLabel_19.setToolTip("")
        self.PyDMLabel_19.setWhatsThis("")
        self.PyDMLabel_19.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_19.setObjectName("PyDMLabel_19")
        self.gridLayout_5.addWidget(self.PyDMLabel_19, 4, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PyDMLabel_14 = PyDMLabel(self.tab)
        self.PyDMLabel_14.setToolTip("")
        self.PyDMLabel_14.setWhatsThis("")
        self.PyDMLabel_14.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_14.setObjectName("PyDMLabel_14")
        self.gridLayout_5.addWidget(self.PyDMLabel_14, 8, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PyDMLabel_30 = PyDMLabel(self.tab)
        self.PyDMLabel_30.setToolTip("")
        self.PyDMLabel_30.setWhatsThis("")
        self.PyDMLabel_30.setStyleSheet("")
        self.PyDMLabel_30.setObjectName("PyDMLabel_30")
        self.gridLayout_5.addWidget(self.PyDMLabel_30, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineEdit_1Count = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_1Count.setMinimumSize(QtCore.QSize(60, 0))
        self.LineEdit_1Count.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LineEdit_1Count.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_1Count.setObjectName("LineEdit_1Count")
        self.gridLayout_5.addWidget(self.LineEdit_1Count, 8, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.LineEdit_2Count = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_2Count.setMinimumSize(QtCore.QSize(60, 0))
        self.LineEdit_2Count.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LineEdit_2Count.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_2Count.setObjectName("LineEdit_2Count")
        self.gridLayout_5.addWidget(self.LineEdit_2Count, 8, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.LineEdit_2GPa = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_2GPa.setMinimumSize(QtCore.QSize(50, 0))
        self.LineEdit_2GPa.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LineEdit_2GPa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);\n"
"")
        self.LineEdit_2GPa.setObjectName("LineEdit_2GPa")
        self.gridLayout_5.addWidget(self.LineEdit_2GPa, 4, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.LineEdit_1nm = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_1nm.setMinimumSize(QtCore.QSize(60, 0))
        self.LineEdit_1nm.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LineEdit_1nm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_1nm.setObjectName("LineEdit_1nm")
        self.gridLayout_5.addWidget(self.LineEdit_1nm, 6, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.LineEdit_2nm = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_2nm.setMinimumSize(QtCore.QSize(60, 0))
        self.LineEdit_2nm.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LineEdit_2nm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_2nm.setObjectName("LineEdit_2nm")
        self.gridLayout_5.addWidget(self.LineEdit_2nm, 6, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PyDMLabel_13 = PyDMLabel(self.tab)
        self.PyDMLabel_13.setToolTip("")
        self.PyDMLabel_13.setWhatsThis("")
        self.PyDMLabel_13.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_13.setObjectName("PyDMLabel_13")
        self.gridLayout_5.addWidget(self.PyDMLabel_13, 6, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PyDMLabel_20 = PyDMLabel(self.tab)
        self.PyDMLabel_20.setToolTip("")
        self.PyDMLabel_20.setWhatsThis("")
        self.PyDMLabel_20.setStyleSheet("")
        self.PyDMLabel_20.setObjectName("PyDMLabel_20")
        self.gridLayout_5.addWidget(self.PyDMLabel_20, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel = PyDMLabel(self.tab)
        self.PyDMLabel.setToolTip("")
        self.PyDMLabel.setWhatsThis("")
        self.PyDMLabel.setStyleSheet("")
        self.PyDMLabel.setObjectName("PyDMLabel")
        self.gridLayout_5.addWidget(self.PyDMLabel, 6, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.LineEdit_1GPa = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_1GPa.setMinimumSize(QtCore.QSize(50, 0))
        self.LineEdit_1GPa.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LineEdit_1GPa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_1GPa.setObjectName("LineEdit_1GPa")
        self.gridLayout_5.addWidget(self.LineEdit_1GPa, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PyDMLabel_32 = PyDMLabel(self.tab)
        self.PyDMLabel_32.setToolTip("")
        self.PyDMLabel_32.setWhatsThis("")
        self.PyDMLabel_32.setStyleSheet("")
        self.PyDMLabel_32.setObjectName("PyDMLabel_32")
        self.gridLayout_5.addWidget(self.PyDMLabel_32, 8, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PyDMLabel_6 = PyDMLabel(self.tab)
        self.PyDMLabel_6.setMinimumSize(QtCore.QSize(0, 0))
        self.PyDMLabel_6.setToolTip("")
        self.PyDMLabel_6.setWhatsThis("")
        self.PyDMLabel_6.setStyleSheet("")
        self.PyDMLabel_6.setObjectName("PyDMLabel_6")
        self.gridLayout_5.addWidget(self.PyDMLabel_6, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMDrawingLine = PyDMDrawingLine(self.tab)
        self.PyDMDrawingLine.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine.setToolTip("")
        self.PyDMDrawingLine.setStyleSheet("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine.setProperty("brush", brush)
        self.PyDMDrawingLine.setObjectName("PyDMDrawingLine")
        self.gridLayout_5.addWidget(self.PyDMDrawingLine, 2, 1, 1, 7)
        self.PyDMLabel_7 = PyDMLabel(self.tab)
        self.PyDMLabel_7.setMinimumSize(QtCore.QSize(0, 0))
        self.PyDMLabel_7.setToolTip("")
        self.PyDMLabel_7.setWhatsThis("")
        self.PyDMLabel_7.setStyleSheet("")
        self.PyDMLabel_7.setObjectName("PyDMLabel_7")
        self.gridLayout_5.addWidget(self.PyDMLabel_7, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMPushButton_PressureCalc = PyDMPushButton(self.tab)
        self.PyDMPushButton_PressureCalc.setMinimumSize(QtCore.QSize(20, 0))
        self.PyDMPushButton_PressureCalc.setMaximumSize(QtCore.QSize(20, 16777215))
        self.PyDMPushButton_PressureCalc.setToolTip("")
        self.PyDMPushButton_PressureCalc.setStyleSheet("color: rgb(255, 69, 0);\n"
"background-color: rgb(70, 70, 70);\n"
"")
        self.PyDMPushButton_PressureCalc.setObjectName("PyDMPushButton_PressureCalc")
        self.gridLayout_5.addWidget(self.PyDMPushButton_PressureCalc, 6, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMPushButton_PositionCalc = PyDMPushButton(self.tab)
        self.PyDMPushButton_PositionCalc.setMinimumSize(QtCore.QSize(20, 0))
        self.PyDMPushButton_PositionCalc.setMaximumSize(QtCore.QSize(20, 16777215))
        self.PyDMPushButton_PositionCalc.setToolTip("")
        self.PyDMPushButton_PositionCalc.setStyleSheet("color: rgb(255, 69, 0);\n"
"background-color: rgb(70, 70, 70);")
        self.PyDMPushButton_PositionCalc.setObjectName("PyDMPushButton_PositionCalc")
        self.gridLayout_5.addWidget(self.PyDMPushButton_PositionCalc, 4, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMPushButton_tempCalc = PyDMPushButton(self.tab)
        self.PyDMPushButton_tempCalc.setMinimumSize(QtCore.QSize(20, 0))
        self.PyDMPushButton_tempCalc.setMaximumSize(QtCore.QSize(20, 16777215))
        self.PyDMPushButton_tempCalc.setToolTip("")
        self.PyDMPushButton_tempCalc.setStyleSheet("color: rgb(255, 69, 0);\n"
"background-color: rgb(70, 70, 70);")
        self.PyDMPushButton_tempCalc.setObjectName("PyDMPushButton_tempCalc")
        self.gridLayout_5.addWidget(self.PyDMPushButton_tempCalc, 8, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_3 = PyDMLabel(self.tab)
        self.PyDMLabel_3.setToolTip("")
        self.PyDMLabel_3.setWhatsThis("")
        self.PyDMLabel_3.setStyleSheet("")
        self.PyDMLabel_3.setObjectName("PyDMLabel_3")
        self.gridLayout_5.addWidget(self.PyDMLabel_3, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_1nm_result = PyDMLabel(self.tab)
        self.PyDMLabel_1nm_result.setMinimumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_1nm_result.setMaximumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_1nm_result.setToolTip("")
        self.PyDMLabel_1nm_result.setWhatsThis("")
        self.PyDMLabel_1nm_result.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_1nm_result.setObjectName("PyDMLabel_1nm_result")
        self.gridLayout_5.addWidget(self.PyDMLabel_1nm_result, 4, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_1Gpa_result = PyDMLabel(self.tab)
        self.PyDMLabel_1Gpa_result.setMinimumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_1Gpa_result.setMaximumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_1Gpa_result.setToolTip("")
        self.PyDMLabel_1Gpa_result.setWhatsThis("")
        self.PyDMLabel_1Gpa_result.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_1Gpa_result.setObjectName("PyDMLabel_1Gpa_result")
        self.gridLayout_5.addWidget(self.PyDMLabel_1Gpa_result, 6, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_2Gpa_result = PyDMLabel(self.tab)
        self.PyDMLabel_2Gpa_result.setMinimumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_2Gpa_result.setMaximumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_2Gpa_result.setToolTip("")
        self.PyDMLabel_2Gpa_result.setWhatsThis("")
        self.PyDMLabel_2Gpa_result.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_2Gpa_result.setObjectName("PyDMLabel_2Gpa_result")
        self.gridLayout_5.addWidget(self.PyDMLabel_2Gpa_result, 6, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_2nm_result = PyDMLabel(self.tab)
        self.PyDMLabel_2nm_result.setMinimumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_2nm_result.setMaximumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_2nm_result.setToolTip("")
        self.PyDMLabel_2nm_result.setWhatsThis("")
        self.PyDMLabel_2nm_result.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_2nm_result.setObjectName("PyDMLabel_2nm_result")
        self.gridLayout_5.addWidget(self.PyDMLabel_2nm_result, 4, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.Checkbox2pPltPosition = QtWidgets.QCheckBox(self.tab)
        self.Checkbox2pPltPosition.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.117949 rgba(60,60, 60, 255), stop:0.225641 rgba(60, 60, 60, 255));")
        self.Checkbox2pPltPosition.setChecked(True)
        self.Checkbox2pPltPosition.setObjectName("Checkbox2pPltPosition")
        self.gridLayout_5.addWidget(self.Checkbox2pPltPosition, 4, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_5 = PyDMLabel(self.tab)
        self.PyDMLabel_5.setToolTip("")
        self.PyDMLabel_5.setWhatsThis("")
        self.PyDMLabel_5.setStyleSheet("")
        self.PyDMLabel_5.setObjectName("PyDMLabel_5")
        self.gridLayout_5.addWidget(self.PyDMLabel_5, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setStyleSheet("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 0, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_temp_result = PyDMLabel(self.tab)
        self.PyDMLabel_temp_result.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMLabel_temp_result.setMaximumSize(QtCore.QSize(69, 15))
        self.PyDMLabel_temp_result.setToolTip("")
        self.PyDMLabel_temp_result.setWhatsThis("")
        self.PyDMLabel_temp_result.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_temp_result.setObjectName("PyDMLabel_temp_result")
        self.gridLayout_5.addWidget(self.PyDMLabel_temp_result, 8, 5, 1, 2, QtCore.Qt.AlignHCenter)
        self.PyDMDrawingLine_5 = PyDMDrawingLine(self.tab)
        self.PyDMDrawingLine_5.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_5.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_5.setProperty("brush", brush)
        self.PyDMDrawingLine_5.setObjectName("PyDMDrawingLine_5")
        self.gridLayout_5.addWidget(self.PyDMDrawingLine_5, 5, 1, 1, 7)
        self.PyDMDrawingLine_7 = PyDMDrawingLine(self.tab)
        self.PyDMDrawingLine_7.setMinimumSize(QtCore.QSize(0, 15))
        self.PyDMDrawingLine_7.setMaximumSize(QtCore.QSize(16777215, 15))
        self.PyDMDrawingLine_7.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_7.setProperty("brush", brush)
        self.PyDMDrawingLine_7.setObjectName("PyDMDrawingLine_7")
        self.gridLayout_5.addWidget(self.PyDMDrawingLine_7, 7, 1, 1, 7)
        self.gridLayout_8.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PyDMLabel_tempCalc = PyDMLabel(self.tab)
        self.PyDMLabel_tempCalc.setToolTip("")
        self.PyDMLabel_tempCalc.setWhatsThis("")
        self.PyDMLabel_tempCalc.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_tempCalc.setObjectName("PyDMLabel_tempCalc")
        self.horizontalLayout.addWidget(self.PyDMLabel_tempCalc)
        self.LineEdit_tempBase = QtWidgets.QLineEdit(self.tab)
        self.LineEdit_tempBase.setMinimumSize(QtCore.QSize(40, 23))
        self.LineEdit_tempBase.setMaximumSize(QtCore.QSize(50, 23))
        self.LineEdit_tempBase.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_tempBase.setObjectName("LineEdit_tempBase")
        self.horizontalLayout.addWidget(self.LineEdit_tempBase, 0, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_tempUnit = PyDMLabel(self.tab)
        self.PyDMLabel_tempUnit.setToolTip("")
        self.PyDMLabel_tempUnit.setWhatsThis("")
        self.PyDMLabel_tempUnit.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_tempUnit.setObjectName("PyDMLabel_tempUnit")
        self.horizontalLayout.addWidget(self.PyDMLabel_tempUnit)
        self.gridLayout_8.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.PyDMDrawingLine_2 = PyDMDrawingLine(self.tab_2)
        self.PyDMDrawingLine_2.setMinimumSize(QtCore.QSize(0, 17))
        self.PyDMDrawingLine_2.setMaximumSize(QtCore.QSize(16777215, 17))
        self.PyDMDrawingLine_2.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_2.setProperty("brush", brush)
        self.PyDMDrawingLine_2.setObjectName("PyDMDrawingLine_2")
        self.gridLayout_10.addWidget(self.PyDMDrawingLine_2, 1, 0, 1, 5)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_9.addWidget(self.label_23, 1, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_9 = PyDMLabel(self.tab_2)
        self.PyDMLabel_9.setToolTip("")
        self.PyDMLabel_9.setWhatsThis("")
        self.PyDMLabel_9.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_9.setObjectName("PyDMLabel_9")
        self.gridLayout_9.addWidget(self.PyDMLabel_9, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineEdit_tempBase_2 = QtWidgets.QLineEdit(self.tab_2)
        self.LineEdit_tempBase_2.setMinimumSize(QtCore.QSize(75, 23))
        self.LineEdit_tempBase_2.setMaximumSize(QtCore.QSize(75, 23))
        self.LineEdit_tempBase_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_tempBase_2.setObjectName("LineEdit_tempBase_2")
        self.gridLayout_9.addWidget(self.LineEdit_tempBase_2, 1, 5, 1, 1)
        self.LineEdit_1nm_2 = QtWidgets.QLineEdit(self.tab_2)
        self.LineEdit_1nm_2.setMinimumSize(QtCore.QSize(75, 0))
        self.LineEdit_1nm_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.LineEdit_1nm_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_1nm_2.setObjectName("LineEdit_1nm_2")
        self.gridLayout_9.addWidget(self.LineEdit_1nm_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_31 = PyDMLabel(self.tab_2)
        self.PyDMLabel_31.setToolTip("")
        self.PyDMLabel_31.setWhatsThis("")
        self.PyDMLabel_31.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_31.setObjectName("PyDMLabel_31")
        self.gridLayout_9.addWidget(self.PyDMLabel_31, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_33 = PyDMLabel(self.tab_2)
        self.PyDMLabel_33.setToolTip("")
        self.PyDMLabel_33.setWhatsThis("")
        self.PyDMLabel_33.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_33.setObjectName("PyDMLabel_33")
        self.gridLayout_9.addWidget(self.PyDMLabel_33, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_10 = PyDMLabel(self.tab_2)
        self.PyDMLabel_10.setToolTip("")
        self.PyDMLabel_10.setWhatsThis("")
        self.PyDMLabel_10.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_10.setObjectName("PyDMLabel_10")
        self.gridLayout_9.addWidget(self.PyDMLabel_10, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_2 = PyDMLabel(self.tab_2)
        self.PyDMLabel_2.setToolTip("")
        self.PyDMLabel_2.setWhatsThis("")
        self.PyDMLabel_2.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_2.setObjectName("PyDMLabel_2")
        self.gridLayout_9.addWidget(self.PyDMLabel_2, 1, 0, 1, 1)
        self.PyDMLabel_4 = PyDMLabel(self.tab_2)
        self.PyDMLabel_4.setToolTip("")
        self.PyDMLabel_4.setWhatsThis("")
        self.PyDMLabel_4.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_4.setObjectName("PyDMLabel_4")
        self.gridLayout_9.addWidget(self.PyDMLabel_4, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineEdit_2nm_2 = QtWidgets.QLineEdit(self.tab_2)
        self.LineEdit_2nm_2.setMinimumSize(QtCore.QSize(75, 0))
        self.LineEdit_2nm_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.LineEdit_2nm_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.LineEdit_2nm_2.setObjectName("LineEdit_2nm_2")
        self.gridLayout_9.addWidget(self.LineEdit_2nm_2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMLabel_11 = PyDMLabel(self.tab_2)
        self.PyDMLabel_11.setToolTip("")
        self.PyDMLabel_11.setWhatsThis("")
        self.PyDMLabel_11.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_11.setObjectName("PyDMLabel_11")
        self.gridLayout_9.addWidget(self.PyDMLabel_11, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_9.addWidget(self.label_30, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_10.addLayout(self.gridLayout_9, 2, 0, 1, 5)
        self.PyDMDrawingLine_3 = PyDMDrawingLine(self.tab_2)
        self.PyDMDrawingLine_3.setMinimumSize(QtCore.QSize(0, 17))
        self.PyDMDrawingLine_3.setMaximumSize(QtCore.QSize(16777215, 17))
        self.PyDMDrawingLine_3.setToolTip("")
        self.PyDMDrawingLine_3.setStyleSheet("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_3.setProperty("brush", brush)
        self.PyDMDrawingLine_3.setObjectName("PyDMDrawingLine_3")
        self.gridLayout_10.addWidget(self.PyDMDrawingLine_3, 4, 0, 1, 5)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_12.addWidget(self.label_20, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.PyDMPushButton = PyDMPushButton(self.tab_2)
        self.PyDMPushButton.setToolTip("")
        self.PyDMPushButton.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.PyDMPushButton.setObjectName("PyDMPushButton")
        self.gridLayout_12.addWidget(self.PyDMPushButton, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_12, 5, 0, 1, 2)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_14.addWidget(self.label_21, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_14.addWidget(self.label_22, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_10.addLayout(self.gridLayout_14, 5, 2, 1, 3)
        self.PyDMPushButton_setSV = PyDMPushButton(self.tab_2)
        self.PyDMPushButton_setSV.setMinimumSize(QtCore.QSize(140, 0))
        self.PyDMPushButton_setSV.setToolTip("")
        self.PyDMPushButton_setSV.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.PyDMPushButton_setSV.setObjectName("PyDMPushButton_setSV")
        self.gridLayout_10.addWidget(self.PyDMPushButton_setSV, 3, 4, 1, 1)
        self.PyDMLabel_tempCalc_3 = PyDMLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.PyDMLabel_tempCalc_3.setFont(font)
        self.PyDMLabel_tempCalc_3.setToolTip("")
        self.PyDMLabel_tempCalc_3.setWhatsThis("")
        self.PyDMLabel_tempCalc_3.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_tempCalc_3.setObjectName("PyDMLabel_tempCalc_3")
        self.gridLayout_10.addWidget(self.PyDMLabel_tempCalc_3, 0, 0, 1, 5, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.leLower3 = PyDMLineEdit(self.tab_4)
        self.leLower3.setEnabled(True)
        self.leLower3.setToolTip("")
        self.leLower3.setWhatsThis("")
        self.leLower3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leLower3.setMaxLength(7)
        self.leLower3.setProperty("alarmSensitiveBorder", False)
        self.leLower3.setObjectName("leLower3")
        self.gridLayout.addWidget(self.leLower3, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.leLower4 = PyDMLineEdit(self.tab_4)
        self.leLower4.setEnabled(True)
        self.leLower4.setToolTip("")
        self.leLower4.setWhatsThis("")
        self.leLower4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leLower4.setMaxLength(7)
        self.leLower4.setProperty("alarmSensitiveBorder", False)
        self.leLower4.setObjectName("leLower4")
        self.gridLayout.addWidget(self.leLower4, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.leLower2 = PyDMLineEdit(self.tab_4)
        self.leLower2.setEnabled(True)
        self.leLower2.setToolTip("")
        self.leLower2.setWhatsThis("")
        self.leLower2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leLower2.setMaxLength(7)
        self.leLower2.setProperty("alarmSensitiveBorder", False)
        self.leLower2.setProperty("channel", "")
        self.leLower2.setObjectName("leLower2")
        self.gridLayout.addWidget(self.leLower2, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lblLuminescence5 = PyDMLabel(self.tab_4)
        self.lblLuminescence5.setToolTip("")
        self.lblLuminescence5.setWhatsThis("")
        self.lblLuminescence5.setStyleSheet("color: rgb(240, 240, 240);")
        self.lblLuminescence5.setObjectName("lblLuminescence5")
        self.gridLayout.addWidget(self.lblLuminescence5, 5, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.leLower5 = PyDMLineEdit(self.tab_4)
        self.leLower5.setEnabled(True)
        self.leLower5.setToolTip("")
        self.leLower5.setWhatsThis("")
        self.leLower5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leLower5.setMaxLength(7)
        self.leLower5.setProperty("alarmSensitiveBorder", False)
        self.leLower5.setObjectName("leLower5")
        self.gridLayout.addWidget(self.leLower5, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lblLuminescence2 = PyDMLabel(self.tab_4)
        self.lblLuminescence2.setToolTip("")
        self.lblLuminescence2.setWhatsThis("")
        self.lblLuminescence2.setStyleSheet("color: rgb(240, 240, 240);")
        self.lblLuminescence2.setObjectName("lblLuminescence2")
        self.gridLayout.addWidget(self.lblLuminescence2, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.leLower1 = PyDMLineEdit(self.tab_4)
        self.leLower1.setEnabled(True)
        self.leLower1.setToolTip("")
        self.leLower1.setWhatsThis("")
        self.leLower1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leLower1.setMaxLength(7)
        self.leLower1.setProperty("alarmSensitiveBorder", False)
        self.leLower1.setProperty("channel", "")
        self.leLower1.setProperty("usePrecision", False)
        self.leLower1.setObjectName("leLower1")
        self.gridLayout.addWidget(self.leLower1, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lblLuminescence3 = PyDMLabel(self.tab_4)
        self.lblLuminescence3.setToolTip("")
        self.lblLuminescence3.setWhatsThis("")
        self.lblLuminescence3.setStyleSheet("color: rgb(240, 240, 240);")
        self.lblLuminescence3.setObjectName("lblLuminescence3")
        self.gridLayout.addWidget(self.lblLuminescence3, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.leUpper3 = PyDMLineEdit(self.tab_4)
        self.leUpper3.setEnabled(True)
        self.leUpper3.setToolTip("")
        self.leUpper3.setWhatsThis("")
        self.leUpper3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leUpper3.setMaxLength(7)
        self.leUpper3.setProperty("alarmSensitiveBorder", False)
        self.leUpper3.setObjectName("leUpper3")
        self.gridLayout.addWidget(self.leUpper3, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.leUpper5 = PyDMLineEdit(self.tab_4)
        self.leUpper5.setEnabled(True)
        self.leUpper5.setToolTip("")
        self.leUpper5.setWhatsThis("")
        self.leUpper5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leUpper5.setMaxLength(7)
        self.leUpper5.setProperty("alarmSensitiveBorder", False)
        self.leUpper5.setObjectName("leUpper5")
        self.gridLayout.addWidget(self.leUpper5, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.lblLuminescence1 = PyDMLabel(self.tab_4)
        self.lblLuminescence1.setToolTip("")
        self.lblLuminescence1.setWhatsThis("")
        self.lblLuminescence1.setStyleSheet("color: rgb(240, 240, 240);")
        self.lblLuminescence1.setProperty("channel", "")
        self.lblLuminescence1.setObjectName("lblLuminescence1")
        self.gridLayout.addWidget(self.lblLuminescence1, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.lblLuminescenceTotal = PyDMLabel(self.tab_4)
        self.lblLuminescenceTotal.setToolTip("")
        self.lblLuminescenceTotal.setWhatsThis("")
        self.lblLuminescenceTotal.setStyleSheet("color: rgb(240, 240, 240);")
        self.lblLuminescenceTotal.setObjectName("lblLuminescenceTotal")
        self.gridLayout.addWidget(self.lblLuminescenceTotal, 6, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.leUpper2 = PyDMLineEdit(self.tab_4)
        self.leUpper2.setEnabled(True)
        self.leUpper2.setToolTip("")
        self.leUpper2.setWhatsThis("")
        self.leUpper2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leUpper2.setMaxLength(7)
        self.leUpper2.setProperty("alarmSensitiveBorder", False)
        self.leUpper2.setObjectName("leUpper2")
        self.gridLayout.addWidget(self.leUpper2, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.lblLuminescence4 = PyDMLabel(self.tab_4)
        self.lblLuminescence4.setToolTip("")
        self.lblLuminescence4.setWhatsThis("")
        self.lblLuminescence4.setStyleSheet("color: rgb(240, 240, 240);")
        self.lblLuminescence4.setObjectName("lblLuminescence4")
        self.gridLayout.addWidget(self.lblLuminescence4, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.leUpper1 = PyDMLineEdit(self.tab_4)
        self.leUpper1.setEnabled(True)
        self.leUpper1.setToolTip("")
        self.leUpper1.setWhatsThis("")
        self.leUpper1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leUpper1.setMaxLength(7)
        self.leUpper1.setProperty("alarmSensitiveBorder", False)
        self.leUpper1.setProperty("channel", "")
        self.leUpper1.setObjectName("leUpper1")
        self.gridLayout.addWidget(self.leUpper1, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.leUpper4 = PyDMLineEdit(self.tab_4)
        self.leUpper4.setEnabled(True)
        self.leUpper4.setToolTip("")
        self.leUpper4.setWhatsThis("")
        self.leUpper4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.leUpper4.setMaxLength(7)
        self.leUpper4.setProperty("alarmSensitiveBorder", False)
        self.leUpper4.setObjectName("leUpper4")
        self.gridLayout.addWidget(self.leUpper4, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_7.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_7.addWidget(self.label_31, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PyDMDrawingLine_9 = PyDMDrawingLine(self.tab_3)
        self.PyDMDrawingLine_9.setMinimumSize(QtCore.QSize(0, 17))
        self.PyDMDrawingLine_9.setMaximumSize(QtCore.QSize(16777215, 17))
        self.PyDMDrawingLine_9.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_9.setProperty("brush", brush)
        self.PyDMDrawingLine_9.setObjectName("PyDMDrawingLine_9")
        self.gridLayout_3.addWidget(self.PyDMDrawingLine_9, 2, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setStyleSheet("color: rgb(240, 240, 240);")
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.btnPath = QtWidgets.QPushButton(self.tab_3)
        self.btnPath.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.btnPath.setObjectName("btnPath")
        self.gridLayout_6.addWidget(self.btnPath, 0, 3, 1, 3, QtCore.Qt.AlignRight)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 2, 3, 1, 2)
        self.lblFileName = QtWidgets.QLineEdit(self.tab_3)
        self.lblFileName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lblFileName.setObjectName("lblFileName")
        self.gridLayout_6.addWidget(self.lblFileName, 2, 1, 1, 1)
        self.sufix = QtWidgets.QLabel(self.tab_3)
        self.sufix.setMinimumSize(QtCore.QSize(80, 0))
        self.sufix.setMaximumSize(QtCore.QSize(80, 16777215))
        self.sufix.setObjectName("sufix")
        self.gridLayout_6.addWidget(self.sufix, 2, 2, 1, 1)
        self.lblPath = QtWidgets.QLineEdit(self.tab_3)
        self.lblPath.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")
        self.lblPath.setObjectName("lblPath")
        self.gridLayout_6.addWidget(self.lblPath, 0, 1, 1, 2)
        self.btnAcqSave = QtWidgets.QPushButton(self.tab_3)
        self.btnAcqSave.setStyleSheet("background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 69, 0);")
        self.btnAcqSave.setObjectName("btnAcqSave")
        self.gridLayout_6.addWidget(self.btnAcqSave, 4, 0, 1, 6, QtCore.Qt.AlignHCenter)
        self.sbRuns = QtWidgets.QSpinBox(self.tab_3)
        self.sbRuns.setMinimumSize(QtCore.QSize(50, 0))
        self.sbRuns.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sbRuns.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(50, 50, 50);")
        self.sbRuns.setMinimum(0)
        self.sbRuns.setMaximum(999)
        self.sbRuns.setProperty("value", 0)
        self.sbRuns.setObjectName("sbRuns")
        self.gridLayout_6.addWidget(self.sbRuns, 2, 5, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_6, 3, 0, 1, 4)
        self.PyDMDrawingLine_10 = PyDMDrawingLine(self.tab_3)
        self.PyDMDrawingLine_10.setMinimumSize(QtCore.QSize(0, 17))
        self.PyDMDrawingLine_10.setMaximumSize(QtCore.QSize(16777215, 17))
        self.PyDMDrawingLine_10.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_10.setProperty("brush", brush)
        self.PyDMDrawingLine_10.setObjectName("PyDMDrawingLine_10")
        self.gridLayout_3.addWidget(self.PyDMDrawingLine_10, 4, 0, 1, 4)
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 1, 0, 1, 4, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 2, 2, 1)
        self.lcdPressure = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdPressure.setMinimumSize(QtCore.QSize(501, 64))
        self.lcdPressure.setMaximumSize(QtCore.QSize(501, 64))
        self.lcdPressure.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 0, 0);")
        self.lcdPressure.setProperty("intValue", -1)
        self.lcdPressure.setObjectName("lcdPressure")
        self.gridLayout_2.addWidget(self.lcdPressure, 3, 0, 1, 2)
        self.msg_error = QtWidgets.QLabel(self.centralwidget)
        self.msg_error.setMinimumSize(QtCore.QSize(420, 0))
        self.msg_error.setMaximumSize(QtCore.QSize(420, 15))
        self.msg_error.setObjectName("msg_error")
        self.gridLayout_2.addWidget(self.msg_error, 4, 0, 1, 1)
        self.PyDMLabel_GPa = PyDMLabel(self.centralwidget)
        self.PyDMLabel_GPa.setMinimumSize(QtCore.QSize(26, 10))
        self.PyDMLabel_GPa.setMaximumSize(QtCore.QSize(26, 10))
        self.PyDMLabel_GPa.setToolTip("")
        self.PyDMLabel_GPa.setWhatsThis("")
        self.PyDMLabel_GPa.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMLabel_GPa.setObjectName("PyDMLabel_GPa")
        self.gridLayout_2.addWidget(self.PyDMLabel_GPa, 4, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.centersOfLoren = QtWidgets.QLabel(self.centralwidget)
        self.centersOfLoren.setMinimumSize(QtCore.QSize(0, 0))
        self.centersOfLoren.setMaximumSize(QtCore.QSize(144, 1000))
        self.centersOfLoren.setObjectName("centersOfLoren")
        self.horizontalLayout_5.addWidget(self.centersOfLoren, 0, QtCore.Qt.AlignHCenter)
        self.label_centerswaves = QtWidgets.QLabel(self.centralwidget)
        self.label_centerswaves.setMinimumSize(QtCore.QSize(100, 0))
        self.label_centerswaves.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_centerswaves.setObjectName("label_centerswaves")
        self.horizontalLayout_5.addWidget(self.label_centerswaves, 0, QtCore.Qt.AlignHCenter)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_5.addWidget(self.label_25)
        self.lblTemp_rubi = QtWidgets.QLabel(self.centralwidget)
        self.lblTemp_rubi.setMinimumSize(QtCore.QSize(40, 0))
        self.lblTemp_rubi.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lblTemp_rubi.setObjectName("lblTemp_rubi")
        self.horizontalLayout_5.addWidget(self.lblTemp_rubi)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_5.addWidget(self.label_35, 0, QtCore.Qt.AlignHCenter)
        self.lblTemp = PyDMLineEdit(self.centralwidget)
        self.lblTemp.setEnabled(True)
        self.lblTemp.setMinimumSize(QtCore.QSize(55, 0))
        self.lblTemp.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lblTemp.setToolTip("")
        self.lblTemp.setWhatsThis("")
        self.lblTemp.setProperty("precisionFromPV", True)
        self.lblTemp.setProperty("precision", 0)
        self.lblTemp.setObjectName("lblTemp")
        self.horizontalLayout_5.addWidget(self.lblTemp)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 2, 1, 1)
        self.PyDMDrawingLine_6 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_6.setGeometry(QtCore.QRect(9, 445, 501, 20))
        self.PyDMDrawingLine_6.setMinimumSize(QtCore.QSize(0, 20))
        self.PyDMDrawingLine_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.PyDMDrawingLine_6.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_6.setProperty("brush", brush)
        self.PyDMDrawingLine_6.setObjectName("PyDMDrawingLine_6")
        self.PyDMDrawingLine_8 = PyDMDrawingLine(self.centralwidget)
        self.PyDMDrawingLine_8.setGeometry(QtCore.QRect(516, 445, 501, 20))
        self.PyDMDrawingLine_8.setMinimumSize(QtCore.QSize(0, 20))
        self.PyDMDrawingLine_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.PyDMDrawingLine_8.setToolTip("")
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMDrawingLine_8.setProperty("brush", brush)
        self.PyDMDrawingLine_8.setObjectName("PyDMDrawingLine_8")
        self.PyDMDrawingLine_6.raise_()
        self.wvRaw.raise_()
        self.PyDMDrawingLine_8.raise_()
        self.lcdPressure.raise_()
        self.wvDark.raise_()
        self.tabWidget.raise_()
        self.toolBox.raise_()
        self.msg_error.raise_()
        self.PyDMLabel_GPa.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        Ui_MainWindow_Ocean.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_MainWindow_Ocean)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 20))
        self.menubar.setObjectName("menubar")
        Ui_MainWindow_Ocean.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_MainWindow_Ocean)
        self.statusbar.setObjectName("statusbar")
        Ui_MainWindow_Ocean.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(Ui_MainWindow_Ocean)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen_2 = QtWidgets.QAction(Ui_MainWindow_Ocean)
        self.actionOpen_2.setCheckable(True)
        self.actionOpen_2.setObjectName("actionOpen_2")

        self.retranslateUi(Ui_MainWindow_Ocean)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow_Ocean)

    def retranslateUi(self, Ui_MainWindow_Ocean):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow_Ocean.setWindowTitle(_translate("Ui_MainWindow_Ocean", "Dioptics 0.0.1 - 2018 Guercio R based on © 2017 BRAZILIAN SYNCHROTRON LIGHT SOURCE <sol@lnls.br> "))
        self.label_33.setText(_translate("Ui_MainWindow_Ocean", "Raw Spectra: a.u. vs nm"))
        self.label_34.setText(_translate("Ui_MainWindow_Ocean", "Dark Corrected Spectra: a.u. vs nm"))
        self.label_3.setText(_translate("Ui_MainWindow_Ocean", " Acquire Status:"))
        self.lblAcquiring.setText(_translate("Ui_MainWindow_Ocean", "PyDMLabel"))
        self.chkDark.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.chkDark.setText(_translate("Ui_MainWindow_Ocean", "Dark Correction  "))
        self.Enable_motor.setText(_translate("Ui_MainWindow_Ocean", "Enable motor"))
        self.label_6.setText(_translate("Ui_MainWindow_Ocean", "Percentage (%):"))
        self.lblProgress.setText(_translate("Ui_MainWindow_Ocean", "PyDMLabel"))
        self.chkTrigger.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.chkTrigger.setText(_translate("Ui_MainWindow_Ocean", "Trigger"))
        self.chkAuto.setText(_translate("Ui_MainWindow_Ocean", "2nd peak line plot"))
        self.label_5.setText(_translate("Ui_MainWindow_Ocean", "Integration time (s):"))
        self.btnAcquireStop.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.btnAcquireStop.setText(_translate("Ui_MainWindow_Ocean", "Stop"))
        self.label_36.setText(_translate("Ui_MainWindow_Ocean", "DAC Temperature (K):"))
        self.btnAcquire.setText(_translate("Ui_MainWindow_Ocean", "Start"))
        self.btnAcquire.setProperty("pressValue", _translate("Ui_MainWindow_Ocean", "1"))
        self.label_4.setText(_translate("Ui_MainWindow_Ocean", "Acquisition Mode:"))
        self.cmbAcquisition.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
"    A QComboBox with support for Channels and more from PyDM\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    init_channel : str, optional\n"
"        The channel to be used by the widget.\n"
"\n"
"    Signals\n"
"    -------\n"
"    send_value_signal : int, float, str, bool or np.ndarray\n"
"        Emitted when the user changes the value.\n"
"    activated : int, str\n"
"        Emitted when the user chooses an item in the combobox.\n"
"    currentIndexChanged : int, str\n"
"        Emitted when the index is changed in the combobox.\n"
"    highlighted : int, str\n"
"        Emitted when an item in the combobox popup list is highlighted\n"
"        by the user.\n"
"    "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Ui_MainWindow_Ocean", "Spectrometer settings: Sensor"))
        self.PyDMPushButton_stop.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton_stop.setText(_translate("Ui_MainWindow_Ocean", "Pause"))
        self.label_28.setText(_translate("Ui_MainWindow_Ocean", "Ratio (μm/GPa)"))
        self.checkBox_degrees.setText(_translate("Ui_MainWindow_Ocean", "Δ μm"))
        self.checkBox_Gpa.setText(_translate("Ui_MainWindow_Ocean", "GPa"))
        self.PyDMDrawingLine_4.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.label_26.setText(_translate("Ui_MainWindow_Ocean", "Manual pressure adjustment"))
        self.label_24.setText(_translate("Ui_MainWindow_Ocean", "Automatic pressure adjustment"))
        self.label_27.setText(_translate("Ui_MainWindow_Ocean", "Speed (rev/s)"))
        self.PyDMDrawingCircle.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton_move.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton_move.setText(_translate("Ui_MainWindow_Ocean", "Move"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Ui_MainWindow_Ocean", "Motor settings: Actuator"))
        self.label_32.setText(_translate("Ui_MainWindow_Ocean", "Calculate theoretical peak position, pressure and temperature"))
        self.PyDMLabel_19.setText(_translate("Ui_MainWindow_Ocean", "GPa"))
        self.PyDMLabel_14.setText(_translate("Ui_MainWindow_Ocean", "a.u."))
        self.PyDMLabel_30.setText(_translate("Ui_MainWindow_Ocean", "Unit"))
        self.LineEdit_1Count.setText(_translate("Ui_MainWindow_Ocean", "a.u."))
        self.LineEdit_2Count.setText(_translate("Ui_MainWindow_Ocean", "a.u."))
        self.LineEdit_2GPa.setText(_translate("Ui_MainWindow_Ocean", "0"))
        self.LineEdit_1nm.setText(_translate("Ui_MainWindow_Ocean", "692.80"))
        self.LineEdit_2nm.setText(_translate("Ui_MainWindow_Ocean", "694.26"))
        self.PyDMLabel_13.setText(_translate("Ui_MainWindow_Ocean", "nm"))
        self.PyDMLabel_20.setText(_translate("Ui_MainWindow_Ocean", "Pressure"))
        self.PyDMLabel.setText(_translate("Ui_MainWindow_Ocean", "Wavelength"))
        self.LineEdit_1GPa.setText(_translate("Ui_MainWindow_Ocean", "0"))
        self.PyDMLabel_32.setText(_translate("Ui_MainWindow_Ocean", "Intensity"))
        self.PyDMLabel_6.setText(_translate("Ui_MainWindow_Ocean", "1st-peak"))
        self.PyDMDrawingLine.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMLabel_7.setText(_translate("Ui_MainWindow_Ocean", "2nd-peak"))
        self.PyDMPushButton_PressureCalc.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton_PressureCalc.setText(_translate("Ui_MainWindow_Ocean", "p"))
        self.PyDMPushButton_PositionCalc.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton_PositionCalc.setText(_translate("Ui_MainWindow_Ocean", "λ"))
        self.PyDMPushButton_tempCalc.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton_tempCalc.setText(_translate("Ui_MainWindow_Ocean", "T"))
        self.PyDMLabel_3.setText(_translate("Ui_MainWindow_Ocean", "1st-peak"))
        self.PyDMLabel_1nm_result.setText(_translate("Ui_MainWindow_Ocean", "692.80 nm"))
        self.PyDMLabel_1Gpa_result.setText(_translate("Ui_MainWindow_Ocean", "0 GPa"))
        self.PyDMLabel_2Gpa_result.setText(_translate("Ui_MainWindow_Ocean", "0 GPa"))
        self.PyDMLabel_2nm_result.setText(_translate("Ui_MainWindow_Ocean", "694.26 nm"))
        self.Checkbox2pPltPosition.setText(_translate("Ui_MainWindow_Ocean", "2nd"))
        self.PyDMLabel_5.setText(_translate("Ui_MainWindow_Ocean", "2nd-peak"))
        self.label_19.setText(_translate("Ui_MainWindow_Ocean", "Plot-line"))
        self.PyDMLabel_temp_result.setText(_translate("Ui_MainWindow_Ocean", "100 K"))
        self.PyDMDrawingLine_5.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMDrawingLine_7.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMLabel_tempCalc.setText(_translate("Ui_MainWindow_Ocean", "Temperature value for pressure and wavelength calculation:"))
        self.LineEdit_tempBase.setText(_translate("Ui_MainWindow_Ocean", "300"))
        self.PyDMLabel_tempUnit.setText(_translate("Ui_MainWindow_Ocean", "K"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Ui_MainWindow_Ocean", "Calculator worksheet"))
        self.PyDMDrawingLine_2.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.label_23.setText(_translate("Ui_MainWindow_Ocean", "K"))
        self.PyDMLabel_9.setText(_translate("Ui_MainWindow_Ocean", "2nd peak"))
        self.LineEdit_tempBase_2.setText(_translate("Ui_MainWindow_Ocean", "300"))
        self.LineEdit_1nm_2.setText(_translate("Ui_MainWindow_Ocean", "692.80"))
        self.PyDMLabel_31.setText(_translate("Ui_MainWindow_Ocean", "Unit"))
        self.PyDMLabel_33.setText(_translate("Ui_MainWindow_Ocean", "Unit"))
        self.PyDMLabel_10.setText(_translate("Ui_MainWindow_Ocean", "nm"))
        self.PyDMLabel_2.setText(_translate("Ui_MainWindow_Ocean", "Position "))
        self.PyDMLabel_4.setText(_translate("Ui_MainWindow_Ocean", "Temperature"))
        self.LineEdit_2nm_2.setText(_translate("Ui_MainWindow_Ocean", "694.06"))
        self.PyDMLabel_11.setText(_translate("Ui_MainWindow_Ocean", "1st peak"))
        self.label_30.setText(_translate("Ui_MainWindow_Ocean", "In DAC"))
        self.PyDMDrawingLine_3.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.label_20.setText(_translate("Ui_MainWindow_Ocean", "From real time reading"))
        self.PyDMPushButton.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton.setText(_translate("Ui_MainWindow_Ocean", "Set new standard values"))
        self.label_21.setText(_translate("Ui_MainWindow_Ocean", "Standard values at 0 Gpa"))
        self.label_22.setText(_translate("Ui_MainWindow_Ocean", " 300K - 692.80 nm - 692.26 nm"))
        self.PyDMPushButton_setSV.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMPushButton_setSV.setText(_translate("Ui_MainWindow_Ocean", "Set standard values"))
        self.PyDMLabel_tempCalc_3.setText(_translate("Ui_MainWindow_Ocean", "Standard values for zero pressure "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Ui_MainWindow_Ocean", "Standard values"))
        self.label_13.setText(_translate("Ui_MainWindow_Ocean", "UpperLimit (nm)"))
        self.label_16.setText(_translate("Ui_MainWindow_Ocean", "Region 5"))
        self.label_15.setText(_translate("Ui_MainWindow_Ocean", "Region 4"))
        self.label_11.setText(_translate("Ui_MainWindow_Ocean", "Region 2"))
        self.label_17.setText(_translate("Ui_MainWindow_Ocean", "Luminescence"))
        self.label_12.setText(_translate("Ui_MainWindow_Ocean", "LowerLimit (nm)"))
        self.label_14.setText(_translate("Ui_MainWindow_Ocean", "Region 3"))
        self.label_9.setText(_translate("Ui_MainWindow_Ocean", "Region of Interest"))
        self.label_10.setText(_translate("Ui_MainWindow_Ocean", "Region 1"))
        self.label_18.setText(_translate("Ui_MainWindow_Ocean", "Full Spectrum"))
        self.label_31.setText(_translate("Ui_MainWindow_Ocean", "Spectrum analysis: Range of wavelength and luminescence"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Ui_MainWindow_Ocean", "Regions"))
        self.PyDMDrawingLine_9.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.label_7.setText(_translate("Ui_MainWindow_Ocean", "Filename"))
        self.label.setText(_translate("Ui_MainWindow_Ocean", "Path"))
        self.btnPath.setText(_translate("Ui_MainWindow_Ocean", "Select"))
        self.label_8.setText(_translate("Ui_MainWindow_Ocean", "Index"))
        self.lblFileName.setText(_translate("Ui_MainWindow_Ocean", "lab6_3p20GPa_300K"))
        self.sufix.setText(_translate("Ui_MainWindow_Ocean", "_n000.txt"))
        self.lblPath.setText(_translate("Ui_MainWindow_Ocean", "/home/ABTLUS/xafs/Documents/2019"))
        self.btnAcqSave.setText(_translate("Ui_MainWindow_Ocean", "Save"))
        self.PyDMDrawingLine_10.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.label_29.setText(_translate("Ui_MainWindow_Ocean", "Saving intensity versus wavelength in real-time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Ui_MainWindow_Ocean", "Save"))
        self.msg_error.setText(_translate("Ui_MainWindow_Ocean", "Message "))
        self.PyDMLabel_GPa.setText(_translate("Ui_MainWindow_Ocean", "GPa"))
        self.centersOfLoren.setText(_translate("Ui_MainWindow_Ocean", "1st & 2nd peaks (nm):"))
        self.label_centerswaves.setText(_translate("Ui_MainWindow_Ocean", "_ _ _ _ _ _ _ _ _ _ "))
        self.label_25.setText(_translate("Ui_MainWindow_Ocean", "Rubi (K):"))
        self.lblTemp_rubi.setText(_translate("Ui_MainWindow_Ocean", "100 "))
        self.label_35.setText(_translate("Ui_MainWindow_Ocean", "Finger (K):"))
        self.PyDMDrawingLine_6.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.PyDMDrawingLine_8.setWhatsThis(_translate("Ui_MainWindow_Ocean", "\n"
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
        self.actionClose.setText(_translate("Ui_MainWindow_Ocean", "Close"))
        self.actionOpen_2.setText(_translate("Ui_MainWindow_Ocean", "Open"))

from pydm.widgets.checkbox import PyDMCheckbox
from pydm.widgets.drawing import PyDMDrawingCircle, PyDMDrawingLine
from pydm.widgets.enum_combo_box import PyDMEnumComboBox
from pydm.widgets.label import PyDMLabel
from pydm.widgets.line_edit import PyDMLineEdit
from pydm.widgets.pushbutton import PyDMPushButton
from pydm.widgets.waveformplot import PyDMWaveformPlot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow_Ocean = QtWidgets.QMainWindow()
    ui = Ui_Ui_MainWindow_Ocean()
    ui.setupUi(Ui_MainWindow_Ocean)
    Ui_MainWindow_Ocean.show()
    sys.exit(app.exec_())

