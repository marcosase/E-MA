'''
Created on Aug 13, 2018

@author: rodrigo.guercio

  (0:"Stop", 1:"Pause", 2:"Move", 3:"Go")
    normally has the value "Go." 
    the motor will not move while SPMG has the value "Stop" or "Pause."
    If "SPMG" has the value "Move," the motor record will reset SPMG to "Pause" when a motion completes.

'''

from py4syn.epics.MotorClass import Motor
import sys
import time
from PyQt5.QtCore import pyqtSignal,QThread

class Nema23(QThread):
    '''
    classdocs
    '''
    motion = pyqtSignal(bool)
    def __init__(self, pvname = "SOL3:motor", mne_ = ""):
        '''
        Constructor
        '''
        QThread.__init__(self)
        self.createMotor(pvname, mne_)
        
    def createMotor(self, pvname = "", mne_ = ""):
        
        try:
            self.motorNema = Motor(pvName=pvname, mnemonic=mne_)
            self.resert()
            return True
        
        except Exception as e:
            print ("Unexpected error -- Create Motor --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
    
    def resert(self):
        
        val = self.motorNema.getPosition()
        self.motorNema.setOffset(-val)
        
    def run(self):
        
        if self.motorNema.isMovingPV(): #There is a motion. It wants reduce or increase the velocity
            self.pause()
            self.motion.emit(False)
        else:
            '''_'''#signal to say that the will start
            self.move_RevOnM4()
            if self.paused():
                self.move()
            
    def move_RevOnM4(self):
        try:
            revs = self.revs_approx()
            print("Number of steps",revs,revs*256*200)
            self.settings_position(revs) #  revs Raw values - I need to check if the motor will start 
            self.move()
            self.motorNema.wait()
            self.motion.emit(True) #emit a signal of finished
                    
        except Exception as e:
            print ("Unexpected error -- move_RevOnM4--:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            self.motion.emit(False)#emit a signal of error
    
    def revs_approx(self):
        ''' revs_onM4 is linked to how many revolutions the bolt will be rev'''
        #Steady time on motor
        revs_total = self.revs_onM4*self.efficiency #revs
        
        return revs_total
    
    def stepsPerRevolution(self):
        
        srev = self.motorNema.motor.get('UREV') #51200
        return srev #number of full steps per revolution
    
    def stop(self):
        try:
            self.motorNema.motor.put('SPMG',0)
            self.motorNema.wait()
            return True
        except Exception as e:
            print ("Unexpected error -- stop --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
    
    def pause(self):
        try:
            self.motorNema.motor.put('SPMG',1)
            self.motorNema.wait()
            return True
        except Exception as e:
            print ("Unexpected error -- pause --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
        
    def move(self):
        try:
            self.motorNema.motor.put('SPMG',2)
            self.wait(delay = 0.1)
            return True
        except Exception as e:
            print ("Unexpected error -- move --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
        
    def go(self):
        try:
            self.motorNema.motor.put('SPMG',3)
            self.wait(delay = 0.1)
            return True
        except Exception as e:
            print ("Unexpected error -- go --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
        
    def paused(self): 
        try:
            status = self.motorNema.motor.get('SPMG')
            if status == 1:
                self.wait(delay = 0.1)
                return True
            else:
                return False
        except Exception as e:
            print ("Unexpected error -- go --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
        
    def settings_motion(self,desired_dir = 0,time_accl = 2,desired_rps = 1.0,gearbox_reduce = 1, efficiency_ = 1,revs_onM4 = 0.1):
        #SREV -> VDE SMAX -> VDE BVEL -> VDE
        try:
            delay = self.motorNema.motor.get('DLY')
            #There is no motion
            self.settings_direction(desired_dir)  
            self.wait(delay)
            self.settings_accl(time_accl) #seconds
            self.wait(delay)
            self.settings_rps(desired_rps) #rps
            self.gearbox_reduce = gearbox_reduce
            self.efficiency = efficiency_
            self.revs_onM4 = revs_onM4 #revs
            return True
                
        except Exception as e:
            print ("Unexpected error -- setting_motion --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
    
    def settings_position(self,desired_rval):
        
        real = self.motorNema.getDialRealPosition() #unit: revolution(rev) #self.motorNema.getDialPosition()
        self.motorNema.setDialPosition( pos = (desired_rval + real), waitComplete = False)
            
    def settings_direction(self,desired_dir):   
        
        real = self.motorNema.getDirection()
        if real != desired_dir:
            print ("self.motor.setDirection()")
            # userVAL = DialVAL * DIR + OFFset
            #self.motorNema.motor.put('DIR',desired_dir) *Ver manual
            
    def settings_accl(self, time_accl):
        
        real = self.motorNema.getAcceleration()
        if real != time_accl:
            self.motorNema.setAcceleration(time_accl)
            
    def settings_rps(self,desired_rps):
        
        real = self.motorNema.motor.get('S') #RVEL -> Speed in steps per second that the motor actually is moving
        if real != desired_rps:
            self.motorNema.motor.put('S',desired_rps)
            
    def wait(self,delay):
        #seconds
        time.sleep(delay)
        
        