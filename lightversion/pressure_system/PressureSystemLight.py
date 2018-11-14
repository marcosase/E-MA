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
        (2) --- (2) --- (2): Signals linked to data processing to determine pressure, position and temperature
        '''
        self.signalsCalc() #Signals linked to data processing to determine pressure, position and temperature
        
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
    
    
    '''
    (2) --- (2) --- (2): Signals linked to data processing to determine pressure, position and temperature
    '''  
        
        
    def signalsCalc(self):
        ''' Determination of pressure data regardless of graph'''
        self.data = DataCalculate()
        
        ''' Initial setup '''
        self.ui.PyDMPushButton_setSV.clicked.connect(self.standard)
        
        ''' Temp ''' 
        self.temp = '300'
        self.ui.LineEdit_tempBase.editingFinished.connect(self.temperatureBase)
        
        ''' Presssure - Position - Temperature '''
        self.ui.PyDMPushButton_tempCalc.clicked.connect(self.temperature)
        
        self.ui.PyDMPushButton_PositionCalc.clicked.connect(self.position)
        
        self.ui.PyDMPushButton_PressureCalc.clicked.connect(self.pressure)
        
        self.ui.PyDMPushButton.clicked.connect(self.getDataFromRealTime)
        
        ''' Plotting line on graph '''
        self.ui.Checkbox2pPltPosition.clicked.connect(self.plotRealTimeLineDesired)
        
    
            
    def standard(self):
        '''Standard values / initial condition '''
        temp0 = self.ui.LineEdit_tempBase_2.text() #In the same widget of others values of position and pressure
        position10 = self.ui.LineEdit_1nm_2.text()
        position20 = self.ui.LineEdit_2nm_2.text()
        self.data.standard(tempzero = temp0, peak1zero = position10, peak2zero = position20)
        self.graphdata.standard(tempzero = temp0, peak1zero = position10, peak2zero = position20)
    
    def temperatureBase(self):
        ''' Temperature: Base of calculation according to sensor on OceanSpectrometer'''
        try:
            #temp_int = float(self.ui.LineEdit_tempBase.text())  
            self.temp = self.ui.LineEdit_tempBase.text()
            #self.getTemp4auto() # With lakeshore this line should commented
            self.pressure()
            self.position()
        except OSError as err:
            self.showDialog("Temperature value is not valid",err)
    
        
    def temperature(self):
        self.showDialog( title = 'Range of Temperature', text = 'Temperature determination has range between 10 and 100K using peak intensities')
        count1 = self.ui.LineEdit_1Count.text()
        count2 = self.ui.LineEdit_2Count.text() 
        
        if (self.data.temperatureCalculate(intensity_peak1 = count1, intensity_peak2 = count2)):
            self.ui.PyDMLabel_temp_result.setText(str(self.data.temp)+' K')
        else:     
            self.ui.PyDMLabel_temp_result.setText("Error")
          
    
    def position(self):
        pressure1 = self.ui.LineEdit_1GPa.text()
        pressure2 = self.ui.LineEdit_2GPa.text()
        if (self.data.peakPositionCalculate(temp = self.temp, press1 = pressure1, press2 = pressure2)):
            self.ui.PyDMLabel_1nm_result.setText(str(self.data.peak1) + ' nm')
            self.ui.PyDMLabel_2nm_result.setText(str(self.data.peak2) + ' nm')
            self.dPressure = float(pressure2)
            self.plotCalcPosition(self.data.peak2)
        else:
            self.ui.PyDMLabel_1nm_result.setText('Error')
            self.ui.PyDMLabel_2nm_result.setText('Error')
            self.plotCalcPosition(0)
            
    def plotRealTimeLineDesired(self):
        wave_on_2peak = self.ui.PyDMLabel_2nm_result.text() 
        if (wave_on_2peak  == 'Error'):
            self.plotCalcPosition(wl_ = 0) 
        else:
            idx_name = wave_on_2peak.find('n')
            if idx_name > 0:
                peak2 = wave_on_2peak[0:idx_name-1]
                self.plotCalcPosition(float(peak2))
            else:
                self.plotCalcPosition(0)
        
    
    def plotCalcPosition(self,wl_):
        if (self.ui.Checkbox2pPltPosition.isChecked()):
            self.plotFlagDesired = True
            self.plotLine_nm_OnGraph(w_l = wl_,_label='SetPoint',plot=self.plotFlagDesired, _angle = 90)
        else:
            self.plotFlagDesired = False
            self.plotLine_nm_OnGraph(w_l = wl_,_label='SetPoint',plot = self.plotFlagDesired, _angle = 90)
    
        
    def plotLine_nm_OnGraph(self,plot = True, w_l = 694.26, _label= 'PV', _angle = 90 ):
        try:
            if (plot):
                if ((w_l>600) and (w_l<800)):
                    if self.ui.chkDark.isChecked():
                        self.ui.wvRaw.plotItem.removeItem(self.line_calc)
                        self.ui.wvDark.plotItem.removeItem(self.line_calc)
                        self.line_calc = InfiniteLine(pos=w_l,angle=_angle,pen = mkPen('g',width = 2), label = _label)
                        self.ui.wvDark.plotItem.addItem(self.line_calc)
                    else:
                        self.ui.wvRaw.plotItem.removeItem(self.line_calc)
                        self.ui.wvDark.plotItem.removeItem(self.line_calc)
                        self.line_calc = InfiniteLine(pos=w_l,angle=_angle,pen = mkPen('g',width = 2), label = _label)
                        self.ui.wvRaw.plotItem.addItem(self.line_calc)
                else:
                    self.showDialog("Error plotting procedure","Wavelength is out of range")
            else:
                self.ui.wvRaw.plotItem.removeItem(self.line_calc)
                self.ui.wvDark.plotItem.removeItem(self.line_calc)
            
        except:
            self.showDialog("Error on pressure data processing","Mode Automatic: Error on pressure data plotting")    
                        
    def pressure(self):
        position1 = self.ui.LineEdit_1nm.text()
        position2 = self.ui.LineEdit_2nm.text()
        if (self.data.pressureCalculate(temp = self.temp, peak1 = position1, peak2 = position2)):
            self.ui.PyDMLabel_1Gpa_result.setText(str(self.data.press1) + ' GPa')
            self.ui.PyDMLabel_2Gpa_result.setText(str(self.data.press2) + ' GPa')
        else:
            self.ui.PyDMLabel_1Gpa_result.setText('Error')
            self.ui.PyDMLabel_2Gpa_result.setText('Error')
    
    def getDataFromRealTime(self):
        ''' Set initial values of pressure calculation '''
        try:
            if (self.ui.chkAuto.isChecked()) and (self.wavelength is not None):
                #temp0 = self.ui.LineEdit_tempBase_2.text()
                temp0 = self.ui.LineEdit_tempBase.text()
                position10 = self.wavelength[1]
                position20 = self.wavelength[0]
                dataFlag = self.data.standard(tempzero = temp0, peak1zero = position10, peak2zero = position20)
                datagraphFlag = self.graphdata.standard(tempzero = temp0, peak1zero = position10, peak2zero = position20)
                if dataFlag and datagraphFlag:
                    self.ui.LineEdit_1nm_2.setText(str(position10))
                    self.ui.LineEdit_2nm_2.setText(str(position20))
                    self.ui.LineEdit_tempBase_2.text(temp0)
                else:
                    self.showDialog('Fatal Error on initial value settings','Fatal Error on initial value settings')
            else:
                self.showDialog("Error: wavelength is None or search peaks is not checked",'Error: wavelength is None or search peaks is not checked')
        except OSError as err:
            self.showDialog("Error: Initial value settings",err)

    
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
     