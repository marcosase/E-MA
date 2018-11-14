'''
Created on Jun 28, 2018

@author: root
10.0.4.141

'''
from PyQt5 import QtWidgets,QtGui,QtCore
from pressure_system.interface_oceanoptics_10 import Ui_Ui_MainWindow_Ocean
from pydm import PyDMApplication
from PyQt5.QtCore import QRegExp,pyqtSlot
from PyQt5.QtGui import QRegExpValidator
from os import path
from PyQt5.QtWidgets import QMessageBox
from pressure_system.pressure_system_sensor.SensorOcean import SensorOcean
from pressure_system.pressure_system_sensor.DataCalculate import DataCalculate
from pressure_system.pressure_system_sensor.CurveDetection import indexes,lorentzianFunctionGenerator
from pyqtgraph.functions import mkPen
from pyqtgraph import InfiniteLine
from pressure_system.pressure_system_motor.Nema23 import Nema23
import time

class PressureSystem(object):
    '''
    Pressure System is a class that contains the following classes:
        SensorOcean acquires spectrogram from OceanOpticsSpectrometer
        and calculates the two most important peaks to calculate pressure
        
        Nema23 represents a stepper motor that has a gearbox connected 
        in order to make pressure on DAC
        
        DataCalculate processing data class.    
    '''
    def __init__(self):
        '''
        Constructor: Ocean Optics window -> It is command and supervisory window 
        '''
        self.ui = Ui_Ui_MainWindow_Ocean()

    def setupUi(self,object = None):
        '''
        Setup of widgets
        '''
        self.ui.setupUi(object)
    
    def setFlowControl(self, oceanPV = "SOL3", motorPV = "SOL:galil:test:A", LS = "XDS:LS"):
        '''
        Functions that determine the flow control of app
        '''
        '''
        (0) --- (0) --- (0): Names of PV - EPICS - Protocol
        '''
        self.setPVnames(oceanPV, motorPV, LS)
        '''
        (1) --- (1) --- (1): User interface based on PyDM channels
        '''
        self.setGuiAnd2flow() #User interface based on PyDM channels
        
        
    '''
    (1) --- (1) --- (1): User interface based on PyDM channels
    '''
    
    def setPVnames(self, oceanPV = "SOL3", motorPV = "SOL:galil:test:A", LS = "XDS:LS"):
        self.oceanPVname = oceanPV
        self.motorPVname = motorPV
        self.lakashorePVname = LS
        
    def setGuiAnd2flow(self):
        #PV Name 
        ''' PVname was defined #self.oceanPVname = "SOL3"''' 
        #Setup user interface
        self._guiSetup(self.oceanPVname)
        
    def _guiSetup(self, pvname):
        # load pv name
        MAXROIS = 6
        urlname = 'ca://'+ pvname
       
        # validation
        regExFloat = QRegExp("[0-9]+(\.[0-9]+)?")
        validFloat = QRegExpValidator(regExFloat)
        #self.ui.edtIntegration.setValidator(validFloat) #It was changed in order to make interface standard
        self.ui.leLower1.setValidator(validFloat)
        self.ui.leLower2.setValidator(validFloat)
        self.ui.leLower3.setValidator(validFloat)
        self.ui.leLower4.setValidator(validFloat)
        self.ui.leLower5.setValidator(validFloat)
        self.ui.leUpper1.setValidator(validFloat)
        self.ui.leUpper2.setValidator(validFloat)
        self.ui.leUpper3.setValidator(validFloat)
        self.ui.leUpper4.setValidator(validFloat)
        self.ui.leUpper5.setValidator(validFloat)
        
        
        # set channel values
        self.ui.wvRaw.curves = ['{"y_channel": "'+ urlname + ':Spectra", \
            "x_channel": "'+ urlname + ':SpectraAxis", "name": \
            "Raw Spectrum", "color": "black"}']
        self.ui.wvDark.curves = ['{"y_channel": "'+ urlname + \
            ':DarkCorrectedSpectra", "x_channel": "'+ urlname + \
            ':SpectraAxis", "name": "Dark Corrected Spectrum", \
            "color": "black"}']
       
        ''' When we have LakeShore '''
        self.ui.lblTemp.channel = 'ca://' + self.lakashorePVname + ':TEMPKGETA' #urlname + ':DetectorTemp'  
        self.ui.lblProgress.channel= urlname + ':ProgressBar'
        self.ui.lblAcquiring.channel = urlname + ':Acquiring'
        self.ui.edtIntegration.channel = urlname + ':IntegrationTime:Value'
        self.ui.cmbAcquisition.channel = urlname + ':AcquisitionMode'
        self.ui.chkDark.channel = urlname + ':ElectricalDark'
        self.ui.chkTrigger.channel = urlname + ':ExternalTrigger'
        self.ui.btnAcquire.channel = urlname + ':Acquire'
        
        for i in range(1, MAXROIS):
            lower = getattr(self.ui, 'leLower'+str(i))
            upper = getattr(self.ui, 'leUpper'+str(i))
            lumi = getattr(self.ui, 'lblLuminescence'+str(i))

            lower.channel = urlname +":Region" + str(i) + ":LowerLimit"
            upper.channel = urlname +":Region" + str(i) + ":UpperLimit"
            lumi.channel = urlname +":Region" + str(i) + ":Luminescence"

        self.ui.lblLuminescenceTotal.channel = urlname + ":TotalLuminescence"
    
    
    

    
    def showDialog(self,title = None, text = None):
        """Show a simple message dialog"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()  
    
if __name__ == "__main__":  
    import sys
    app = PyDMApplication(use_main_window=False)
    Ui_MainWindow_Ocean = QtWidgets.QMainWindow()
    ui = PressureSystem()
    ui.setupUi(Ui_MainWindow_Ocean)
    ui.setFlowControl(oceanPV = "SOL3", motorPV = "SOL:galil:test:A", LS = "XDS:LS")
    Ui_MainWindow_Ocean.show()
    app.establish_widget_connections(widget = Ui_MainWindow_Ocean)
    sys.exit(app.exec_())    
     