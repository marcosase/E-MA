'''
Created on Aug 16, 2018

@author: rodrigo.guercio
'''
from interface_motor_nochannel import Ui_MainWindow_motor
from PyQt5 import QtWidgets 
from pydm import PyDMApplication
from Nema23 import Nema23
import sys 

class NemaKalatec(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.ui = Ui_MainWindow_motor()

    def setupUi(self,object = None):
        self.ui.setupUi(object)
    
    def setFlowControl(self):
        self.ui.PyDMPushButton_move.clicked.connect(self.moveMotor)
        self.ui.PyDMPushButton_restart.clicked.connect(self.restartMotor)
        self.ui.PyDMPushButton_stop.clicked.connect(self.pauseMotor)
        self.machine = Nema23(pvname='SOL:galil:test:A',mne_='kalatec01')
        self.machine.pause()
        self.machine.motion.connect(self.printA)
        self.moveFlag = True
        self.gpa_desired = None
        self.pauseUser = False
        
    def printA(self):
        print('-------Finished Motion-------')

    def moveMotor(self):
        self.pauseUser = False
        if (self.getparams()) and not(self.machine.isRunning()):
            self.startMotor()
        else:
            self.ui.msg_error.setText('MoveMotor - error')
            
    def startMotor(self):
        if (not(self.pauseUser) and self.machine.settings_motion(desired_dir = self.dir, time_accl = self.acc, desired_rps = self.rps, gearbox_reduce = self.gb, efficiency_= self.eff, revs_onM4 = self.revs_desired)):
            self.machine.start()
            #self.ui.msg_error.setText('StartMotor')
            self.moveFlag = True
        else:
            self.ui.msg_error.setText('StartMotor - error')
    
    def pauseMotor(self):
        self.pauseUser = True
        self.pauseMotor_automatic()
    
    def pauseMotor_automatic(self):
        self.ui.msg_error.setText('pauseMotor')
        self.machine.pause()
        self.moveFlag = False
        
    def restartMotor(self):
        self.ui.msg_error.setText('restartMotor')
        ''' Ver documentacao para settar os parametros corretos'''
        
        
    def getparams(self):
        try:
            self.dir = 0 #self.ui.cb_Dir.QComboBox.get() #getCurrentIndex() #self.dd = float(self.ui.lineEdit_dir.text())
            self.acc = self.ui.dSB_accl.value() #self.ta = float(self.ui.lineEdit_as.text())
            self.rps = self.ui.dSB_s.value()#self.dr = float(self.ui.lineEdit_rps.text())
            self.gb = self.ui.dSB_reduction.value() #self.gb = float(self.ui.lineEdit_red.text())
            self.eff = self.ui.dSB_eff.value()/100#self.ef = float(self.ui.lineEdit_eff.text())
            return self.chooseGPAorROT() #It could be choose between GPA and nm of wavelenght 
        except Exception as e:
            print ("Unexpected error -- getparams --:", sys.exc_info()[0])
            print ("Error %s" % str(e))
            return False
        
    def chooseGPAorROT(self):
        
        if self.ui.checkBox_2.isChecked() and not(self.ui.checkBox.isChecked()):
            self.revs_desired = self.ui.dSB_graus.value()/360 #self.gr = float(self.ui.lineEdit_graus.text())
            print("Graus select (revs):",self.revs_desired)
            return True
        elif self.ui.checkBox.isChecked() and not(self.ui.checkBox_2.isChecked()):
            self.gpa_desired = self.ui.dSB_gpa.value()
            self.revs_desired = 0 #self.revsEstimationAndGo(self.gpa_desired, 0)
            print("GPa select (revs):",self.revs_desired)
            return True
        else:
            self.ui.msg_error.setText('Choose only one checkbox')
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
            if (flag and (self.gpa_desired is not None)): #Is there real value ?
                self.gpa_real = gpa_real 
                if self.gpa_real >= self.gpa_desired: #Is it the desired value ?
                    self.ui.msg_error.setText('Desired pressure reached!\0/') #Automatic system task was done! Do manually
                    self.pauseMotor_automatic() #Pause
                else:
                    if not(self.machine.isRunning()): #Is it stopped but it is not the desired value ?
                        if (self.gpa_desired - self.gpa_real > 0.01) and self.moveFlag: #it is so close... but there is no more motion
                            self.revs_desired = self.revsEstimationAndGo(self.gpa_desired, self.gpa_real) #New estimation
                            self.ui.msg_error.setText('--Automatic adjustment--')  
                            self.startMotor() #Go
                        else:
                            print("self.gpa_desired - self.gpa_real < 0.01")
                            self.ui.msg_error.setText('--Do manual adjustment--')
                    else:
                        self.ui.msg_error.setText('There a motion! Wait ')
            else:
                self.pauseMotor_automatic() #Pause
                self.moveFlag = True #But, it is possible to continue if another true value exists
                self.ui.msg_error.setText('No signal was found')
                
        except Exception as e:
            print ("Unexpected error -- Create Motor --:", sys.exc_info()[0])
            print ("Error %s" % str(e))

    
if __name__ == "__main__":  
    import sys
    app = PyDMApplication(use_main_window=False)
    Ui_MainWindow_ = QtWidgets.QMainWindow()
    ui = NemaKalatec()
    ui.setupUi(Ui_MainWindow_)
    ui.setFlowControl()
    Ui_MainWindow_.show()
    app.establish_widget_connections(widget = Ui_MainWindow_)
    sys.exit(app.exec_())    