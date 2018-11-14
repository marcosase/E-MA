'''
Created on Jun 28, 2018

@author: root
10.0.4.141

'''
from PyQt5 import QtWidgets,QtGui,QtCore
from pressure_system.interface_oceanoptics_5 import Ui_Ui_MainWindow_Ocean
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
import os
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
        (3) --- (3) --- (3): Management of interfaces on right of major interface 
        '''
        #self.signalsStackedWidget() #Management of interfaces on right of major interface
        '''
        (4) --- (4) --- (4): Interface of motor to be displayed if clicked
        '''
        #self.motorinterface() #Interface of motor to be displayed if clicked
        self.setFlowControl_motor()
        '''
        (5) --- (5) --- (5): Save data on .txt!
        '''
        self.save_data_on_txt()
        
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
        self.set2ndFlowGui()
    
    def set2ndFlowGui(self):
        #Create Ocean object: Operation and communication in parallel flow control 
        self.SensorOcean_func(self.oceanPVname)
        
        #Instance: Determination of pressure data with data of graph'''
        self.graphdata = DataCalculate()
        
        # connect signals of SensorOcean -> PV of OceanOptics
        self.SensorOcean.signal.connect(self.searchPressure)
        #self.SensorOcean.finished.connect(self.finish)
        self.SensorOcean.error_message.connect(self.errorMessage) 
        
        #Connect the most important signal (Acquire spectrogram)
        self.ui.btnAcquire.released.connect(self.managerUserInterfaceforacquisition)
        
    
        #It does not break the program
        self.line = InfiniteLine()
        self.line_calc = InfiniteLine()
        self.ui.lcdPressure.setSmallDecimalPoint(True)
        self.ui.lcdPressure.setDigitCount(6)
        self.plotFlagDesired = None
        self.dPressure = None
        
        
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
        #self.ui.edtIntegration.channel = urlname + ':IntegrationTime:Value'
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
        
        
    def SensorOcean_func(self,pvname):
        ''' 
        This is a class related to OceanSpectrometer class 
        In order to have a multiple run, it was necessary to work with hardware interruptions. 
        For this reason, multiple runs without sum of spectrogram
        ''' 
        self.SensorOcean = SensorOcean(pvname)
    
    def managerUserInterfaceforacquisition(self):
        ''' user interface flow control '''
        try:
            #btn_str = self.ui.btnAcquire.text() #Get text of start button
            btn_int = self.SensorOcean.ocean.pvStart.get() #We changed btn_st per btn_int
        
            if(btn_int == 0): #Acquiring is not happening
                cmd_str = self.SensorOcean.ocean.pvAcMode.get()
                if (cmd_str == 0): 
                    self.searchPeaks_single()
                elif (cmd_str == 1):
                    self.ui.btnAcquire.setText('Stop')
                    self.searchPeaks_continuous()
                    self.ui.cmbAcquisition.setEnabled(False)
                    self.ui.edtIntegration.setEnabled(False)
                self.SensorOcean.editIntegrationTime(timeValue = self.ui.edtIntegration.value())
            elif(btn_int == 1): #Acquiring is happening
                self.ui.btnAcquire.setText('Start') #Initial mode
                self.SensorOcean.ocean.pvAcMode.put("Single")
                self.searchPeaks_single()
                self.ui.cmbAcquisition.setEnabled(True)
                self.ui.edtIntegration.setEnabled(True)

        except OSError as err:
            self.showDialog("Manager User Interface for acquisition",err)
    
        
    def searchPeaks_single(self):
        if (not(self.ui.chkAuto.isChecked())): # But, it does not want to search peak automatically
                self.plotAutomaticLineOnGraph(plot=False) #Stop plotting
                
        
    def searchPeaks_continuous(self):
        if (not(self.ui.chkAuto.isChecked())): # But, it does not want to search peak automatically
                self.plotAutomaticLineOnGraph(plot=False) #Stop plotting
    
    '''
    (1) --- (1) --- (1):  SensorOcean -> PV of OceanOptics -> Callback
    '''

    def searchPressure(self,wl):
        '''
        Callback of OceanSpectrometer: Every time that there is a new data, this function will work
        '''
        if(self.pressureGraphDataCalculation(wl)): #If wavelength makes sense
            if (self.ui.chkAuto.isChecked()): #The user wants to search peaks automatically
                if self.SensorOcean.ocean.pvAcMode.get() == 1: #Real time is happening
                    self.setRealPressure(flag=True, gpa_real= self.graphdata.press2)#Motion! Go!
                else:
                    self.setRealPressure(flag=False, gpa_real= 0) #Pause. It is not safe to start 
                self.plotAutomaticLineOnGraph(plot=True, w_l=wl[0] ,_label='process variable') #Plot
                self.wavelength = wl #Save wavelength in order to set pressure in standard condition
                #print('Waves (nm):',wl)
            else:
                self.setRealPressure(flag=False, gpa_real= 0) #Pause
                self.plotAutomaticLineOnGraph(plot=False)
        else:
            self.setRealPressure(flag=False, gpa_real= 0) #Pause motor 
            self.ui.lcdPressure.display('--') 
            self.plotAutomaticLineOnGraph(plot=False) #Stop plotting

    
    def pressureGraphDataCalculation(self,wl):
        ''' 1st peak is the leftmost peak. 2nd peak is the rightmost '''
        ''' wl[0] is the wavelength with biggest value of intensity. wl[0] is rightmost -> 2nd peak'''
        ''' wl[1] is leftmost -> 1st peak'''
        try:
            #print('GetTemp4auto', self.getTemp4auto())
            if wl is not None: #wl[0] is not -1
                if len(wl) == 2:
                    if (self.graphdata.pressureCalculate(temp = self.getTemp4auto(), peak1 = wl[1], peak2 = wl[0])):
                        self.displayONlcd(self.graphdata.press2) #self.ui.lcdPressure.display(self.graphdata.press2) 
                        return True 
                    else:
                        return False
                elif (len(wl) == 1) and (wl[0] == -1):
                    return False
                else:
                    return False 
            else:
                return False
        except OSError as err:
            self.showDialog("Error on pressure GraphData Calculation",err)
            return False
    
    def getTemp4auto(self):
        ''' Data from OceanSpectrometer '''
        try:
            ''' When we have LakeShore '''
            temp = self.ui.lblTemp.text() #LakeSHore
            #temp = self.temp # with no lakeshore
            #self.ui.lblTemp.setText(self.temp) #with no LakeShore
            t = float(temp)
            #print('Temperature: ',t)
            if t > 0.01:
                return t
            else:
                self.ui.lblTemp.setText('--')
                return 300
        except OSError as err:
            self.showDialog("Temperature value is not valid",err)
            return None

    
    def displayONlcd(self,data):
        ''' Display Pressure on LCD '''
            
        if(self.plotFlagDesired and (self.dPressure is not None)):
            if (self.checkNiceRange(gpa_desired = self.dPressure, gpa_real = data)): #old: self.dPressure - data < 0.1) and (data <= self.dPressure
                self.ui.lcdPressure.setStyleSheet("background-color: rgb(65, 65, 65);\n"
                                           "color: rgb(0, 255, 0);")
                self.ui.lcdPressure.display(data)
            else:
                self.ui.lcdPressure.setStyleSheet("background-color: rgb(65, 65, 65);\n"
                                           "color: rgb(255, 0, 0);")
                self.ui.lcdPressure.display(data)
        else:
            self.ui.lcdPressure.display(data)
    
         
    def plotAutomaticLineOnGraph(self,plot=True, w_l = 694.26, _label= 'PV'):
        ''' Plotting line on graph '''
        try:
            if (plot):
                if self.ui.chkDark.isChecked():
                    self.ui.wvRaw.plotItem.removeItem(self.line)
                    self.ui.wvDark.plotItem.removeItem(self.line)
                    self.line = InfiniteLine(pos=w_l,angle=90,pen = mkPen('r',width = 2), label = _label)
                    self.ui.wvDark.plotItem.addItem(self.line)
                else:
                    self.ui.wvRaw.plotItem.removeItem(self.line)
                    self.ui.wvDark.plotItem.removeItem(self.line)
                    self.line = InfiniteLine(pos=w_l,angle=90,pen = mkPen('r',width = 2), label = _label)
                    self.ui.wvRaw.plotItem.addItem(self.line)
            else:
                self.ui.wvRaw.plotItem.removeItem(self.line)
                self.ui.wvDark.plotItem.removeItem(self.line)
        except:
            self.showDialog("Error on pressure data processing","Mode Automatic: Error on pressure data plotting")
    
                
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

    
    '''
    (3) --- (3) --- (3): Management of interfaces on the left and on the right of major interface
    '''
        
    '''
    (4) --- (4) --- (4): Interface of motor to be displayed if clicked
    '''
    def setFlowControl_motor(self):
        self.ui.PyDMPushButton_move.clicked.connect(self.moveMotor)
        '''self.ui.PyDMPushButton_restart.clicked.connect(self.restartMotor)'''
        self.ui.PyDMPushButton_stop.clicked.connect(self.pauseMotor)
        
        self.moveFlag = True
        self.automoveFlag = False
        self.pauseUser = False
        
        
        self.machine = Nema23(pvname = self.motorPVname,mne_=str(int(time.time())))
        self.machine.pause()
        self.machine.motion.connect(self.motion_end)
       
        
        
    def motion_end(self):
        self.ui.msg_error.setText('Pressure motion was completed!')

    def moveMotor(self):
        self.pauseUser = False
        if self.getparams():
            if self.machine.isRunning():
                self.ui.msg_error.setText('Error: Motor is running. You should pause motor!')
            else:
                if self.automoveFlag:
                    self.ui.msg_error.setText('Verify if spectrometer and pressure detection are enable!')
                else:
                    self.startMotor()
        else:
            self.ui.msg_error.setText('User data inputs are wrongs')
            
    def startMotor(self):
        if self.pauseUser:
            self.ui.msg_error.setText("User command 'Pause' detected")
        else:
            if self.machine.settings_motion(desired_rps = self.rps, efficiency_= self.eff, revs_onM4 = self.revs_desired):
                self.machine.start()
                self.moveFlag = True
                self.colourYellowCircle() 
            else:
                self.ui.msg_error.setText("Error: Motor settings on PV ")
    
    def pauseMotor(self):
        self.pauseUser = True
        self.pauseMotor_automatic()
        self.colourWhiteCircle()
    
    def pauseMotor_automatic(self):
        self.machine.pause()
        self.moveFlag = False
    
    def getparams(self):
        try:
            self.rps = self.ui.dSB_s.value()#self.dr = float(self.ui.lineEdit_rps.text())
            self.eff = self.ui.dSB_eff.value()/100#self.ef = float(self.ui.lineEdit_eff.text())
            return self.revsSetup() #Setting number of revolutions 
        except Exception as e:
            print ("Unexpected error -- getparams --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
    
    def revsSetup(self):
        
        if (self.ui.checkBox_degrees.isChecked() and self.ui.checkBox_Gpa.isChecked()):
            self.ui.checkBox_degrees.setChecked(False)
            self.ui.checkBox_Gpa.setChecked(False)
            self.ui.msg_error.setText('Choose only one checkbox')
            self.automoveFlag = False
            return False
        elif self.ui.checkBox_Gpa.isChecked() and not(self.ui.checkBox_degrees.isChecked()):
            ''' Automatic motion to desired pressue'''
            self.gpa_desired = self.ui.dSB_gpa.value()
            self.revs_desired = self.revsEstimationAndGo(self.gpa_desired, 0)
            self.automoveFlag = True
            return True
        elif self.ui.checkBox_degrees.isChecked() and not(self.ui.checkBox_Gpa.isChecked()):
            ''' Manual pressure adjustment ''' 
            self.revs_desired = self.revsEstimationAndGo(self.ui.dSB_graus.value() , 0) 
            self.automoveFlag = False
            return True
        else:
            self.ui.msg_error.setText('Choose one checkbox')
            self.automoveFlag = False
            return False
            
        
    
    def revsEstimationAndGo(self,gpa__desired, gpa__real):
        if (gpa__real >= 0):
            revs = gpa__desired - gpa__real
            return revs
        else:
            self.ui.msg_error.setText('Real pressure is negative :(')
            return 0
    
    def setRealPressure(self,flag = False, gpa_real = 0):
        try:
            if (self.automoveFlag): #Automation motion on motor widget was  selected
                if flag: #Is there real value ?
                    if self.checkNiceRange(self.gpa_desired, gpa_real): #gpa_real == self.gpa_desired: #Is it the desired value ?
                        self.pauseMotor_automatic() #Pause
                        self.colourGreenCircle() #Finished motion! Every thing is ok!
                    else:
                        if not(self.machine.isRunning() and self.moveFlag): #It is the stopped but it is not the desired value!
                            self.revs_desired = self.revsEstimationAndGo(self.gpa_desired, gpa_real) #New estimation 
                            self.startMotor() #Go
                        else:
                            self.colourBlueCircle(gpa_real) #It is running
                else:
                    self.pauseMotor_automatic() #Pause
                    self.moveFlag = True #But, it is possible to continue if another true value exists
                    self.colourGrayCircle()
            else:
                self.ui.msg_error.setText('Automatic motion on motor widget is not selected and clicked')
        except Exception as e:
            print ("Unexpected error -- Create Motor --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
    

    def checkNiceRange(self, gpa_desired, gpa_real):
        ''' See and check if pressure real value is closed to disired value of pressure '''
        
        if gpa_desired >= gpa_real:
            if gpa_desired <= 0:
                gpa_desired = 0.01
            if (gpa_real/gpa_desired >= 0.98):
                return True
            else:  
                return False
        else: # gpa_real >= gpa_desired
            if (gpa_real <= 0):
                gpa_real = 0.01
            if (gpa_desired/gpa_real >= 0.98):
                return True
            else:
                return False
            
    def colourGreenCircle(self):
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.ui.PyDMDrawingCircle.setProperty("brush", brush)
        self.ui.msg_error.setText('Desired pressure reached!\0/') #Automatic system task was done! Do manually
    
    def colourGrayCircle(self):
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.ui.PyDMDrawingCircle.setProperty("brush", brush)
        self.ui.msg_error.setText('Motor system stopped. No signal was found!')
    
    def colourWhiteCircle(self):
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.ui.PyDMDrawingCircle.setProperty("brush", brush)
    
    def colourBlueCircle(self,gpa_real):
        if (gpa_real%0.02 > 0.005):
            brush = QtGui.QBrush(QtGui.QColor(0,0,200))
        else:
            brush = QtGui.QBrush(QtGui.QColor(56, 176, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.ui.PyDMDrawingCircle.setProperty("brush", brush)
        self.ui.msg_error.setText('Motor system running') 
    
    def colourYellowCircle(self):
        brush = QtGui.QBrush(QtGui.QColor(200,200,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.ui.PyDMDrawingCircle.setProperty("brush", brush)
        self.ui.msg_error.setText('Motor system running with new settings')
        
        
    '''
    (5) --- (5) --- (5): Save data on .txt!
    '''
    def save_data_on_txt(self):
        # connect other signals related to multiple acquisition
        self.ui.btnPath.released.connect(self.chooseDir)
        self.ui.btnAcqSave.released.connect(self.acqMult)
        self.ui.sbRuns.valueChanged.connect(self.update_filename)
        
    def showDialog(self,title = None, text = None):
        """Show a simple message dialog"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()  
    
    #@pyqtSlot()
    def chooseDir(self):
        """Open a Choose Directory Dialog and save result on lePath"""
        self.ui.lblPath.setText(
            QtWidgets.QFileDialog.getExistingDirectory(self.ui.btnPath))
    
    
    def getPathHome(self):
        if ' ' in self.pathHome:
            self.showDialog("Invalid Filename", "We hate filenames with special character!")
            return False
        elif(not (os.path.exists(self.pathHome))): 
            self.showDialog("Invalid directory", "Check your directory!")
            return False
        elif not(self.getFileName()):
            return False
        elif ((os.path.isfile(self.pathHome + self.fileName))):
            self.showDialog("Filename already exists", "Check your directory and your filename!")
            return False
        elif (not (self.update_filename())):
            self.showDialog("Filename Failed", "Error: Filename-Update!")
            return False
        else:
            return True
    
    def getFileName(self):
        #self.fileName = self.ui.lblFileName.text()
        if '.txt' not in self.fileName:
            self.showDialog("Invalid Filename", "This filename does not have .txt !")
            return False
        elif ('#' in self.fileName) or ('\\' in self.fileName) or ('/' in self.fileName):
            self.showDialog("Invalid Filename", "We hate filenames with special character!")
            return False
        elif ' ' in self.fileName:
            self.showDialog("Invalid Filename", "We hate filenames with special character!")
            return False
        elif ('(' in self.fileName) or ('{' in self.fileName) or ('[' in self.fileName) or ('´' in self.fileName):
            self.showDialog("Invalid Filename", "We hate filenames with special character!")
            return False
        elif (')' in self.fileName) or ('}' in self.fileName) or (']' in self.fileName) or ('"' in self.fileName):
            self.showDialog("Invalid Filename", "We hate filenames with special character!")
            return False
        else:
            return True
    
    #@pyqtSlot()
    def acqMult(self):
        self.pathHome = self.ui.lblPath.text()
        self.pathHome = self.pathHome + '/'
        self.fileName = self.ui.lblFileName.text() + self.ui.sufix.text()
        if not self.SensorOcean.isReady():
            self.showDialog("Ocean disconnected", "Ocean is disconnected!")
            return
        if self.getPathHome():
            pathComp = self.pathHome + self.fileName #self.update_filename()
            if (self.SensorOcean.saveData(pathComp,peak1zero=self.graphdata._peak1zero,peak2zero=self.graphdata._peak2zero,temp=self.graphdata._tempzero)):
                self.ui.sbRuns.setValue(self.ui.sbRuns.value() + 1)
                self.update_filename()
 
                
    def update_filename(self):
        ''' I am so sorry, see this bad code ... Strategy was changed in a line emergency '''
        try:
            number = self.ui.sbRuns.value() #Read the spinbox value
            filetype = '.txt'

            if number < 10:
                changed = '00' + str(number) + filetype
            elif number < 100:
                changed = '0' + str(number) + filetype
            else:
                changed = str(number) + filetype
            self.ui.sufix.setText('_n' + changed)
            return True
        
        except:
            return False
    
    def errorMessage(self, message):
        self.showDialog("---Attention---", message)
    '''
    ____________________________________________________________________________________________________________________________________
    Functions not used 
    '''
        
                
    
    
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
    
    
    '''
    self.ui.lblAcquiring.linkActivated.connect(self.pri1)
        self.ui.lblAcquiring.linkHovered.connect(self.pri1)
        #self.ui.lblAcquiring.channel.
        self.ui.lblProgress.value_changed(0)
        self.ui.cmbAcquisition.send_value_signal.connect(self.pri1)
    '''  