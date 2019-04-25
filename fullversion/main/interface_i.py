# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_i.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 454)
        MainWindow.setMinimumSize(QtCore.QSize(300, 454))
        MainWindow.setMaximumSize(QtCore.QSize(300, 454))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.1 rgba(65, 65, 65, 255), stop:0.1 rgba(65, 65, 65, 255));\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setMinimumSize(QtCore.QSize(24, 18))
        self.toolButton.setMaximumSize(QtCore.QSize(24, 18))
        self.toolButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100);")
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.PyDMPushButton_ligthsystem = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_ligthsystem.setToolTip("")
        self.PyDMPushButton_ligthsystem.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_ligthsystem.setObjectName("PyDMPushButton_ligthsystem")
        self.gridLayout.addWidget(self.PyDMPushButton_ligthsystem, 6, 1, 1, 1)
        self.PyDMImageView_inicial = PyDMImageView(self.centralwidget)
        self.PyDMImageView_inicial.setToolTip("")
        self.PyDMImageView_inicial.setProperty("alarmSensitiveBorder", False)
        self.PyDMImageView_inicial.setProperty("colorMap", PyDMImageView.Monochrome)
        self.PyDMImageView_inicial.setObjectName("PyDMImageView_inicial")
        self.gridLayout.addWidget(self.PyDMImageView_inicial, 2, 0, 1, 2)
        self.PyDMCheckbox_singlecrystal = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_singlecrystal.setToolTip("")
        self.PyDMCheckbox_singlecrystal.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMCheckbox_singlecrystal.setChecked(True)
        self.PyDMCheckbox_singlecrystal.setObjectName("PyDMCheckbox_singlecrystal")
        self.gridLayout.addWidget(self.PyDMCheckbox_singlecrystal, 8, 0, 1, 1)
        self.PyDMPushButton_singlecrystal = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_singlecrystal.setToolTip("")
        self.PyDMPushButton_singlecrystal.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_singlecrystal.setObjectName("PyDMPushButton_singlecrystal")
        self.gridLayout.addWidget(self.PyDMPushButton_singlecrystal, 8, 1, 1, 1)
        self.PyDMCheckbox_lightsource = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_lightsource.setToolTip("")
        self.PyDMCheckbox_lightsource.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMCheckbox_lightsource.setObjectName("PyDMCheckbox_lightsource")
        self.gridLayout.addWidget(self.PyDMCheckbox_lightsource, 6, 0, 1, 1)
        self.PyDMCheckbox_temperature = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_temperature.setToolTip("")
        self.PyDMCheckbox_temperature.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMCheckbox_temperature.setObjectName("PyDMCheckbox_temperature")
        self.gridLayout.addWidget(self.PyDMCheckbox_temperature, 9, 0, 1, 1)
        self.PyDMPushButton_temperaturesystem = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_temperaturesystem.setToolTip("")
        self.PyDMPushButton_temperaturesystem.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_temperaturesystem.setObjectName("PyDMPushButton_temperaturesystem")
        self.gridLayout.addWidget(self.PyDMPushButton_temperaturesystem, 9, 1, 1, 1)
        self.PyDMCheckbox_pressure = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_pressure.setToolTip("")
        self.PyDMCheckbox_pressure.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMCheckbox_pressure.setChecked(True)
        self.PyDMCheckbox_pressure.setObjectName("PyDMCheckbox_pressure")
        self.gridLayout.addWidget(self.PyDMCheckbox_pressure, 7, 0, 1, 1)
        self.PyDMPushButton_pressuresystem = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_pressuresystem.setToolTip("")
        self.PyDMPushButton_pressuresystem.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_pressuresystem.setObjectName("PyDMPushButton_pressuresystem")
        self.gridLayout.addWidget(self.PyDMPushButton_pressuresystem, 7, 1, 1, 1)
        self.PyDMCheckbox_visionsystem = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_visionsystem.setToolTip("")
        self.PyDMCheckbox_visionsystem.setStyleSheet("color: rgb(240, 240, 240);")
        self.PyDMCheckbox_visionsystem.setChecked(True)
        self.PyDMCheckbox_visionsystem.setObjectName("PyDMCheckbox_visionsystem")
        self.gridLayout.addWidget(self.PyDMCheckbox_visionsystem, 5, 0, 1, 1)
        self.PyDMPushButton_visionsystem = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_visionsystem.setEnabled(True)
        self.PyDMPushButton_visionsystem.setToolTip("")
        self.PyDMPushButton_visionsystem.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_visionsystem.setObjectName("PyDMPushButton_visionsystem")
        self.gridLayout.addWidget(self.PyDMPushButton_visionsystem, 5, 1, 1, 1)
        self.PyDMPushButton_beamsystem = PyDMPushButton(self.centralwidget)
        self.PyDMPushButton_beamsystem.setToolTip("")
        self.PyDMPushButton_beamsystem.setStyleSheet("color: rgb(255, 255, 255);")
        self.PyDMPushButton_beamsystem.setObjectName("PyDMPushButton_beamsystem")
        self.gridLayout.addWidget(self.PyDMPushButton_beamsystem, 4, 1, 1, 1)
        self.PyDMCheckbox_beamalignment = PyDMCheckbox(self.centralwidget)
        self.PyDMCheckbox_beamalignment.setToolTip("")
        self.PyDMCheckbox_beamalignment.setStyleSheet("color: rgb(240, 240, 240);\n"
"")
        self.PyDMCheckbox_beamalignment.setObjectName("PyDMCheckbox_beamalignment")
        self.gridLayout.addWidget(self.PyDMCheckbox_beamalignment, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(240, 240, 240);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.PyDMPushButton_pressuresystem.raise_()
        self.PyDMPushButton_visionsystem.raise_()
        self.PyDMPushButton_beamsystem.raise_()
        self.PyDMPushButton_ligthsystem.raise_()
        self.PyDMImageView_inicial.raise_()
        self.PyDMPushButton_singlecrystal.raise_()
        self.PyDMPushButton_temperaturesystem.raise_()
        self.PyDMCheckbox_beamalignment.raise_()
        self.PyDMCheckbox_lightsource.raise_()
        self.PyDMCheckbox_pressure.raise_()
        self.PyDMCheckbox_singlecrystal.raise_()
        self.PyDMCheckbox_temperature.raise_()
        self.PyDMCheckbox_visionsystem.raise_()
        self.toolButton.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("color: rgb(208, 208, 208);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E-MA © 2018 EMA "))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.PyDMPushButton_ligthsystem.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMPushButton_ligthsystem.setText(_translate("MainWindow", "Open"))
        self.PyDMImageView_inicial.setWhatsThis(_translate("MainWindow", "\n"
"    A PyQtGraph ImageView with support for Channels and more from PyDM\n"
"\n"
"    Parameters\n"
"    ----------\n"
"    parent : QWidget\n"
"        The parent widget for the Label\n"
"    image_channel : str, optional\n"
"        The channel to be used by the widget for the image data.\n"
"    width_channel : str, optional\n"
"        The channel to be used by the widget to receive the image width\n"
"        information\n"
"    "))
        self.PyDMCheckbox_singlecrystal.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMCheckbox_singlecrystal.setText(_translate("MainWindow", "Single Crystal System"))
        self.PyDMPushButton_singlecrystal.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMPushButton_singlecrystal.setText(_translate("MainWindow", "Open"))
        self.PyDMCheckbox_lightsource.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMCheckbox_lightsource.setText(_translate("MainWindow", "Light Source System"))
        self.PyDMCheckbox_temperature.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMCheckbox_temperature.setText(_translate("MainWindow", "Temperature System"))
        self.PyDMPushButton_temperaturesystem.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMPushButton_temperaturesystem.setText(_translate("MainWindow", "Open"))
        self.PyDMCheckbox_pressure.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMCheckbox_pressure.setText(_translate("MainWindow", "Pressure System"))
        self.PyDMPushButton_pressuresystem.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMPushButton_pressuresystem.setText(_translate("MainWindow", "Open"))
        self.PyDMCheckbox_visionsystem.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMCheckbox_visionsystem.setText(_translate("MainWindow", "Diffraction Imaging System"))
        self.PyDMPushButton_visionsystem.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMPushButton_visionsystem.setText(_translate("MainWindow", "Open"))
        self.PyDMPushButton_beamsystem.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMPushButton_beamsystem.setText(_translate("MainWindow", "Open"))
        self.PyDMCheckbox_beamalignment.setWhatsThis(_translate("MainWindow", "\n"
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
        self.PyDMCheckbox_beamalignment.setText(_translate("MainWindow", "Beam Alignment System"))
        self.label.setText(_translate("MainWindow", "Experiment Management App"))

from pydm.widgets.checkbox import PyDMCheckbox
from pydm.widgets.image import PyDMImageView
from pydm.widgets.pushbutton import PyDMPushButton

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

