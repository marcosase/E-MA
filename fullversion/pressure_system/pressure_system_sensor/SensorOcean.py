'''
Created on Jun 19, 2018

@author: rodrigo.guercio
based on http://git.lnls.br/cgit/
'''
from pressure_system.pressure_system_sensor.CurveDetection import indexes
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread
from py4syn.epics.OceanClass import OceanOpticsSpectrometer
from py4syn.utils.counter import createCounter
from py4syn.utils.scan import timescan, setOutput, setPlotGraph, setFitScan,\
                              setPostPointCallback, setPostScanCallback
from time import sleep
from math import fabs
from logging.config import thread
import os
import time
from epics import PV

CHANNELS = 2048

HEADER = ' --- Spectrogram data --- ' 
DEVICE = '\n Modular Spectrometer: H2000+ Ocean Optics'
PAPERS = '\n --- Calculation of pressure using Ruby Fluorescence ---- ' + \
    '\nTemperature dependence with peak position: DD Ragan et al., J. Appl. Phys. 72 (1992) 5539' + \
    '\nTemperature dependence with peak intensity: BA Weinstein, Rev. Sci. Instrum. 57 (1986) 910' + \
    '\nPressure dependence: AD Chijioke et al., J. Appl. Phys. 98 (2005) 114905'
STANDARD = '\n --- Standard values for zero pressure ---'
LEGEND = '\n(nm) --- (intensity)'

class SensorOcean(QThread):
    '''
    SensorOcean is a class that acquires spectrogram from OceanOpticsSpectrometer
    and calculates the two most important peaks to calculate pressure
    '''
    error_message = pyqtSignal(str)
    signal = pyqtSignal([np.ndarray])
    
    def __init__(self, pvname):
        QThread.__init__(self)
        self.pvname = pvname
        try:
            self.createOcean()
        except RuntimeError:
            self.ocean = None

    def createOcean(self):
        self.numPoints = 2048
        self.mnemonic = str(int(time.time()))
        self.ocean = OceanOpticsSpectrometer(self.mnemonic, pv=self.pvname, numPoints=self.numPoints)
        createCounter(self.mnemonic, self.ocean)
        # disable graph and fitscan
        setPlotGraph(False)
        setFitScan(False)
        
        self.pvProgressBar = PV(self.pvname + ':ProgressBar')
        if  self.pvProgressBar.get() <= 1:
            if (self.ocean.pvStart.get() == "Start"):
                self.ocean.pvStart.put("Stop")
            
        self.pvProgressBar.add_callback(self.searchPeaks)
        
        
    def editIntegrationTime(self, timeValue):
        ''' Edit integration time '''
        ''' It was developed due to a good interface user style'''
        try:
            self.timeValue = timeValue
            self.ocean.pvTime.put(value = timeValue, wait = True)
            return True
        except:
            return False
            
    def isReady(self):
        # if ocean is disconnected cannot run
        if self.ocean is None:
            try:
                self.createOcean()
            except RuntimeError:
                return False
        return True
        
    
    def searchPeaks(self,pvname=None, value=None,
              char_value=None, **kws):
        try:
            if (char_value is not None) and (float(char_value) >= 100):
                ''' Defining which data is X or Y '''
                ydata = self.getYdata()       
                xdata = self.getXdata()
                ''' Selecting peaks and getting the respective wavelength '''
                wavelength = indexes(ydata,xdata)
                #wavelength = np.array([695,694])
                #print('wavelength',wavelength)
                ''' Filtering situations to emit signal'''    
                if wavelength is not None:
                    self.signal.emit(wavelength)
                else:
                    self.signal.emit(np.array([-1,-1]))
            
        except OSError as err:
            self.error_message.emit("Fatal exception error! Close E-MA application! ->"
                                + str(err))        
    
    def getYdata(self):
        ''' Getting Y data '''
        dark = self.ocean.pvDarkCorrection.get()
        ''' The spectra come from different pv if use darkcorrection '''
        if dark == 1:
            allSpectrum =self.ocean.pvSpectrumCorrected.get(as_numpy=True)[:self.numPoints]
        elif dark == 0:
            allSpectrum = self.ocean.pvSpectrum.get(as_numpy=True)[:self.numPoints]
        else:
            allSpectrum = 0
        
        return allSpectrum
    
    def getXdata(self):
        ''' Getting X data '''
        return self.ocean.axis #I need to test if axis X will have the same range regardless of time'''
    
    def saveData(self,pathComp,peak1zero = 692.80,peak2zero = 694.26,temp = 300.00):
        try:
            np.savetxt(pathComp,
                       np.array([self.getXdata(), self.getYdata()]).T,
                       fmt="%f\t%f", header = self.headerData(peak1zero,peak2zero,temp))
            if ((os.path.isfile(pathComp))):
                self.error_message.emit("Spectrogram data saved!"
                                + str(' See:') + pathComp)
                return True
            else:
                self.error_message.emit("Average file not saved. Error saving file.")
                return False
        except OSError as err:
            self.error_message.emit("Average file not saved. Error saving file: "
                                + str(err))
            return False
        
    def headerData(self,peak1 = 692.80,peak2 = 694.26,temp = 300.00):
        itime = '\n Integration time (s): ' + str(self.timeValue)
        peaks1 = '\nPeak1 (nm): ' + str(peak1)
        peaks2 = '\nPeak2 (nm): ' + str(peak2)
        temp = '\nTemperature (K): ' + str(temp)
        clocktime = '\nSaved at: ' + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    
        return HEADER + DEVICE + itime + PAPERS  + STANDARD + peaks1 + peaks2 + temp + clocktime + LEGEND
        
    def run(self):

        import time
        while(True):
            try:
                #start = time.time()
                ''' Getting data from PV'''
                dark = self.ocean.pvDarkCorrection.get()
                print('Dark value: ', dark)
                if dark is None:
                    break
                else:
                    #self.searchPeaks(dark)
                    sleep(self.scantime)
                #stop = time.time()
                #print('Time exec: ',(stop-start))
            
            except OSError as err:
                self.error_message.emit("Error on automatic search peak: "
                                + str(err))
                break
            
    def oneread(self):
        try:
            ''' Getting data from PV'''
            dark = self.ocean.pvDarkCorrection.get()
            print('Dark value: ', dark)
            if dark is not None:
                self.searchPeaks(dark)
        
        except OSError as err:
            self.error_message.emit("Error on automatic search peak: "
                                + str(err))