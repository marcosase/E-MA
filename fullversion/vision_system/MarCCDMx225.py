
'''
Created on May 21, 2018
@author: rodrigo.guercio
See Marccd Class developed by SOL-LNLS
'''

from shutil import move
from py4syn.epics.MarCCDClass import MarCCD
from py4syn.epics.ShutterClass import SimpleShutter
from ftplib import FTP
import os, sys
from PyQt5.QtCore import pyqtSignal,QThread
from builtins import str
from future.backports.test.pystone import FALSE
#import imageio
import tifffile
import numpy as np

class MarCCDMx225(QThread):
    '''
    classdocs
    '''
    signal = pyqtSignal(str)
    terminated = pyqtSignal(int)
    def __init__(self, name ):
        '''
        Constructor
        '''
        QThread.__init__(self)
        self.name = name
        
    def connect(self,host='localhost', port=2222):       
        try:
            self.host = host
            self.port = port
            self.camera = MarCCD(self.name, (self.host, self.port)) #'192.168.1.10', port
            return True
        except Exception as e:
            print ("Unexpected error (connect):", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
        
    def check_status(self):
        try:
            ans = self.camera.getState(20)
            print('Status of camera: ', ans)
            if (ans == 0):
                return True
            else:
                self.camera.close()
                self.camera = MarCCD(self.name, (self.host, self.port)) #'192.168.1.10', port
                ans = self.camera.getState(20)
                print('Status of camera: ', ans)
                if (ans == 0):
                    return True
                else:
                    return False
                
        except Exception as e:
            print ("Unexpected error (check_status):", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
    
    def abort_acquisition(self):
        try:
            #self.camera.socket.send(b'abort\n')
            
            return self.check_status()
        except:
            return False
            
    def _move(self,filename):
        
        self._ftp(filename)  
        move(filename, self.pathHomeUser + filename)
        
        return os.path.exists(self.pathHomeUser + filename)   
    
    def _ftp(self,filename):    
        #Delete remote
        ftp = FTP('')
        ftp.connect(self.host,1026)
        ftp.login()
        ftp.cwd('') #replace with your directory
        ftp.retrlines('LIST')
        
        #filename = file #replace with your file in the directory ('directory_name')
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 8192)
        ftp.quit()
        localfile.close()   
        
    def _accumulate(self,filename):
        accumulate = 0
        for k in range(0,self.numOfimages):
            file = '_' + str(k) + '_' + filename
            self.remote = self.pathMarCCD + file
            self.captureImage(self.count_number*k+1)
            self._ftp(file)
            if not (os.path.exists(file)):
                return False
            else:
                image = np.uint32(tifffile.imread(file))
                accumulate = np.uint32(accumulate + image)
                move(file, self.pathHomeUser + file)
        
        pathFileAcclt = self.pathHomeUser + filename
        tifffile.imwrite(file = pathFileAcclt, data = accumulate)
        return os.path.exists(pathFileAcclt) 
    
    def _accumulate2(self,filename):
        ''' This function is not safe -> some headers are not compatible with it '''
        accumulate = 0
        for k in range(0,self.numOfimages):
            file = '_' + str(k) + '_' + filename
            self.remote = self.pathMarCCD + file
            self.captureImage(self.count_number*k+1)
            self._ftp(file)
            if not (os.path.exists(file)):
                return False
            else:
                #image = np.uint32(tifffile.imread(file))
                with tifffile.TiffFile(file) as image:  #This variable is a tifffile, not numpy 
                    image_matrix = image.asarray() #Now, it is numpy 
                    ''' Getting the header of tiff image '''
                    tag = image.pages[0]
                'Operating with image - numpy'
                accumulate = np.uint32(accumulate + image_matrix)
                move(file, self.pathHomeUser + file)
        'Define an address to new image'
        pathFileAcclt = self.pathHomeUser + filename
        'Now, it is time to write the new image'
        #tifffile.imwrite(file = pathFileAcclt, data = accumulate)
        with tifffile.TiffWriter(file = pathFileAcclt) as newimage:
            newimage.save(data=accumulate,
            photometric=tag.tags['PhotometricInterpretation'].value,
            planarconfig=None,
            extrasamples=None,
            tile=None,
            contiguous=True,
            align=16,
            truncate=False, 
            compress=0,
            rowsperstrip=tag.tags['RowsPerStrip'].value, 
            predictor=False, 
            colormap=None,
            description=None,
            datetime=None,
            resolution=(tag.tags['XResolution'].value[0]/tag.tags['XResolution'].value[1],tag.tags['XResolution'].value[0]/tag.tags['XResolution'].value[1]),
            subfiletype=0,
            software='tifffile.py', 
            metadata={}, 
            ijmetadata=None,
            extratags=())
        return os.path.exists(pathFileAcclt) 
            
    
    def args (self, exposure = 10, count_number = 10, prefix = 'data.tiff',pathHomeUser = '', pix_size = 1024, cumulative = 1):
        self.pathHomeUser = pathHomeUser #'/home/ABTLUS/rodrigo.guercio/Documents/MarCCD - Computer files/'
        self.pathMarCCD = '/home/marccd/XDS/2018/ftp_files/'
        #self.pathMarCCD = '/home/marccd/XDS_teste/ftp-pack/images_from_marccd/'
        self.pix_size = pix_size
        self.exposure = exposure
        self.count_number = count_number
        self.numOfimages = cumulative
        self.prefix = prefix
        self.remote = self.pathMarCCD + prefix
        self.local = self.pathHomeUser + prefix
        
        
    def run2(self):
        
        try:
            self.camera.setImageSize(width = self.pix_size, height = self.pix_size) #Binning effect
            print('self.count_number',self.count_number)
            print('self.exposure:',self.exposure)
            exp_time = self.exposure/self.count_number
            self.camera.setCountTime(exp_time) #Sets the image acquisition time.
            self.terminated.emit(0)
            if self.count_number > 1:
                self.camera.darkNoise() #Prepares a dark noise image to be used as a correction image by the server.
                self.camera.setSubScan(count=2) #Configure the MarCCD object to know that each acquisition will be done in multiple steps.
                for i in range(0,self.count_number): 
                    self.camera.startCount() #Starts acquiring an image.
                    self.camera.wait() #Blocks until the configured count time passes 
                    self.camera.stopCount() #Stops acquiring the image and stores it into server memory.
                    self.camera.waitForIdle() #Blocks until the camera server is completely idle.
                    #Final image processing aiming a single image    
                    self.camera.dezinger() #Apply the dezinger correction algorithm in 2 images and store the resulting image in the MarCCD server.
                    self.camera.correct() #Queues image correction on the MarCCD server. After the image is corrected, it can be saved to a file.
                    #Management of threads - > Got one image again
                    self.terminated.emit(i+1)
            else:
                self.camera.startCount() #Starts acquiring an image.
                self.camera.wait() #Blocks until the configured count time passes 
                self.camera.stopCount() #Stops acquiring the image and stores it into server memory.
                
            
            self.camera.writeImage(self.remote)  #Write the image stored in MarCCD server memory in a file. the MarCCD camera server to store the image in a remote location
            saved = self._move(self.prefix)

            if saved:
                self.signal.emit(self.local)
            else:
                self.signal.emit('False')    
            
        except Exception as e:
            print ("Unexpected error (RUN):", sys.exc_info()[0])
            print ("Error %s" % str(e))
            self.camera.close()
            self.signal.emit('False') 
    
    def run(self):
        
        try:
            self.terminated.emit(0)
            if self.numOfimages > 1:
                #It is necessary to save image in other place
                saved = self._accumulate(self.prefix)
            else:
                self.captureImage(1)
                saved = self._move(self.prefix)

            if saved:
                self.signal.emit(self.local)
            else:
                self.signal.emit('False')    
            
        except Exception as e:
            print ("Unexpected error (RUN):", sys.exc_info()[0])
            print ("Error %s" % str(e))
            self.camera.close()
            self.signal.emit('False')      
            
    def captureImage(self,j):
        self.camera.setImageSize(width = self.pix_size, height = self.pix_size) #Binning effect
        exp_time = self.exposure/self.count_number
        self.camera.setCountTime(exp_time) #Sets the image acquisition time.
        if self.count_number > 1:
            self.camera.darkNoise() #Prepares a dark noise image to be used as a correction image by the server.
            self.camera.setSubScan(count=2) #Configure the MarCCD object to know that each acquisition will be done in multiple steps.
            for i in range(0,self.count_number): 
                self.camera.startCount() #Starts acquiring an image.
                self.camera.wait() #Blocks until the configured count time passes 
                self.camera.stopCount() #Stops acquiring the image and stores it into server memory.
                self.camera.waitForIdle() #Blocks until the camera server is completely idle.
                if i > 0:
                    #Final image processing aiming a single image    
                    self.camera.dezinger() #Apply the dezinger correction algorithm in 2 images and store the resulting image in the MarCCD server.
                    self.camera.correct() #Queues image correction on the MarCCD server. After the image is corrected, it can be saved to a file.
                #Management of threads - > Got one image again
                self.terminated.emit(i+j)
        else:
            self.camera.startCount() #Starts acquiring an image.
            self.camera.wait() #Blocks until the configured count time passes 
            self.camera.stopCount() #Stops acquiring the image and stores it into server memory.
            
        self.camera.writeImage(self.remote)  #Write the image stored in MarCCD server memory in a file. the MarCCD camera server to store the image in a remote location
                        
    def run3(self):

        try:  
            self.camera.setImageSize(width = self.pix_size, height = self.pix_size) #Binning effect
            self.camera.setCountTime(self.exposure) #Sets the image acquisition time.
            
            if self.count_number > 1:
                self.camera.darkNoise() #Prepares a dark noise image to be used as a correction image by the server.
                self.camera.setSubScan(count=2) #Configure the MarCCD object to know that each acquisition will be done in multiple steps.
            
            for i in range(1,self.count_number): 
                self.camera.startCount() #Starts acquiring an image.
                self.camera.wait() #Blocks until the configured count time passes 
                self.camera.stopCount() #Stops acquiring the image and stores it into server memory.
                self.camera.waitForIdle() #Blocks until the camera server is completely idle.
                if i > 2:
                    #Final image processing aiming a single image    
                    self.camera.dezinger() #Apply the dezinger correction algorithm in 2 images and store the resulting image in the MarCCD server.
                    self.camera.correct() #Queues image correction on the MarCCD server. After the image is corrected, it can be saved to a file. 
                
            self.camera.writeImage(self.remote)  #Write the image stored in MarCCD server memory in a file. the MarCCD camera server to store the image in a remote location
            saved = self._move(self.prefix)
            if saved:
                self.signal.emit(self.local)
            else:
                self.signal.emit('False')    
        
        except Exception as e:
            print ("Unexpected error:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            #self.camera.close()
            self.signal.emit('False')   
            
    
    def getImage(self, fileName='image.tif', ShutterSignal = False, exposure = 10):
        try:
            if ShutterSignal:
                shutter = '' #Class Shutter
                self.shutter = SimpleShutter(shutter, shutter)
                self.camera.setCountTime(exposure)
                self.camera.startCount()
                self.shutter.open()
                self.camera.wait()
                self.camera.stopCount()
                self.shutter.close()
                self.camera.writeImage(self.pathMarCCD + fileName)
                saved = self._move(fileName)
                self.camera.close()
            else:
                #self.camera.darkNoise()
                self.camera.setImageSize(width = 2048, height = 2048)
                self.camera.setCountTime(60) #Sets the image acquisition time.
                self.camera.startCount() #Starts acquiring an image.
                self.camera.wait() #Blocks until the configured count time passes 
                self.camera.stopCount() #Stops acquiring the image and stores it into server memory.
                self.camera.writeImage(self.pathMarCCD + fileName) #Write the image stored in MarCCD server memory in a file. the MarCCD camera server to store the image in a remote location
                saved = self._move(fileName)
                self.camera.close()
                
            return saved    
        except Exception as e:
            print ("Unexpected error:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            print('ERROR: def getImage(self, fileName=image.tif, ShutterSignal = False): ')
        finally:
            self.camera.close()    
            return False
            
    def acquireSetWithCorrection(self,shutter, exposure=10, count=10, prefix='data'):
        try:
            self.shutter.close()
            self.camera.darkNoise()
            self.camera.setCountTime(exposure)
            self.camera.setSubScan(count = count)

            for i in range(count):
                fileName = '%s-%02d.tif' % (prefix, i)
                remote = self.pathMarCCD + fileName
                local = self.pathHomeUser + fileName
                self.camera.startCount()
                self.shutter.open()
                self.camera.wait()
                self.camera.stopCount()
                self.shutter.close()
                self.camera.waitForIdle()
                self.camera.startCount()
                self.shutter.open()
                self.camera.wait()
                self.camera.stopCount()
                self.shutter.close()
                self.camera.dezinger()
                self.camera.correct()
                self.camera.writeImage(remote)
                self._move(fileName)
        finally:
            self.camera.close()
            self.shutter.close() 
            
    def acquireSetWithCorrection_noshutter(self, exposure=10, c=10, prefix='data', pathMarCCD = '', pathHomeUser = ''):
        try:
            self.pathMarCCD = pathMarCCD #'/remote/'
            self.pathHomeUser = pathHomeUser #'/home/ABTLUS/rodrigo.guercio/Documents/MarCCD - Computer files/'
            self.camera.setImageSize(width = 2048, height = 2048)
            self.camera.darkNoise() #Prepares a dark noise image to be used as a correction image by the server.
            self.camera.setCountTime(exposure) #Sets the image acquisition time.
            self.camera.setSubScan(count=2) #Configure the MarCCD object to know that each acquisition will be done in multiple steps.

            for i in range(c):
                fileName = '%s-%02d.tiff' % (prefix, i)
                remote = self.pathMarCCD + fileName
                #local = self.pathHomeUser + fileName
                self.camera.startCount() #Starts acquiring an image.
                self.camera.wait() #Blocks until the configured count time passes 
                self.camera.stopCount() #Stops acquiring the image and stores it into server memory.
                self.camera.waitForIdle() #Blocks until the camera server is completely idle.
                self.camera.startCount()
                self.camera.wait() 
                self.camera.stopCount()
                self.camera.dezinger() #Apply the dezinger correction algorithm in 2 images and store the resulting image in the MarCCD server.
                self.camera.correct() #Queues image correction on the MarCCD server. After the image is corrected, it can be saved to a file.
                self.camera.writeImage(remote)  #Write the image stored in MarCCD server memory in a file. the MarCCD camera server to store the image in a remote location
                saved = self._move(fileName)
                print (saved)
        finally:
            self.camera.close()    
            
class DisplayTime(QThread):
    timeleft = pyqtSignal(int)
    def __init__(self):
        QThread.__init__(self)
    def args(self,target_time = 0,step_time = 1):
        self.targettime = target_time
        self.steptime = step_time
    def run(self):
        try:
            time_sum = -2 #Two seconds of delay
            while(self.targettime > time_sum):
                QThread.sleep(self.steptime)
                time_sum = time_sum + 0.5*self.steptime
                timeL = int(100*(time_sum/self.targettime))
                if timeL > 0 and timeL < 100:
                    self.timeleft.emit(timeL)
        except:
            self.timeleft.emit(-1)