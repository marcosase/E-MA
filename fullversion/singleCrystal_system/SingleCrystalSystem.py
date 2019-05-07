'''
Created on Mar 27, 2019

@author: rodrigo.guercio
'''

from singleCrystal_system.interface_singleCrystalA import Ui_MainWindow
from pydm import PyDMApplication
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import pyqtSignal,QThread

from qtpy.QtWidgets import QWidget


class SingleCrystalSystem(QThread):
    '''
    classdocs
    '''
    motorfinished = pyqtSignal()
    
    def __init__(self, parent = None):
        QThread.__init__(self)
        self.ui = Ui_MainWindow()
    
        
    def setupUi(self,object = None,name = 'dmc:galil:test:A'):
        '''
        Setup of widgets
        '''
        self.ui.setupUi(object)
        self.rename_channelPV(name)
        
    def setFlowControl(self):
        #self.ui.PyDMPushButton_Measure.clicked.connect(self.move) # +/- motor GO
        self.ui.PyDMCheckbox_msg.stateChanged.connect(self.endMotion) # FINISH 
        
        self.ui.PyDMSpinbox_aF.valueChanged.connect(self.setMaxLimit) 
        self.ui.PyDMSpinbox_a0.valueChanged.connect(self.setMinLimit)
        
        self.ui.QMotor.PyDMPushButton_rlv_plus.clicked.connect(self.blockDiffractionSystem)
        self.ui.QMotor.PyDMPushButton_rlv_minus.clicked.connect(self.blockDiffractionSystem)
        self.ui.QMotor.PyDMPushButton_stop.clicked.connect(self.blockDiffractionSystem)
        self.ui.QMotor.PyDMLineEdit_val.editingFinished.connect(self.blockDiffractionSystem)
        
        self.angle_step = 0
        
    def rename_channelPV(self, name = 'dmc:galil:test:A'):
        #self.ui.QMotor.setProperty("channel", _translate("MainWindow", "ca://dmc:galil:test:A"))
        name = 'ca://' + name
        self.ui.QMotor.channel = name
        self.ui.PyDMSpinbox_a0.channel = name + '.LLM'
        self.ui.PyDMSpinbox_aF.channel = name + '.HLM'
        self.ui.PyDMCheckbox_msg.channel = name + '.DMOV'
        #self.ui.PyDMCheckbox_msg.channel = name + '.MOVN'
        
    def blockDiffractionSystem(self):
        self.ui.checkBox_enableMarccd.setChecked(False)
        
    def endMotion(self,value):
        #Precisa de signal para saber se foi do automatico ou do manual!
        if value == 0:
            self.ui.msg.setText('Motor is moving! Wait, please!')
        else:
            self.ui.msg.setText('You are allowed to capture image!')
            self.motorfinished.emit()

    
    def move_bySystem(self):
        self.ui.QMotor.PyDMPushButton_rlv_plus.updatePressValue(self.angle_step)
        self.ui.QMotor.PyDMPushButton_rlv_plus.sendValue()
    
    def move(self):
        self.getParameters()
        self.move_bySystem()

        
    def getParameters(self):
        self.angle_step = self.ui.doubleSpinBox_step.value()
    
    def setMaxLimit(self):
        self.ui.PyDMSpinbox_aF.send_value()
        
    def setMinLimit(self):
        self.ui.PyDMSpinbox_a0.send_value()
        
    
if __name__ == "__main__":  
    import sys
    app = PyDMApplication(use_main_window=False)
    Ui_MainWindow_Ocean = QtWidgets.QMainWindow()
    ui = SingleCrystalSystem()
    ui.setupUi(Ui_MainWindow_Ocean)
    ui.setFlowControl()
    Ui_MainWindow_Ocean.show()
    app.establish_widget_connections(widget = Ui_MainWindow_Ocean)
    sys.exit(app.exec_())   
