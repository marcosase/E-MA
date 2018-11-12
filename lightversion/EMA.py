'''
Created on Jun 8, 2018

@author: rodrigo.guercio
Working as intern at LNLS
'''
import sys
from vision_system.MainController_dioptas import MainController, excepthook
from PyQt5 import QtWidgets
from pydm import PyDMApplication
from PyQt5.QtWidgets import QMessageBox


class EmaApp (object):
    def __init__(self): 
        '''Open initial interface of E-Manager Application '''       
        self.setEmaApp()
        
        ''' EditPVNames on screen'''
        self.setEditPVnames()
        
        ''' Pressure System '''
        self.setOceanApp()
        
        ''' Set rules '''
        self.__setFlowControl() 
        
    
    def setEmaApp(self):
        ''' Ema App: Display and settings'''
        from main.interface_i import Ui_MainWindow
        self.window_MW = QtWidgets.QMainWindow()
        self.ui_MW = Ui_MainWindow()
        self.ui_MW.setupUi(self.window_MW)       
        self.uploadEmaphoto()

        
    def setOceanApp(self):
        ''' Pressure System Interface: Settings '''
        from pressure_system.PressureSystemLight import PressureSystem
        self.Ui_MainWindow_Ocean = QtWidgets.QMainWindow()
        self.ui_ocean = PressureSystem()
        self.ui_ocean.setupUi(self.Ui_MainWindow_Ocean)
        self.ui_ocean.setFlowControl(oceanPV = self.pvname_ocean, motorPV = self.pvname_motorGearBox, LS = self.pvname_lakeshore)

        
    def setEditPVnames(self):
        ''' Edit PVnames of each system: Settings '''
        from main.interface_PVnames import Ui_MainWindow_PVnames
        self.Ui_MainWindow_editPVnames = QtWidgets.QMainWindow()
        self.ui_pvnames = Ui_MainWindow_PVnames()
        self.ui_pvnames.setupUi(self.Ui_MainWindow_editPVnames) 
        ''' Edit lineedit '''
        self.setFlowControl_pvname()
        self.getting_pvname()
         
    def  __setFlowControl(self):
        ''' Signals to display each system interface '''
        self.ui_MW.PyDMPushButton_visionsystem.clicked.connect(self.__openDioptas)
        self.ui_MW.PyDMPushButton_ligthsystem.clicked.connect(self.__openLightSource)
        self.ui_MW.PyDMPushButton_pressuresystem.clicked.connect(self.__openPressureSystem)
        self.ui_MW.toolButton.clicked.connect(self.__openEditPVnames)
        
        
        self.window_MW.show()  

    
    def __openEditPVnames(self):
        ''' Edit PVnames of each system: Displaying '''
        self.Ui_MainWindow_editPVnames.show()
        
    def __openPressureSystem(self):
        ''' PressureSystem displaying '''
        if(self.ui_MW.PyDMCheckbox_pressure.isChecked()):
            app.establish_widget_connections(widget = self.Ui_MainWindow_Ocean)
            self.Ui_MainWindow_Ocean.show()
        else:
            #self.ui_ocean.mruns.mnemonic = 'ocean1'
            self.showDialog(title = 'Box of Pressure System: Not Checked', text = 'Box of Pressure System: Not Checked')
        
    def __openDioptas(self): 
        ''' Dioptas displaying'''
        if (self.ui_MW.PyDMCheckbox_visionsystem.isChecked()):
            ui_Dioptas.show_window()
            print('dioptas.run()')
        else: 
            self.showDialog(title = 'Box of Vision System: Not Checked', text = 'Box of Vision System: Not Checked')
    
            
    def __openLightSource(self):
        if (self.ui_MW.PyDMCheckbox_lightsource.isChecked()): 
            '''
            self.ui_MW.checkBoxLS_status()
            from interface_lightsource import Ui_MainWindown_lightsource
            self.window_LS = QtWidgets.QMainWindow()
            self.ui_LS = Ui_MainWindown_lightsource()
            self.ui_LS.setupUi(self.window_LS)               
            self.window_LS.show()
            '''
            print("Not working for now")
        else:
            print("Box LS: Not checked ")    
            
            
    def uploadEmaphoto(self): 
        import imageio
        ema = imageio.imread("ema-animal.png")
        self.ui_MW.PyDMImageView_inicial.imageItem.setImage(image = ema[:,:,1], autoLevels = True)
        
    def setFlowControl_pvname(self):
        self.ui_pvnames.buttonBox.accepted.connect(self.acceptedChanges_pvname)
        self.ui_pvnames.buttonBox.rejected.connect(self.rejectedChanges_pvname)
    
    def getting_pvname(self):
        ''' PV names edition '''
        self.pvname_ocean = self.ui_pvnames.lineEdit_spec.text()
        self.pvname_motorGearBox = self.ui_pvnames.lineEdit_motor.text()
        self.pvname_lakeshore = self.ui_pvnames.lineEdit_LS.text()
    
    def acceptedChanges_pvname(self):
        ''' PV names edition '''
        try:
            self.getting_pvname()
            self.showDialog(title = 'Please Wait', text = 'Please Wait While E-MA Configures E-MA Application')
            self.ui_ocean.setFlowControl(oceanPV = self.pvname_ocean, motorPV = self.pvname_motorGearBox, LS = self.pvname_lakeshore)
        except OSError as err:
            self.showDialog(title = 'Error on PV names edition', text = err)
        
        self.Ui_MainWindow_editPVnames.close()
        
    def rejectedChanges_pvname(self):
        self.Ui_MainWindow_editPVnames.close()
            
    def showDialog(self,title = None, text = None):
        """Show a simple message dialog"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()  
        
if __name__ == '__main__':
    pass
    app = PyDMApplication(use_main_window=False)
    app.load_external_tools()
    ui_Dioptas = MainController() 
    emapp = EmaApp()
    sys.excepthook = excepthook
    sys.exit(app.exec_())
    QtWidgets.QApplication.closeAllWindows()