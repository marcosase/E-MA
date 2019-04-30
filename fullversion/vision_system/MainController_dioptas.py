from __future__ import absolute_import
# The above line is related to excepthook
'''
Created on Jun 8, 2018

@author: rodrigo.guercio
There are some notes that are on report of intership 

For example:
    [1] At Dioptas/Dioptas/tree/develop/dioptas/controller/integration/ImageController.py
        It was necessary to comment line 169: #self.connect_click_function(self.widget.qa_save_img_btn, self.save_img)
    [2] Bug of Cosmic Removal
'''
# -*- coding: utf8 -*-
# Dioptas - GUI program for fast processing of 2D X-ray data
# Copyright (C) 2017  Clemens Prescher (clemens.prescher@gmail.com)
# Institute for Geology and Mineralogy, University of Cologne
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import json
from sys import platform as _platform

from qtpy import QtWidgets, QtCore

from dioptas.widgets.MainWidget import MainWidget
from dioptas.model.DioptasModel import DioptasModel
from dioptas.widgets.UtilityWidgets import save_file_dialog, open_file_dialog

from dioptas.controller import CalibrationController
from dioptas.controller.integration import IntegrationController
from dioptas.controller.MaskController import MaskController
from dioptas.controller.ConfigurationController import ConfigurationController

from dioptas import __version__


class MainController(object):
    """
    Creates a the main controller for Dioptas. Creates all the data objects and connects them with the other controllers
    """

    def __init__(self, use_settings=True, settings_directory='default'):

        self.use_settings = use_settings
        self.widget = MainWidget()
        #Changing
        self.capture_image_sample_btn = QtWidgets.QPushButton('Capture the sample image')
        self.capture_image_sample_btn.setStyleSheet("color: rgb(0, 255, 255);")
        self.capture_image_sample_btn.setMaximumSize(QtCore.QSize(190, 600))
        self.widget.integration_widget.integration_control_widget.img_control_widget._layout.addWidget(self.capture_image_sample_btn)
        
        self.capture_image_calibration_btn = QtWidgets.QPushButton('Capture the sample image')
        self.capture_image_calibration_btn.setStyleSheet("color: rgb(0, 255, 255);")
        self.capture_image_calibration_btn.setMaximumSize(QtCore.QSize(190, 600))
        self.widget.calibration_widget.calibration_control_widget._file_layout.addWidget(self.capture_image_calibration_btn)
        # create data
        if settings_directory == 'default':
            self.settings_directory = os.path.join(os.path.expanduser("~"), '.Dioptas')
        else:
            self.settings_directory = settings_directory

        self.model = DioptasModel()

        self.calibration_controller = CalibrationController(self.widget.calibration_widget,
                                                            self.model)
        self.mask_controller = MaskController(self.widget.mask_widget,
                                              self.model)
        self.integration_controller = IntegrationController(self.widget.integration_widget,
                                                            self.model)

        self.configuration_controller = ConfigurationController(
            configuration_widget=self.widget.configuration_widget,
            dioptas_model=self.model,
            controllers=[
                self.calibration_controller,
                self.mask_controller,
                self.integration_controller,
                self
            ]
        )
        
        ''' Changed by rmguercio '''
        self.widget.calibration_mode_btn.setText('Calibrate standard image')
        self.widget.mask_mode_btn.setText('Mask the image of sample')
        self.widget.integration_mode_btn.setText('Integrate image sample')
        self.widget.setMinimumSize(1024,768)
        #self.widget.maximumSize()
        self._create_windows() #R Guercio
        self.create_signals()
        self._create_signals() # R Guercio
        self.update_title()
        self.bug_fault() #R Guercio
        ''' Changed by rmguercio 

        if use_settings:
            self.load_default_settings()
            self.setup_backup_timer()
        '''

        self.current_tab_index = 0
        
    def bug_fault(self):
        ''' Disabling some functionalities '''
        ''' Cosmic removal button should be disabled '''
        self.mask_controller.widget.cosmic_btn.setEnabled(False)
        ''' Enable Calibrate button when one peak was selected by yser '''
        self.calibration_controller.widget.calibrate_btn.setEnabled(False)
        self.calibration_controller.widget.img_widget.mouse_left_clicked.connect(self.setEnableCalibrateBtn)
        
    def setEnableCalibrateBtn(self):
        self.calibration_controller.widget.calibrate_btn.setEnabled(True)

    def show_window(self):
        """
        Displays the main window on the screen and makes it active.
        """
        self.widget.show()
        
        if _platform == "darwin":
            self.widget.setWindowState(self.widget.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
            self.widget.activateWindow()
            self.widget.raise_()
            
        ''' Changed by rmguercio '''
        self._set_iparams()
            
    def create_signals(self):
        """
        Creates subscriptions for changing tabs and also newly loaded files which will update the title of the main
                window.
        """
        self.widget.tabWidget.currentChanged.connect(self.tab_changed)
        self.widget.closeEvent = self.close_event
        self.widget.show_configuration_menu_btn.toggled.connect(self.widget.configuration_widget.setVisible)

        self.widget.calibration_mode_btn.toggled.connect(self.widget.calibration_widget.setVisible)
        self.widget.mask_mode_btn.toggled.connect(self.widget.mask_widget.setVisible)
        self.widget.integration_mode_btn.toggled.connect(self.widget.integration_widget.setVisible)

        self.widget.mode_btn_group.buttonToggled.connect(self.tab_changed)

        self.model.img_changed.connect(self.update_title)
        self.model.pattern_changed.connect(self.update_title)

        self.widget.save_btn.clicked.connect(self.save_btn_clicked)
        self.widget.load_btn.clicked.connect(self.load_btn_clicked)
        self.widget.reset_btn.clicked.connect(self.reset_btn_clicked)
        
        ''' Some code done by R Guercio ''' 

    def _create_windows(self):  
        ''' Interfaces done on pyqt5 - qt designer 5 '''
        from vision_system.interface_askCaptureImage_calib import Ui_MainWindow_askCalibCCD
        from vision_system.ui_marccd import ui_marccd 
        'Interface_askCaptureImage_calib'
        self.window_askmarccd = QtWidgets.QMainWindow()
        self.ui_askmarccd = Ui_MainWindow_askCalibCCD()
        self.ui_askmarccd.setupUi(self.window_askmarccd)
        'Interface_ccd_marccd'
        self.window_marccd = QtWidgets.QMainWindow()
        self.ui_marccd = ui_marccd()
        self.ui_marccd.setupUi(self.window_marccd)
        self.ui_marccd.setFlowControl()
        
        
    def _create_signals(self):
        'Signals to new windows on pyqt5'  
        self.widgetflag = 0  
        self.capture_image_calibration_btn.clicked.connect(self.tab_changed_rmg_v1)
        self.capture_image_sample_btn.clicked.connect(self.tab_changed_rmg_v2) #toggled.connect(self.tab_changed_rmg)
        ''' Signals: Ask if the user wants to capture! '''
        #CALIBRATION and INTEGRATION
        self.ui_askmarccd.PyDMPushButton_YES.clicked.connect(self.open_calibInterface)
        self.ui_askmarccd.PyDMPushButton_NO.clicked.connect(self.window_askmarccd.close) 
        self.ui_askmarccd.PyDMPushButton_YES.clicked.connect(self.window_askmarccd.close)
        ''' There is a new image saved on computer '''
        self.ui_marccd.marccd.signal.connect(self.displayImageOnDioptas)
        
    def _set_iparams(self):
        ''' Set inicial params to MarCCD'''
        ''' Search PEAk '''
        self.widget.calibration_widget.automatic_peak_num_inc_cb.setChecked(False)
        self.widget.calibration_widget.automatic_peak_search_rb.setChecked(False)
        self.widget.calibration_widget.select_peak_rb.setChecked(True)
        ''' Inicial params'''
        self.widget.calibration_widget.calibration_control_widget.calibration_parameters_widget.start_values_gb.distance_cb.setChecked(False)
        self.widget.calibration_widget.calibration_control_widget.calibration_parameters_widget.start_values_gb.wavelength_cb.setChecked(True)
        
        
    def displayImageOnDioptas(self,imagesaved):
        if (imagesaved == 'False'):
            print('ERROR: Image was not saved and it wont be displayed') 
            if (self.ui_marccd.marccd.isRunning()):
                self.ui_marccd.marccd.terminate() ## self.ui_marccd.marccd.finished()
        else:
            print('Displaying image on Dioptas')
            if self.widgetflag == 0:
                self.calibration_controller.model.working_directories['image'] = os.path.dirname(imagesaved)
                self.calibration_controller.model.img_model.load(imagesaved)
            elif self.widgetflag == 2:
                self.integration_controller.model.working_directories['image'] = os.path.dirname(imagesaved)
                self.integration_controller.model.img_model.load(imagesaved)
            else:
                print ('ErroooRRRodrigo')
            if (self.ui_marccd.marccd.isRunning()):
                self.ui_marccd.marccd.terminate() ## self.ui_marccd.marccd.finished()
            print('Is the marccd thread is keeping active ? True or False: ',self.ui_marccd.marccd.isRunning())
            print('Is the display thread is keeping active ? True or False: ',self.ui_marccd.timeleft.isRunning())
            #self.window_marccd.close()
    
    def open_calibInterface(self): 
        
        if self.window_marccd.isVisible():
            self.window_marccd.close()
        
        if self.widgetflag == 0:
            self.ui_marccd.ui.PyDMPushButton_imagesequence.setText("Capture calibration image")
            self.window_marccd.show() 
        elif self.widgetflag == 2:
            self.ui_marccd.ui.PyDMPushButton_imagesequence.setText("Capture single image")
            self.window_marccd.show() 
        else:
            print('ERROR  => RODRIGO')
            
            
    def open_interfaceTocaptureImage(self):
        self.open_calibInterface()
        
        
    def tab_changed_rmg_v1(self):
    
        if self.window_askmarccd.isVisible():
            self.window_askmarccd.close()
        
        if self.widget.calibration_mode_btn.isChecked():
            self.widgetflag = 0
            #self.window_askmarccd.show() #Do you want calibration?
            self.open_calibInterface()
        elif self.widget.mask_mode_btn.isChecked():
            self.widgetflag = 1
        elif self.widget.integration_mode_btn.isChecked():
            self.widgetflag = 2
            #self.window_askmarccd.show() #Don't show anymore - Integration
            self.open_calibInterface()
        else:
            print("Hi")  
            
    def tab_changed_rmg_v2(self):
    
        if self.window_askmarccd.isVisible():
            self.window_askmarccd.close()
        
        if self.widget.calibration_mode_btn.isChecked():
            self.widgetflag = 0
            #self.window_askmarccd.show() #Do you want calibration?
            self.open_calibInterface()
        elif self.widget.mask_mode_btn.isChecked():
            self.widgetflag = 1
        elif self.widget.integration_mode_btn.isChecked():
            self.widgetflag = 2
            #self.window_askmarccd.show() #Don't show anymore - Integration
            self.open_calibInterface()
        else:
            print("Hi")  
   

    def tab_changed(self):
        """
        Function which is called when a tab has been selected (calibration, mask, or integration). Performs
        needed initialization tasks.
        :return:
        """
        if self.widget.calibration_mode_btn.isChecked():
            ind = 0
        elif self.widget.mask_mode_btn.isChecked():
            ind = 1
        elif self.widget.integration_mode_btn.isChecked():
            ind = 2
        else:
            return

        old_index = self.current_tab_index
        self.current_tab_index = ind

        # get the old view range
        old_view_range = None
        old_hist_levels = None
        if old_index == 0:  # calibration tab
            old_view_range = self.widget.calibration_widget.img_widget.img_view_box.targetRange()
            old_hist_levels = self.widget.calibration_widget.img_widget.img_histogram_LUT_horizontal.getExpLevels()
        elif old_index == 1:  # mask tab
            old_view_range = self.widget.mask_widget.img_widget.img_view_box.targetRange()
            old_hist_levels = self.widget.mask_widget.img_widget.img_histogram_LUT_horizontal.getExpLevels()
        elif old_index == 2:
            old_view_range = self.widget.integration_widget.img_widget.img_view_box.targetRange()
            old_hist_levels = self.widget.integration_widget.img_widget.img_histogram_LUT_horizontal.getExpLevels()

        # update the GUI
        if ind == 2:  # integration tab
            self.model.mask_model.set_supersampling()
            self.integration_controller.image_controller.plot_mask()
            self.integration_controller.widget.calibration_lbl.setText(self.model.calibration_model.calibration_name)
            self.integration_controller.image_controller._auto_scale = False

            if self.widget.integration_widget.img_mode == "Image":
                self.integration_controller.image_controller.plot_img()

            if self.model.use_mask:
                self.model.current_configuration.integrate_image_1d()
                if self.model.current_configuration.auto_integrate_cake:
                    self.model.current_configuration.integrate_image_2d()
            else:
                self.model.pattern_changed.emit()
            self.widget.integration_widget.img_widget.set_range(x_range=old_view_range[0], y_range=old_view_range[1])
            self.widget.integration_widget.img_widget.img_histogram_LUT_horizontal.setLevels(*old_hist_levels)
            self.widget.integration_widget.img_widget.img_histogram_LUT_vertical.setLevels(*old_hist_levels)
        elif ind == 1:  # mask tab
            self.mask_controller.plot_mask()
            self.mask_controller.plot_image()
            self.widget.mask_widget.img_widget.set_range(x_range=old_view_range[0], y_range=old_view_range[1])
            self.widget.mask_widget.img_widget.img_histogram_LUT_vertical.setLevels(*old_hist_levels)
        elif ind == 0:  # calibration tab
            self.calibration_controller.plot_mask()
            try:
                self.calibration_controller.update_calibration_parameter_in_view()
            except (TypeError, AttributeError):
                pass
            self.widget.calibration_widget.img_widget.set_range(x_range=old_view_range[0], y_range=old_view_range[1])
            self.widget.calibration_widget.img_widget.img_histogram_LUT_vertical.setLevels(*old_hist_levels)

    def update_title(self):
        """
        Updates the title bar of the main window. The title bar will always show the current version of Dioptas, the
        image or pattern filenames loaded and the current calibration name.
        """
        img_filename = os.path.basename(self.model.img_model.filename)
        pattern_filename = os.path.basename(self.model.pattern.filename)
        calibration_name = self.model.calibration_model.calibration_name
        str = 'Dioptas ' + __version__
        if img_filename is '' and pattern_filename is '':
            self.widget.setWindowTitle(str + u' - © 2019 C. Prescher modified by 2018 Guercio R')
            self.widget.integration_widget.img_frame.setWindowTitle(str + u' - © 2019 C. Prescher')
            return

        if img_filename is not '' or pattern_filename is not '':
            str += ' - ['
        if img_filename is not '':
            str += img_filename
        elif img_filename is '' and pattern_filename is not '':
            str += pattern_filename
        if not img_filename == pattern_filename:
            str += ', ' + pattern_filename
        if calibration_name is not None:
            str += ', calibration: ' + calibration_name
        str += ']'
        str += u' - © 2019 C. Prescher'
        self.widget.setWindowTitle(str)
        self.widget.integration_widget.img_frame.setWindowTitle(str)

    def save_default_settings(self):
        if not os.path.exists(self.settings_directory):
            os.mkdir(self.settings_directory)
        self.model.save(os.path.join(self.settings_directory, 'config.dio'))

    def load_default_settings(self):
        config_path = os.path.join(self.settings_directory, 'config.dio')
        if os.path.isfile(config_path):
            self.show_window()
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self.widget,
                                                                           'Recovering previous state.',
                                                                           'Should Dioptas recover your previous Work?',
                                                                           QtWidgets.QMessageBox.Yes,
                                                                           QtWidgets.QMessageBox.No):
                self.model.load(os.path.join(self.settings_directory, 'config.dio'))
            else:
                self.load_directories()

    def setup_backup_timer(self):
        self.backup_timer = QtCore.QTimer(self.widget)
        self.backup_timer.timeout.connect(self.save_default_settings)
        self.backup_timer.setInterval(600000)  # every 10 minutes
        self.backup_timer.start()

    def save_directories(self):
        """
        Currently used working directories for images, spectra, etc. are saved as csv file in the users directory for
        reuse when Dioptas is started again without loading a configuration
        """
        working_directories_path = os.path.join(self.settings_directory, 'working_directories.json')
        json.dump(self.model.working_directories, open(working_directories_path, 'w'))

    def load_directories(self):
        """
        Loads previously used Dioptas directory paths.
        """
        working_directories_path = os.path.join(self.settings_directory, 'working_directories.json')
        if os.path.exists(working_directories_path):
            self.model.working_directories = json.load(open(working_directories_path, 'r'))

    def close_event(self, ev):
        """
        Intervention of the Dioptas close event to save settings before closing the Program.
        """
        if self.use_settings:
            self.save_default_settings()
            self.save_directories()
        #QtWidgets.QApplication.closeAllWindows()
        ev.accept()

    def save_btn_clicked(self):
        try:
            default_file_name = os.path.join(self.model.working_directories['project'], 'config.dio')
        except (TypeError, KeyError):
            default_file_name = '.'
        filename = save_file_dialog(self.widget, "Save Current Dioptas Project", default_file_name,
                                    filter='Dioptas Project (*.dio)')

        if filename is not None and filename != '':
            self.model.save(filename)
            self.model.working_directories['project'] = os.path.dirname(filename)

    def load_btn_clicked(self):
        try:
            default_file_name = os.path.join(self.model.working_directories['project'], 'config.dio')
        except (TypeError, KeyError):
            default_file_name = '.'
        filename = open_file_dialog(self.widget, "Load a Dioptas Project", default_file_name,
                                    filter='Dioptas Project (*.dio)')
        if filename is not None and filename != '':
            self.model.load(filename)
            self.model.working_directories['project'] = os.path.dirname(filename)

    def reset_btn_clicked(self):
        if QtWidgets.QMessageBox.Yes == \
                QtWidgets.QMessageBox.question(self.widget,
                                               'Resetting Dioptas.',
                                               'Do you really want to reset Dioptas?\nAll unsaved work will be lost!',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No):
            self.model.reset()
        if QtWidgets.QMessageBox.Yes == \
                QtWidgets.QMessageBox.question(self.widget,
                                               'Resetting Dioptas.',
                                               'Do you really want to reset Dioptas?\nAll unsaved work will be lost!',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No):
            self.model.reset()


# -*- coding: utf8 -*-
# Dioptas - GUI program for fast processing of 2D X-ray data
# Copyright (C) 2017  Clemens Prescher (clemens.prescher@gmail.com)
# Institute for Geology and Mineralogy, University of Cologne
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



from dioptas._version import get_versions

__version__ = get_versions()['version']
del get_versions

if __version__ == "0+unknown":
    __version__ = "0.4.0"

import time

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import traceback
dioptas_version = __version__[:5]

resources_path = os.path.join(os.path.dirname(__file__), 'resources')
calibrants_path = os.path.join(resources_path, 'calibrants')
icons_path = os.path.join(resources_path, 'icons')
data_path = os.path.join(resources_path, 'data')
style_path = os.path.join(resources_path, 'style')


from dioptas.widgets.UtilityWidgets import ErrorMessageBox


def excepthook(exc_type, exc_value, traceback_obj):
    """
    Global function to catch unhandled exceptions. This function will result in an error dialog which displays the
    error information.
    :param exc_type: exception type
    :param exc_value: exception value
    :param traceback_obj: traceback object
    :return:
    """

    separator = '-' * 80
    log_file = "error.log"
    notice = \
        """An unhandled exception occurred. Please report the bug under:\n """ \
        """\t%s\n""" \
        """or via email to:\n\t <%s>.\n\n""" \
        """A log has been written to "%s".\n\nError information:\n""" % \
        ("https://github.com/Dioptas/Dioptas/issues",
         "clemens.prescher@gmail.com",
         os.path.join(os.path.dirname(__file__), log_file))
    version_info = '\n'.join((separator, "Dioptas Version: %s" % dioptas_version))
    time_string = time.strftime("%Y-%m-%d, %H:%M:%S")
    tb_info_file = StringIO()
    traceback.print_tb(traceback_obj, None, tb_info_file)
    tb_info_file.seek(0)
    tb_info = tb_info_file.read()
    errmsg = '%s: \n%s' % (str(exc_type), str(exc_value))
    sections = [separator, time_string, separator, errmsg, separator, tb_info]
    msg = '\n'.join(sections)
    try:
        f = open(log_file, "w")
        f.write(msg)
        f.write(version_info)
        f.close()
    except IOError:
        pass
    errorbox = ErrorMessageBox()
    errorbox.setText(str(notice) + str(msg) + str(version_info))
    errorbox.exec_()