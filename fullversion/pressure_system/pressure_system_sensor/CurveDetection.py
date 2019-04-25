'''
Created on Jul 2, 2018

@author: rodrigo.guercio
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Peak detection algorithms.'''

import numpy as np
from scipy import optimize
import math
from lmfit.models import LorentzianModel
import matplotlib.pyplot as plt
import pylab


def indexes(input_array,axis_x, thres = 0.01, error_fit = 0.5, deltaMin_nm = 1.0):
    '''Peak detection routine.
    Finds the peaks in *y* by taking its first order difference. By using
    *thres* and *min_dist* parameters, it is possible to reduce the number of
    detected peaks.
    Parameters
    ----------
    y : ndarray
        1D amplitude data to search for peaks.
    thres : float between [0., 1.]
        Normalized threshold. Only the peaks with amplitude higher than the
        threshold will be detected.
    min_dist : int
        Minimum distance between each detected peak. The peak with the highest
        amplitude is preferred to satisfy this constraint.
    Returns
    -------
    ndarray
        Array containing the indexes of the peaks that were detected
    '''
    try:
        range = np.where((axis_x > 689) & (axis_x < 720)) #Range between 0 Gpa and 80 Gpa aprox
        
        ''' Normalizing input array '''
        y = normalizeY(input_array[range])
        ''' Range of X '''
        x = axis_x[range]
        '''Find the peaks by using the first order difference'''
        dy = np.diff(y)
        '''Find the peaks according to first order difference +- and threshold'''
        p= 0.00
        peaks = np.where((np.hstack([dy, p]) < p)
                     & (np.hstack([p, dy]) > p)
                     & (y > thres))[0]
    
        '''Min value of distinction between curves '''
        min_dist = set_min_dist(x, delta_nm = deltaMin_nm) #Samples
        
        #print('Indexes - Peaks:',peaks)
        ''' '''
        if peaks.size > 1 and min_dist > 1: #There is some peak
            ''' Filter peaks according to minimum distance between them '''
            majors = filterPeaks(y, peaks, min_dist)
            
            ''' Calculating the center of lorentzian '''
            if majors.size > 1: #There is more than one peak
                x_for_max_y = np.round_(a = x[majors[0]], decimals = 2) #nm
                [center_right,I2] = lorentzian_fit(x,y,majors[0], error = error_fit,range_sample = min_dist)
                [center_left,I1] = lorentzian_fit(x,y,majors[1], error = error_fit,range_sample = min_dist)   
                
                ''' Are centers float or int numbers ?''' #Fitting is enough to detect peaks
                if center_left is not None and center_right is not None:
                    center_left = np.round_(a = center_left, decimals = 2) #nm
                    center_right = np.round_(a = center_right, decimals = 2) #nm
                    
                    'Rightmost peak is bigger than leftmost peak (nm) and their relative distance is smaller than 5 nm, for example'
                    if ((center_right > center_left) and (center_right - center_left) < 5*deltaMin_nm): #(wl[0] > wl[1]) and (wl[0] - wl[1] < 120.5): #rightmost peak should greater than leftmost
                        temp = temperatureCalculate(I1, I2)
                        print('Int. peaks:', I1,I2,temp)
                        return np.array([center_right,center_left,temp])
                    else: 
                        return np.array([x_for_max_y,-1,-1])
                    
                else:
                    return np.array([x_for_max_y,-1,-1])
               
            elif majors.size == 1:
                center_right= lorentzian_fit(x,y,majors[0], error = error_fit,range_sample = min_dist)
                
                ''' Are centers float or int numbers ?'''
                if center_right is not None:
                    center_right = np.round_(a = center_right, decimals = 2) #nm
                    return np.array([center_right,-1,-1])
                else:
                    return np.array([x_for_max_y,-1,-1])
                
            else:
                'If there no peak'
                return None
        else:
            'There is no peak'
            return None    
    except:
        return None
    
def temperatureCalculate(intensity_peak1,intensity_peak2):
    '''
    temperatureCalculate
    '''
    try:
        intensity_peak1 = float(intensity_peak1)
        intensity_peak2 = float(intensity_peak2)
            
        temp = ((-3.55/0.08617343))/(math.log(intensity_peak1/(0.65*intensity_peak2)))
        temp = round(temp,1)
        return temp
    except:
        return 300    

def filterPeaks(y,peaks,min_dist):
    ''' Filter peaks according to minimum distance between them '''
    highest = peaks[np.argsort(y[peaks])][::-1]
    rem = np.ones(y.size, dtype=bool)
    rem[peaks] = False

    for peak in highest:
        if not rem[peak]:
            sl = slice(max(0, peak - min_dist), peak + min_dist + 1)
            rem[sl] = True
            rem[peak] = False

    peaks = np.arange(y.size)[~rem]
    majors = peaks[np.argsort(y[peaks])][::-1]
    
    if majors.size > 1:
        minors = 0
        minors = np.where(majors < majors[0])[0]
        #inors = np.where(majors < 1)[0]
        if minors.size > 0:
            majors[1] = majors[minors[0]]
        
    return majors

def getTwoMajorPeaks(majors): 
    ''' Getting two major peaks'''
    
    if majors.size > 1:
        return majors[0:2]
    elif majors.size == 1:
        return majors[0]
    else:
        return None

def transformIndtoNM(peak,x):
    peak_nm = np.round_(a = x[peak], decimals = 2) #xdata[peaks] 
    return peak_nm
    

def normalizeY(y):
    y_max = np.max(y)
    y_min = np.min(y)
    
    deltaY = y_max - y_min
    n = np.size(y)
    
    z = np.ones(n)
    for i in range(0,n):
        z[i] = (y[i] - y_min)/deltaY
        
    return z

def desNormalizePointY(y,z):
    y_max = np.max(y)
    y_min = np.min(y)
    
    deltaY = y_max - y_min
    
    return z*deltaY + y_min

def set_min_dist(x,delta_nm = 10):
    ''' Minimum distance to differentiate two Lorentzian Curves '''
    #Number of samples
    n = np.size(x)
    
    #Range of x nm
    x_max = np.max(x)
    x_min = np.min(x)
    x_range = x_max - x_min #nm
    
    #Sample per nm
    ss_p_nm = n/x_range #samples/nm
    
    #Const 10% of all nm => ? samples
    min_dist = ss_p_nm*delta_nm  #samples
    
    return int(min_dist)

def gaussian(x, ampl, center, dev):
    '''Computes the Gaussian function.
    Parameters
    ----------
    x : float
        Point to evaluate the Gaussian for.
    a : float
        Amplitude.
    b : float
        Center.
    c : float
        Width.
    Returns
    -------
    float
        Value of the specified Gaussian at *x*
    '''
    return ampl * np.exp(-(x - center) ** 2 / (2 * dev ** 2))

def lorentzian(x, ampl, center, w):
    return ampl*(1./2.0/np.pi)*(w/((x-center)**2+w**2/4.0))
    #return ((1/np.pi)*(0.5*w))/((x-center)**2 + (0.5*w)**2)
    
def gaussian_fit(x, y):
    '''Performs a Gaussian fitting of the specified data.
    Parameters
    ----------
    x : ndarray
        Data on the x axis.
    y : ndarray
        Data on the y axis.
    Returns
    -------
    ndarray
        Parameters of the Gaussian that fits the specified data
    '''
    initial = [np.max(y), x[0], (x[1] - x[0]) * 5]
    params, pcov = optimize.curve_fit(gaussian, x, y, initial)
    return params[1]

def lorentzian_fit(x, y,peak, error = 0.10,range_sample = 10):
    try:
        ''' Range of signal to be fitted '''
        range = round(range_sample/2)
        ''' Selecting a small range of signal '''
        #initial = [np.max(y), x[peak], (x[peak+1] - x[peak]) * 5]
        initial = [y[peak], x[peak], (x[peak+1] - x[peak]) * 5]
        x_compact = x[peak - range:peak + range]
        y_compact = y[peak - range:peak + range]
        params, pcov = optimize.curve_fit(lorentzian, x_compact, y_compact,initial)
        if (params is not None) and (pcov is not None):
            perr = np.sqrt(np.diag(pcov))
            #print('Error:', np.sum(perr))
            #print('Params :',params)
            if np.sum(perr) < error:
                return float(params[1]),float(0.637*params[0]/params[2])
            else:
                return None,None
    except:
        return None,None
        #return x[peak],y[peak]
    
def lorentzian_fit2(x, y,peak):
    #initial = [np.max(y), x[i], (x[i+1] - x[i]) * 5]
    initial = [np.max(y), x[peak], (x[peak+1] - x[peak]) * 5]
    plt.plot(x,y)
    wl = x[peak]
    x_compact = x[peak - 5:peak + 5]
    y_compact = y[peak - 5:peak + 5]
    plt.plot(x_compact,y_compact)
    params, pcov = optimize.curve_fit(lorentzian, x_compact, y_compact,initial)
    plt.axvline(x = wl) 
    plt.axvline(x = params[1])
    am = desNormalizePointY(y, np.pi/2.0)
    fit = lorentzian(x = x_compact, ampl = params[0], center = params[1], w = params[2])
    #inter = interpolate(x,y,ind = peak)
    #print(inter)
    #fit = normalizeY(fit)
    print('max value of y', np.max(y_compact))
    plt.plot(x_compact, fit,'r--' )
    print("params: ", params)
    print("pcov", pcov)
    perr = np.sqrt(np.diag(pcov))
    print('standard deviation errors', perr)
    print('Interpolate: ',params[1])
    pylab.show()
    print('Real',wl )
    return float(params[1])


def interpolate(x, y, ind=None, width=20, func=lorentzian_fit):
    '''Tries to enhance the resolution of the peak detection by using
    Gaussian fitting, centroid computation or an arbitrary function on the
    neighborhood of each previously detected peak index.
    Parameters
    ----------
    x : ndarray
        Data on the x dimension.
    y : ndarray
        Data on the y dimension.
    ind : ndarray
        Indexes of the previously detected peaks. If None, indexes() will be
        called with the default parameters.
    width : int ==> Window
        Number of points (before and after) each peak index to pass to *func*
        in order to encrease the resolution in *x*.
    func : function(x,y)
        Function that will be called to detect an unique peak in the x,y data.
    Returns
    -------
    ndarray :
        Array with the adjusted peak positions (in *x*)
    '''
    print("Entrou! 1")
    
    if ind is None:
        ind = indexes(y)
    print("Entrou! 2")
    out = []
    print("Entrou! 3")
    for slice_ in (slice(i - width, i + width) for i in ind):
        print("Entrou! 4")
        try:
            fit = func(x[slice_], y[slice_])
            print(fit)
            out.append(fit)
        except Exception:
            #pass
            print("ERROR ON SLICE FIT LAUT")
    print('SAiu do laco')
    print(np.array(out))
    return np.array(out)

def get_index_from_values(vector, values):
    """ returns the index of values in the vector """
    ind = []
    for v in values:
        diff = abs(v-vector)
        i = np.argmin(diff)
        ind.append(i)
        
    return np.array(ind)

def lorentzianFunctionGenerator(x1,r1,x2,r2,x3,r3,n):
    #n = 50000
    x = np.linspace(start = 650, stop = 750, num = n)
    
    y_num1 = 200*(1/3.14)*(0.5*r1)
    y_num2 = 200*(1/3.14)*(0.5*r2)
    y_num3 = 300*(1/3.14)*(0.5*r3)
    
    y_den1 = np.ones(n)
    y_den2 = np.ones(n)
    y_den3 = np.ones(n)
    
    np.random.seed(1729)
    y_noise = 0.2 * np.random.normal(size=x.size)

    for i in range(0,n):
        y_den1[i] = math.pow((x[i]-x1), 2) + math.pow((0.5*r1),2)
        y_den2[i] = math.pow((x[i]-x2), 2) + math.pow((0.5*r2),2)
        y_den3[i] = math.pow((x[i]-x3), 2) + math.pow((0.5*r3),2)
    
    y1 = y_num1/y_den1
    y2 = y_num2/y_den2
    y3 = y_num3/y_den3
    
    
    y = y1 + y2 + y3 + y_noise
    return [x,y]
    

def params_Lorentzian(x,y):
    mod = LorentzianModel()
    params = mod.guess(y,x)
    print (params)
    out = mod.fit(y, params, x=x)
    print(out.fit_report(min_correl=0.3))
    init = mod.eval(params, x=x)
    plt.figure(2)
    plt.plot(x, y, 'b')
    plt.plot(x, init, 'k--')
    plt.plot(x, out.best_fit, 'r-')

def mult_params_peaks_Lorentzian(x,y):
    #http://cars9.uchicago.edu/software/python/lmfit/builtin_models.html
    
    loren_mod1 = LorentzianModel(prefix='l1_')
    pars = loren_mod1.guess(y,x)
    
    loren_mod2 = LorentzianModel(prefix='l2_')
    pars.update(loren_mod2.make_params())
    
    loren_mod3 = LorentzianModel(prefix='l3_')
    pars.update(loren_mod3.make_params())

    mod = loren_mod1 + loren_mod2 + loren_mod3

    init = mod.eval(pars, x=x)

    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))

    plot_components = False

    plt.plot(x, y, 'b')
    plt.plot(x, init, 'k--')
    plt.plot(x, out.best_fit, 'r-')

    if plot_components:
        comps = out.eval_components(x=x)
        plt.plot(x, comps['l1_'], 'b--')
        plt.plot(x, comps['l2_'], 'b--')
        plt.plot(x, comps['l3_'], 'b--')
         
if __name__ == '__main__':
    pass
    #PATH = '/home/ABTLUS/rodrigo.guercio/Pictures/3test/GearBox/goldenPressure/subidarubi/'
    #PATH ='/home/ABTLUS/rodrigo.guercio/Downloads/'
    PATH = '/home/ABTLUS/rodrigo.guercio/Pictures/barbara/'
    #PATH = '/home/ABTLUS/rodrigo.guercio/Pictures/Ruby_kousik/'
    #name = 'au_002_21p85_GPa_d_n016.txt'
    #name = 'au_002_6p36_GPa_d_n000.txt'
    #name = 'lab6_17p5GPa_6p67K_n000.txt'
    #name = 'GdPtBi_0p95GPa_300K_n000.txt'
    name = 'f_10_r_11_n001.txt'
    #ame = 'f_80_r_80_n002.txt'
    #name = 'Ruby_8p69GPa_14K_n005.txt'
    #name = 'Ruby_29p82GPa_14K_n016.txt'
    #name = 'Ruby_52p30GPa_14K_n020.txt'
    #name = 'Ruby_17K_n001.txt'
    #name = 'Ruby_55p30GPa_14K_Problem_n021.txt'
    name = 'au_002_25p63_GPa_d_n020.txt'
    [x,y] = np.loadtxt(fname = PATH+name, delimiter = '\t', skiprows = 0, unpack = True, ndmin = 0)
    plt.figure(1)
    y = normalizeY(y)
    plt.plot(x,y,'r--')
    wavelength = indexes(y,x)
                
    if wavelength is not None:
        print(wavelength)
        #print(wavelength[2])
    else:
        print(wavelength)
        
    
    #print(temperatureCalculate(0.01,1))
    #print(temperatureCalculate(0.03,1))
    #print(temperatureCalculate(0.2,1))
    #print(temperatureCalculate(0.3,1))
    #print(temperatureCalculate(0.44,1))
    
    y[y<0.01*np.max(y)] = 0
    plt.plot(x,y,'*b')
    pylab.show() 
    '''
    import random
    for i in range(1,2):
        a = random.uniform(1,20)
        b = random.uniform(-10,10)
        c = random.uniform(-5,10)GdPtBi_0p95GPa_300K_n000
        x_1 = 680 + a
        r_1 = 10 + a
        x_2 = 700 + b
        r_2 = 10 + b
        x_3 = 720 + c
        r_3 = 20 + c
        samples = int(2048 + random.uniform(-500,500))
        [x,y] = lorentzianFunctionGenerator(x1 = x_1, r1 = r_1 , x2 = x_2, r2 = r_2, x3 = x_3 , r3 = r_3,n = samples)
    
        plt.figure(i)
        plt.plot(x,y,'r--')
    
        z = normalizeY(y)
        plt.plot(x,z,'b--')
    
        peaks = indexes(y, x, thres=0.3)
        print(peaks)
        print(x[peaks])
        
        
        for p in x[peaks]:
            plt.axvline(x = p)
            print('Peaks %d',i)
            print('Real: %d %d %d',x_1,x_2,x_3)
            print('Samples %d',samples)
            print(x[peaks])
            print(y[peaks])
            print('------')
        
    pylab.show()  
    '''  