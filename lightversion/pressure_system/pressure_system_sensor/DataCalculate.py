'''
Created on Jun 19, 2018

@author: rodrigo.guercio

Calculation of pressure using Ruby Fluorescence<br>



&nbsp;&nbsp;Temperature dependence with peak position: DD Ragan et al., J. Appl.
Phys. 72 (1992) 5539<br>



&nbsp;&nbsp;Temperature dependence with peak intensity: BA Weinstein, Rev. Sci. Instrum. 57 
(1986) 910<br>



&nbsp; Pressure dependence: AD Chijioke et al., J. Appl. Phys. 98
(2005) 114905<br>

Argonne National Laboratory<br>



Advanced Photon Source<br>



Magnetic Material Group<br>



Author: Narcizo M Souza-Neto<br>

'''
import math

class DataCalculate(object):
    '''
    classdocs
    '''


    def __init__(self, tempzero = '300', peak1zero = '692.80', peak2zero = '694.26'):
        '''
        '''
        self.standard(tempzero,peak1zero,peak2zero)
        
    def standard(self, tempzero = '300', peak1zero = '692.80', peak2zero = '694.26'):
        '''
        Standard values
        '''
        try:
            self._tempzero = float(tempzero)
            self._peak1zero = float(peak1zero)
            self._peak2zero = float(peak2zero)
            self.peak1zero = 1e7/(1e7/self._peak1zero - (3.00e-2*self._tempzero - 3.88e-4*self._tempzero*self._tempzero + 2.55e-7*self._tempzero*self._tempzero*self._tempzero))
            self.peak2zero = 1e7/(1e7/self._peak2zero - (4.49e-2*self._tempzero - 4.81e-4*self._tempzero*self._tempzero + 3.71e-7*self._tempzero*self._tempzero*self._tempzero))
            
            return True
        except:
            return False  

    def pressureCalculate(self, temp, peak1, peak2):
        '''
        Pressure Calculate
        '''
        try:
            temp = float(temp)
            peak1 = float(peak1)
            peak2 = float(peak2)
            
            peak1 = 1e7/(1e7/peak1 - (3.00e-2*temp - 3.88e-4*temp*temp + 2.55e-7*temp*temp*temp))
            peak2 = 1e7/(1e7/peak2 - (4.49e-2*temp - 4.81e-4*temp*temp + 3.71e-7*temp*temp*temp))
    
            press1 = (1876/10.71) * (math.pow((peak1/self.peak1zero),10.71)-1)
            press2 = (1876/10.71) * (math.pow((peak2/self.peak2zero),10.71)-1)
            
            self.press1 = round(press1,2)
            self.press2 = round(press2,2)
            self.pressAvg = round((press1+press2)/2,2)
        
            return True
        except :
            return False
            
        
    def peakPositionCalculate(self,temp,press1,press2):
        '''
        pealPositionCalculate
        '''
        try:
            temp = float(temp)
            press1 = float(press1)
            press2 = float(press2)
            
            peak1 = self.peak1zero*math.pow(1+(10.71/1876)*press1,1/10.71)
            peak2 = self.peak2zero*math.pow(1+(10.71/1876)*press2,1/10.71)
            
            peak1 = (1e7)/(1e7/peak1 + (3.00e-2*temp - 3.88e-4*temp*temp + 2.55e-7*temp*temp*temp))
            peak2 = (1e7)/(1e7/peak2 + (4.49e-2*temp - 4.81e-4*temp*temp + 3.71e-7*temp*temp*temp))
            
            self.peak1 = round(peak1,2)
            self.peak2 = round(peak2,2)
            
            return True
        except:
            return False
        
        return 
        
    def temperatureCalculate(self,intensity_peak1,intensity_peak2):
        '''
        temperatureCalculate
        '''
        try:
            intensity_peak1 = float(intensity_peak1)
            intensity_peak2 = float(intensity_peak2)
            
            temp = ((-3.55/0.08617343))/(math.log(intensity_peak1/(0.65*intensity_peak2)))
            self.temp = round(temp,1)
            return True
        except:
            return False