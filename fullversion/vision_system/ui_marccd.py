'''
Created on Oct 9, 2018

@author: rodrigo.guercio
'''
import os
from vision_system.MarCCDMx225 import MarCCDMx225, DisplayTime       
from enum import IntEnum
from pydm import PyDMApplication
from PyQt5 import QtWidgets
from vision_system.interface_ccd_marccd import Ui_Ui_MainWindow_marccd

class ui_marccd(object):
    '''
    Class ui_marrcd:
        There is a class called MarCCDMx255 
        (CCD camera that has a server to communicate with others applications)
    '''

    def __init__(self):
        '''
        Constructor: Ocean Optics window -> It is command and supervisory window 
        '''
        self.ui = Ui_Ui_MainWindow_marccd()

    def setupUi(self,object = None):
        '''
        Setup of widgets
        '''
        self.ui.setupUi(object)
    
    def setFlowControl(self):
        self.connected = False
        self.marccd = MarCCDMx225(name='MarCCDMx225_guercio')
        self.ui.PyDMPushButton_connect.clicked.connect(self._deviceConnect)
        self.ui.PyDMPushButton_imagesequence.clicked.connect(self._imagesequence)
        self.ui.spinBox_filename.valueChanged.connect(self.update_filename)
        self.ui.PyDMPushButtonSelect.clicked.connect(self.getpath)
        
        self.marccd.signal.connect(self.display_status)
        self.marccd.terminated.connect(self.imagenumbercapture)
        self.timeleft = DisplayTime()
        self.timeleft.timeleft.connect(self.displaytimeleft)
        
        self.ui.PyDMPushButton_abort.clicked.connect(self.abortCapture)
        
    def getpath(self):
        self.ui.lineEdit_path.setText(QtWidgets.QFileDialog.getExistingDirectory(self.ui.PyDMPushButtonSelect))
    
    def abortCapture(self):
        try:
            if(self.timeleft.isRunning()):
                self.timeleft.terminate()
                
            if(self.marccd.isRunning()):
                self.marccd.terminate()
           
            if (self.marccd.abort_acquisition()):
                    self.ui.PyDMPushButton_imagesequence.setEnabled(True)
                    self.display_msg(msg.abortSuccess)
            else:
                self.ui.PyDMPushButton_imagesequence.setEnabled(False)
                self.display_msg(msg.abortFailed)
                
        except:
            self.display_msg(msg.FatalErro)
        
            
    def display_status(self,imagesaved):
        
        if imagesaved == 'False':
            self.display_msg(msg.NotSaved)
        else:
            self.display_msg(msg.Finished)
        
    def _imagesequence(self):  
        if not (self.connected):
            self.display_msg(msg.NotReady)
        else:
            paramssaved = self.getting_imgsequece_params()
            if paramssaved:
                self.display_msg(msg.Waiting)
                ''' Starting marccd'''
                if (self.marccd.isRunning()):
                    self.marccd.terminate()
                else:
                    self.marccd.args(exposure = self.exposure, count_number = self.count, prefix = self.fileName, pathHomeUser = self.pathHome, pix_size = self.pixelsize)
                    self.marccd.start()
                ''' Starting clock - timeleft'''
                if (self.timeleft.isRunning()):
                    self.timeleft.terminate()
                else:
                    self.timeleft.args(target_time = self.exposure)
                    self.timeleft.start()              
    
    def imagenumbercapture(self,numOfImages):
        self.msg_label = str(numOfImages) + ' of ' + str(self.count) + ' images were captured...'
        self.ui.PyDMLabel_msgerror.setText(self.msg_label)
        if numOfImages >= self.count:
            self.timeleft.terminate()
    
    def displaytimeleft(self,timeleft):
        if (self.marccd.isRunning()):
            yellow = int(2.55*timeleft*0.5)
            str_msg = "color: rgb("+ str(255-yellow) + ", 240, 0);"
            self.ui.PyDMLabel_msgerror.setStyleSheet(str_msg)
            label_msg = self.msg_label + '(' + str(timeleft) + '%)'
            self.ui.PyDMLabel_msgerror.setText(label_msg)
    
    def getting_imgsequece_params(self):
        if (not (self.check_status())):
            self.display_msg(msg.InicialStatus)
            return False
        try:
            if ((self.getExposureAndCount()) and (self.getPathHome()) and (self.getBinning()) ):
                return True
            else:
                return False
                  
        except Exception as e:
            print ("Error (getting_imgsequece_params) %s" % str(e))
            self.display_msg(msg.InputValue_mr)
            return False
                  
    def getFileName(self):
        #self.fileName = self.ui.lineEdit_filename.text()
        if '.tiff' not in self.fileName:
            self.display_msg(msg.NotTIFF)
            return False
        elif ('#' in self.fileName) or ('\\' in self.fileName) or ('/' in self.fileName) :
            self.display_msg(msg.char)
            return False
        elif ' ' in self.fileName:
            self.display_msg(msg.space)
            return False
        elif ('(' in self.fileName) or ('{' in self.fileName) or ('[' in self.fileName) or ('´'  in self.fileName):
            self.display_msg(msg.char)
            return False
        elif (')' in self.fileName) or ('}' in self.fileName) or (']' in self.fileName) or ('"'  in self.fileName):
            self.display_msg(msg.char)
            return False
        else:
            return True
        
    def getExposureAndCount(self):
        self.exposure = int(self.ui.lineEdit_Exposureone.value()) #int(self.ui.lineEdit_Exposureone.text())
        self.count = self.ui.lineEdit_count.value()#int(self.ui.lineEdit_count.text())
        if ((self.exposure < 1) or (self.count < 1)):
            self.display_msg(msg.nonegative)
            return False
        else:
            return True
        
    def getPathHome(self):
        self.pathHome = self.ui.lineEdit_path.text()
        self.pathHome = self.pathHome + '/'
        self.fileName = self.ui.lineEdit_filename.text() + self.ui.sufix.text()
        if ' ' in self.pathHome:
            self.display_msg(msg.space)
            return False
        elif(not (os.path.exists(self.pathHome))): 
            self.display_msg(msg.Directory)
            return False
        elif(not(self.getFileName())):
            return False
        elif ((os.path.isfile(self.pathHome + self.fileName) )):
            self.display_msg(msg.sameName)
            return False
        elif (not (self.update_filename())):
            self.display_msg(msg.NnotFound)
            return False
        else:
            return True
        
    def getBinning(self):
        self.pixelsize = self.checkBox_pixelsize()
        if self.pixelsize  == 0:
            self.display_msg(msg.PixelSize)
            return False
        else:
            return True
    
    def _deviceConnect(self):
        if self.getting_connection_params():
            if (self.check_status()):
                self.display_msg(msg.Double_clicked)
            else:    
                self.connected = self.marccd.connect(host = self.IP, port = self.Port)
                if self.connected:
                    self.display_msg(msg.Connected)
                else:
                    self.display_msg(msg.IP_Port_error)                    
                
            
    def getting_connection_params(self):
        try:
            self.IP = self.ui.lineEdit_IP.text()
            self.Port = int(self.ui.lineEdit_Port.text())
            return True
        except Exception as e:
            self.display_msg(msg.InputValue_error)
            print ("Error (getting_connection_params) %s" % str(e))
            return False
        
    def checkBox_pixelsize(self):
        flag512 = self.ui.PyDMCheckbox_512.isChecked()
        flag1024 = self.ui.PyDMCheckbox_1024.isChecked()
        flag2048 = self.ui.PyDMCheckbox_2.isChecked()
                             
        if (flag512 and not(flag1024) and not(flag2048)):
            return int(512)
        elif (flag1024 and not(flag2048) and not(flag512)):
            return int(1024)
        elif (flag2048 and not(flag512) and not(flag1024)):
            return int(2048)
        else:
            return int(0)
            
    def check_status(self):
        return self.marccd.check_status()
    
    def update_filename(self):
        ''' I am so sorry, see this bad code ... Strategy was changed in a line emergency '''
        try:
            number = self.ui.spinBox_filename.value() #Read the spinbox value
            filetype = '.tiff'

            if number < 10:
                changed = '00' + str(number) + filetype
            elif number < 100:
                changed = '0' + str(number) + filetype
            else:
                changed = str(number) + filetype
            self.ui.sufix.setText('_n' + changed)
            return True
        
        except Exception as e:
            self.display_msg(msg.NameStructure)
            print ("Error (update_filename) %s" % str(e))
            return False
    
    def display_msg(self, command):   

        if command == 1:
            self.ui.PyDMLabel_connectstatus.setText('Device NOT connected') 
            self.ui.PyDMLabel_msgerror.setText("Error: Inputs values are not compatible")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 0, 0);")
        elif command == 2:
            self.ui.PyDMLabel_connectstatus.setText('Error: Device NOT connected')  
            self.ui.PyDMLabel_msgerror.setText('See or restart IP and Port Address on CCD server') 
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 0, 0);")        
        elif command == 3:
            self.ui.PyDMLabel_connectstatus.setText('Device connected')
            self.ui.PyDMLabel_msgerror.setText('Device connected \o/')  
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(0, 240, 0);")
        elif command == 4:
            self.ui.PyDMLabel_connectstatus.setText('Device connected')  
            self.ui.PyDMLabel_msgerror.setText("Why did you click twice times? ¬¬'")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 0, 0);")
        elif command == 5:
            self.ui.PyDMLabel_msgerror.setText("Error: Inputs values are not compatible")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 0, 0);")
        elif command == 6: 
            self.ui.PyDMLabel_msgerror.setText("Choose only one pixel size! ")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")           
        elif command == 7:
            self.ui.PyDMLabel_msgerror.setText("Directory does not exist. Make one! ")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")
        elif command == 8: 
            self.ui.PyDMLabel_msgerror.setText("Restart marccd server :/")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")
        elif command == 9:       
            self.ui.PyDMLabel_msgerror.setText("Waiting image from device ...")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);") 
        elif command == 10: 
            self.ui.PyDMLabel_msgerror.setText("Device is NOT connected")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")
        elif command == 11:
            self.ui.PyDMLabel_msgerror.setText("Error: Image not saved on path. Check FTP server")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 0, 0);")
        elif command == 12:
            msg = self.fileName + " is ready on path"
            self.ui.PyDMLabel_msgerror.setText(msg)
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(0, 240, 0);")
            indexFile = self.ui.spinBox_filename.value()
            self.ui.spinBox_filename.setValue(indexFile + 1)
            self.update_filename()
        elif command == 13:    
            self.ui.PyDMLabel_msgerror.setText("It is not a .tiff file")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")
        elif command == 14:
            self.ui.PyDMLabel_msgerror.setText("Filename is not compatible with the structure")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);") 
        elif command == 15:
            self.ui.PyDMLabel_msgerror.setText("See FileName Structure: name_n###.tiff")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")
        elif command == 16:
            self.ui.PyDMLabel_msgerror.setText("Choose a number: Ex. name_n234.tiff")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")   
        elif command == 17:
            self.ui.PyDMLabel_msgerror.setText("Space: ' ' is not allowed")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")  
        elif command == 18:
            self.ui.PyDMLabel_msgerror.setText("Exposure and Count should be '>=1'")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")      
        elif command == 19:
            self.ui.PyDMLabel_msgerror.setText("This file name already exists")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")  
        elif command == 20:
            self.ui.PyDMLabel_msgerror.setText("Stop process was done successfully ")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(0, 240, 0);")  
        elif command == 21: 
            self.ui.PyDMLabel_msgerror.setText("Attention: stop process failed. Click again on button 'Abort acquisition' ")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 0, 0);")   
        elif command == 22:
            self.ui.PyDMLabel_msgerror.setText("-- FATAL ERROR -- You should close the vision system ")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 0, 0);")
        elif command == 23:
            self.ui.PyDMLabel_msgerror.setText("Filename: ´ [ º { ( not supported")
            self.ui.PyDMLabel_msgerror.setStyleSheet("color: rgb(240, 240, 0);")
        else:
            print("No error was mapped")    
            
              
import os
from vision_system.MarCCDMx225 import MarCCDMx225, DisplayTime       
from enum import IntEnum


class msg(IntEnum):
    InputValue_error = 1
    IP_Port_error = 2
    Connected = 3 
    Double_clicked = 4
    InputValue_mr = 5 #MuliRead
    PixelSize = 6
    Directory = 7
    InicialStatus = 8
    Waiting = 9
    NotReady = 10
    NotSaved = 11
    Finished = 12
    NotTIFF = 13
    NnotFound = 14
    NameStructure = 15
    hastag = 16
    space = 17
    nonegative = 18
    sameName = 19
    abortSuccess = 20
    abortFailed = 21
    FatalErro = 22
    char = 23
    
    
if __name__ == "__main__":  
    import sys
    app = PyDMApplication(use_main_window=False)
    Ui_MainWindow_marccd = QtWidgets.QMainWindow()
    ui = ui_marccd()
    ui.setupUi(Ui_MainWindow_marccd)
    ui.setFlowControl()
    Ui_MainWindow_marccd.show()
    app.establish_widget_connections(widget = Ui_MainWindow_marccd)
    sys.exit(app.exec_())    