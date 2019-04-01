#!/usr/bin/env python3
import os
from qtpy.QtWidgets import QWidget, QDialog, QSizePolicy, QFrame, \
QGridLayout, QSpacerItem, QLineEdit, QPushButton, QWIDGETSIZE_MAX, QDoubleSpinBox, QLabel
from qtpy.QtGui import QColor, QFont
from qtpy.QtCore import Qt, QCoreApplication, Property
from qtpy import uic
from pydm.widgets.channel import PyDMChannel
from pydm.widgets import PyDMScaleIndicator, PyDMLabel, PyDMSymbol, \
PyDMPushButton, PyDMCheckbox, PyDMLineEdit, PyDMSpinbox
from pydm.utilities import macro
import yaml

if __name__ == '__main__':
    import sys
    from pydm import PyDMApplication    # For test

CONFIG_FIELDS_FILE = 'motor_fields_default.yml'
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))

class QMotorSettings(QDialog):
    '''
    A window to view/edit EPICS motor settings
    '''
    def __init__(self, parent, fields_map):
        super(QMotorSettings, self).__init__(parent)
        self.fields_map= fields_map
        self.ui = None
        self.on_edition = False

        self.load_ui()
        self.initialize_window()
        self.show()

    def get_ui_filename(self):
        return 'motor_settings.ui'

    def load_ui(self):
        f = macro.substitute_in_file(THIS_FOLDER + '/' + self.get_ui_filename(), self.fields_map)
        self.ui = uic.loadUi(f, baseinstance=self)

    def switch_edition_mode(self):
        current_mode = self.on_edition
        self.on_edition = not current_mode
        if self.on_edition:
            self.enable_edition()
        else:
            self.disable_edition()

    def enable_edition(self):
        self.ui.pushButton_switch.setText('Done')
        self.ui.groupBox_limits.setEnabled(True)
        self.ui.groupBox_motion.setEnabled(True)
        self.ui.groupBox_encoder.setEnabled(True)
        self.ui.groupBox_calibration.setEnabled(True)

    def disable_edition(self):
        self.ui.pushButton_switch.setText('Edit')
        self.ui.groupBox_limits.setEnabled(False)
        self.ui.groupBox_motion.setEnabled(False)
        self.ui.groupBox_encoder.setEnabled(False)
        self.ui.groupBox_calibration.setEnabled(False)

    def initialize_window(self):
        self.ui.listWidget.currentRowChanged.connect(self.ui.stackedWidget.setCurrentIndex)
        #self.ui.stackedWidget.currentChanged.connect(self.ui.listWidget.setCurrentRow)
        self.ui.pushButton_switch.clicked.connect(self.switch_edition_mode)

        # Initial state of settings dialog
        self.ui.listWidget.setCurrentRow(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.disable_edition()

    def closeEvent(self, event):
        '''
        When trying to close settings, just hide instead.
        '''
        event.ignore()
        self.disable_edition()
        self.hide()


class QMotor(QWidget):
    '''
    Widget based on EPICS motor record
    Details about motor record parameters are found at: https://www3.aps.anl.gov/bcda/synApps/motor/R6-9/motorRecord.html
    '''
    def __init__(self, parent=None, init_channel=None):
        super(QMotor, self).__init__(parent)
        self._channel = init_channel
        self.app = QCoreApplication.instance()
        self.ui = None
        self.settings_window = None
        self.config_fields_file = None
        self.fields_map = None
        self._orientation = Qt.Horizontal
        self._flipped = False
        self._inverted_scale = False

        self.setup_widgets()
        self.build_layout(self._orientation, self._flipped, self._inverted_scale)
        self.set_fields()
        self.load_images()
        self.set_all_channels(self._channel)
        self.show()
        self.repaint()

        #self.lineEdit_rlv.textEdited.connect(self.set_press_values)
        self.lineEdit_rlv.valueChanged.connect(self.set_press_values)
        self.pushButton_settings.clicked.connect(self.load_settings_ui)

    def init_for_designer(self):
        '''
        This is called by PyDM qtplugin_factory.
        If in QtDesigner, initialize all PyDM child widgets.
        '''
        widgets = self.findChildren(QWidget)
        for child_widget in widgets:
            try:
                child_widget.init_for_designer()
            except:
                pass

    def get_ui_filename(self):
        return 'motor_horizontal.ui'

    def setup_widgets(self):
        base_width = 55
        base_height = 26

        self.frame_motor = QFrame()
        self.frame_motor.setFrameShape(QFrame.StyledPanel)
        #Header
        self.widget_offset = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.widget_offset.setSizePolicy(sizePolicy)
        self.widget_offset.setFixedWidth(15)
        self.widget_offset.setMinimumHeight(base_height)

        label_font = QFont()
        label_font.setBold(True)

        self.PyDMLabel_desc = PyDMLabel()
        self.PyDMLabel_desc.setText('<DESC>')
        self.PyDMLabel_desc.setAlignment(Qt.AlignCenter)
        self.PyDMLabel_desc.setMinimumHeight(base_height)
        self.PyDMLabel_desc.setFont(label_font)

        self.pushButton_settings = QPushButton('⋮')
        self.pushButton_settings.setSizePolicy(sizePolicy)
        self.pushButton_settings.setFixedWidth(15)
        self.pushButton_settings.setMinimumHeight(base_height)

        # Control
        self.frame_controls = QFrame()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame_controls.setSizePolicy(sizePolicy)
        
        '''
        self.lineEdit_rlv = QLineEdit()
        self.lineEdit_rlv.setPlaceholderText('RLV')
        self.lineEdit_rlv.setAlignment(Qt.AlignCenter)
        '''
        self.lineEdit_rlv = QDoubleSpinBox()
        #self.lineEdit_rlv.setPlaceholderText('RLV')
        self.lineEdit_rlv.setAlignment(Qt.AlignCenter)
        self.lineEdit_rlv.setEnabled(True)
        self.lineEdit_rlv.setMinimumSize(2*base_width, base_height)
        self.lineEdit_rlv.setMinimum(-360.1)
        self.lineEdit_rlv.setMaximum(360.1)
        self.lineEdit_rlv.setSingleStep(0.1)
        
        self.PyDMLineEdit_val = PyDMLineEdit()
        self.PyDMLineEdit_val.alarmSensitiveBorder = False
        self.PyDMLineEdit_val.setPlaceholderText('VAL')
        self.PyDMLineEdit_val.setAlignment(Qt.AlignCenter)

        #self.PyDMPushButton_rlv_minus = PyDMPushButton('-')
        self.PyDMPushButton_rlv_minus = QLabel()
        self.PyDMPushButton_rlv_minus.setText('Step (°):')
        self.PyDMPushButton_rlv_minus.setMinimumSize(base_width, base_height)
        self.PyDMPushButton_rlv_minus.setEnabled(False)

        #self.PyDMPushButton_rlv_plus = PyDMPushButton('+')
        self.PyDMPushButton_rlv_plus = PyDMPushButton('Start')
        self.PyDMPushButton_rlv_plus.setMinimumSize(base_width, base_height)

        self.PyDMCheckbox_set = PyDMCheckbox()
        self.PyDMCheckbox_set.setText('SET')
        self.PyDMCheckbox_set.setLayoutDirection(Qt.RightToLeft)

        self.PyDMPushButton_stop = PyDMPushButton('STOP')
        self.PyDMPushButton_stop.setMinimumSize(base_width, base_height)
        self.PyDMPushButton_stop.pressValue = 1

        # Readback
        self.PyDMLabel_rbv = PyDMLabel()
        self.PyDMLabel_rbv.setText('<RBV>')
        self.PyDMLabel_rbv.setAlignment(Qt.AlignCenter)
        self.PyDMLabel_rbv.setFont(label_font)

        self.PyDMSymbol_lvio = PyDMSymbol()
        self.PyDMSymbol_lvio.setMinimumSize(base_height, base_height)
        size_fixed = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.PyDMSymbol_lvio.setSizePolicy(size_fixed)

        self.PyDMSymbol_movn = PyDMSymbol()
        self.PyDMSymbol_movn.setMinimumSize(base_height, base_height)
        self.PyDMSymbol_movn.setSizePolicy(size_fixed)

        # Scale
        self.scale = PyDMScaleIndicator()
        self.scale.showValue = False
        self.scale.showLimits = False
        self.scale.scaleHeight = 30
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scale.setSizePolicy(sizePolicy)

        self.PyDMLabel_llm = PyDMLabel()
        self.PyDMLabel_llm.setText('<LLM>')


        self.PyDMLabel_hlm = PyDMLabel()
        self.PyDMLabel_hlm.setText('<HLM>')

        self.PyDMSymbol_lls = PyDMSymbol()
        self.PyDMSymbol_lls.setMinimumSize(base_height, base_height)
        self.PyDMSymbol_lls.setSizePolicy(size_fixed)
        self.PyDMSymbol_athm = PyDMSymbol()
        self.PyDMSymbol_athm.setMinimumSize(base_height, base_height)
        self.PyDMSymbol_athm.setSizePolicy(size_fixed)
        self.PyDMSymbol_hls = PyDMSymbol()
        self.PyDMSymbol_hls.setMinimumSize(base_height, base_height)
        self.PyDMSymbol_hls.setSizePolicy(size_fixed)

        # Set name of objects for easily styling them with stylesheet
        # (when a ui is made in designer, this step is not needed)
        self.frame_motor.setObjectName('frame_motor')
        self.frame_controls.setObjectName('frame_controls')
        self.PyDMPushButton_stop.setObjectName('PyDMPushButton_stop')
        self.scale.setObjectName('scale')
        self.PyDMCheckbox_set.setObjectName('check_set')

    def build_layout(self, orientation, flipped, inverted):
        self.header_layout   = None
        self.control_layout  = None
        self.readback_layout = None
        self.scale_layout    = None
        self.motor_layout    = None
        self.top_layout      = None

        # Recreate spaces each time layout is rebuilt to prevent segfault
        # because they may be deleted by Python GC
        self.hspacer_lvio_left = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.hspacer_lvio_right = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.hspacer_movn_left = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.hspacer_movn_right = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.hspacer_llm = QSpacerItem(3, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.hspacer_hlm = QSpacerItem(3, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.vspacer_llm = QSpacerItem(0, 3, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.vspacer_hlm = QSpacerItem(0, 3, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)


        # Header
        self.header_layout = QGridLayout()

        # Control
        self.control_layout = QGridLayout()
        self.control_layout.setContentsMargins(1, 1, 1, 1)
        self.control_layout.setHorizontalSpacing(2)
        self.control_layout.setVerticalSpacing(2)

        # Readback
        self.readback_layout = QGridLayout()

        # Motor frame
        self.motor_layout = QGridLayout()
        self.motor_layout.setContentsMargins(1, 1, 1, 1)
        self.motor_layout.setHorizontalSpacing(2)
        self.motor_layout.setVerticalSpacing(3)

        # Scale
        self.setMaximumSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)
        self.scale_layout = QGridLayout()
        self.scale_layout.setContentsMargins(0, 0, 1, 1)
        self.scale_layout.setHorizontalSpacing(1)
        self.scale_layout.setVerticalSpacing(1)

        if self._orientation == Qt.Horizontal:
            self.header_layout.addWidget(self.widget_offset, 0, 0)
            self.header_layout.addWidget(self.PyDMLabel_desc, 0, 1)
            self.header_layout.addWidget(self.pushButton_settings, 0, 2)

            self.readback_layout.addItem(self.hspacer_lvio_left, 0, 0)
            self.readback_layout.addWidget(self.PyDMSymbol_lvio, 0, 1)
            self.readback_layout.addItem(self.hspacer_lvio_right, 0, 2)
            self.readback_layout.addWidget(self.PyDMLabel_rbv, 0, 3)
            self.readback_layout.addItem(self.hspacer_movn_left, 0, 4)
            self.readback_layout.addWidget(self.PyDMSymbol_movn, 0, 5)
            self.readback_layout.addItem(self.hspacer_movn_right, 0, 6)

            self.scale.orientation = Qt.Horizontal
            if flipped == False:
                self.scale.flipScale = False
                self.scale_layout.addWidget(self.scale, 0, 0, 1, 0)
                self.scale_layout.addWidget(self.PyDMSymbol_lls, 1, 1)
                self.scale_layout.addItem(self.hspacer_llm, 1, 2)
                self.scale_layout.addWidget(self.PyDMSymbol_athm, 1, 3)
                self.scale_layout.addItem(self.hspacer_hlm, 1, 4)
                self.scale_layout.addWidget(self.PyDMSymbol_hls, 1, 5)

                if inverted == False:
                    self.scale.invertedAppearance = False
                    self.scale_layout.addWidget(self.PyDMLabel_llm, 1, 0)
                    self.scale_layout.addWidget(self.PyDMLabel_hlm, 1, 6)
                    self.PyDMLabel_llm.setAlignment(Qt.AlignLeft|Qt.AlignTop)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignRight|Qt.AlignTop)
                elif inverted == True:
                    self.scale.invertedAppearance = True
                    self.scale_layout.addWidget(self.PyDMLabel_llm, 1, 6)
                    self.scale_layout.addWidget(self.PyDMLabel_hlm, 1, 0)
                    self.PyDMLabel_llm.setAlignment(Qt.AlignRight|Qt.AlignTop)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignLeft|Qt.AlignTop)

                self.control_layout.addWidget(self.PyDMPushButton_rlv_minus, 0, 0)
                self.control_layout.addWidget(self.lineEdit_rlv, 0, 1)
                self.control_layout.addWidget(self.PyDMPushButton_rlv_plus, 0, 2)
                self.control_layout.addWidget(self.PyDMCheckbox_set, 1, 0)
                self.control_layout.addWidget(self.PyDMLineEdit_val, 1, 1)
                self.control_layout.addWidget(self.PyDMPushButton_stop, 1, 2)

                self.motor_layout.addItem(self.header_layout, 0,0)
                self.motor_layout.addWidget(self.frame_controls, 1,0)
                self.motor_layout.addItem(self.readback_layout, 2,0)
                self.motor_layout.addItem(self.scale_layout, 3,0)

            elif flipped == True:
                self.scale.flipScale = True
                self.scale_layout.addWidget(self.scale, 1, 0, 1, 0)
                self.scale_layout.addWidget(self.PyDMSymbol_lls, 0, 1)
                self.scale_layout.addItem(self.hspacer_llm, 0, 2)
                self.scale_layout.addWidget(self.PyDMSymbol_athm, 0, 3)
                self.scale_layout.addItem(self.hspacer_hlm, 0, 4)
                self.scale_layout.addWidget(self.PyDMSymbol_hls, 0, 5)

                if inverted == False:
                    self.scale.invertedAppearance = False
                    self.scale_layout.addWidget(self.PyDMLabel_llm, 0, 0)
                    self.scale_layout.addWidget(self.PyDMLabel_hlm, 0, 6)

                    self.PyDMLabel_llm.setAlignment(Qt.AlignLeft|Qt.AlignBottom)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignRight|Qt.AlignBottom)
                elif inverted == True:
                    self.scale.invertedAppearance = True
                    self.scale_layout.addWidget(self.PyDMLabel_llm, 0, 6)
                    self.scale_layout.addWidget(self.PyDMLabel_hlm, 0, 0)
                    self.PyDMLabel_llm.setAlignment(Qt.AlignRight|Qt.AlignBottom)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignLeft|Qt.AlignBottom)

                self.control_layout.addWidget(self.PyDMCheckbox_set, 0, 0)
                self.control_layout.addWidget(self.PyDMLineEdit_val, 0, 1)
                self.control_layout.addWidget(self.PyDMPushButton_stop, 0, 2)
                self.control_layout.addWidget(self.PyDMPushButton_rlv_minus, 1, 0)
                self.control_layout.addWidget(self.lineEdit_rlv, 1, 1)
                self.control_layout.addWidget(self.PyDMPushButton_rlv_plus, 1, 2)

                self.motor_layout.addItem(self.scale_layout, 0,0)
                self.motor_layout.addItem(self.readback_layout, 1,0)
                self.motor_layout.addWidget(self.frame_controls, 2,0)
                self.motor_layout.addItem(self.header_layout, 3,0)

        elif self._orientation == Qt.Vertical:
            self.scale.orientation = Qt.Vertical
            if flipped == False:
                self.readback_layout.addItem(self.hspacer_lvio_left, 0, 0)
                self.readback_layout.addWidget(self.PyDMSymbol_lvio, 0, 1)
                self.readback_layout.addItem(self.hspacer_lvio_right, 0, 2)
                self.readback_layout.addWidget(self.PyDMLabel_rbv, 0, 3)
                self.readback_layout.addItem(self.hspacer_movn_left, 0, 4)
                self.readback_layout.addWidget(self.PyDMSymbol_movn, 0, 5)
                self.readback_layout.addItem(self.hspacer_movn_right, 0, 6)

                self.header_layout.addWidget(self.pushButton_settings, 0, 0)
                self.header_layout.addWidget(self.PyDMLabel_desc, 0, 1)
                self.header_layout.addWidget(self.widget_offset, 0, 2)

                self.scale.flipScale = False
                self.scale_layout.addWidget(self.scale, 0, 0, 5, 1)
                self.scale_layout.addItem(self.hspacer_llm, 0, 1, 5, 1)
                self.scale_layout.addWidget(self.PyDMSymbol_lls, 0, 2)
                self.scale_layout.addItem(self.vspacer_llm, 1, 2)
                self.scale_layout.addWidget(self.PyDMSymbol_athm, 2, 2)
                self.scale_layout.addItem(self.vspacer_hlm, 3, 2)
                self.scale_layout.addWidget(self.PyDMSymbol_hls, 4, 2)

                self.control_layout.addWidget(self.PyDMPushButton_rlv_plus, 0, 0)
                self.control_layout.addWidget(self.lineEdit_rlv, 1, 0)
                self.control_layout.addWidget(self.PyDMPushButton_rlv_minus, 2, 0)
                self.control_layout.addWidget(self.PyDMCheckbox_set, 0, 1, alignment=Qt.AlignCenter)
                self.control_layout.addWidget(self.PyDMLineEdit_val, 1, 1)
                self.control_layout.addWidget(self.PyDMPushButton_stop, 2, 1)

                self.motor_layout.addItem(self.header_layout, 0,0)
                self.motor_layout.addWidget(self.frame_controls, 1,0)
                self.motor_layout.addItem(self.readback_layout, 2,0)
                self.motor_layout.addItem(self.scale_layout, 1, 1)

                if inverted == False:
                    self.scale.invertedAppearance = False
                    self.motor_layout.addWidget(self.PyDMLabel_hlm, 0, 1)
                    self.motor_layout.addWidget(self.PyDMLabel_llm, 2, 1)
                    self.PyDMLabel_llm.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignHCenter|Qt.AlignBottom)
                elif inverted == True:
                    self.scale.invertedAppearance = True
                    self.motor_layout.addWidget(self.PyDMLabel_hlm, 2, 1)
                    self.motor_layout.addWidget(self.PyDMLabel_llm, 0, 1)
                    self.PyDMLabel_llm.setAlignment(Qt.AlignHCenter|Qt.AlignBottom)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

            elif flipped == True:
                self.readback_layout.addItem(self.hspacer_movn_left, 0, 0)
                self.readback_layout.addWidget(self.PyDMSymbol_movn, 0, 1)
                self.readback_layout.addItem(self.hspacer_movn_right, 0, 2)
                self.readback_layout.addWidget(self.PyDMLabel_rbv, 0, 3)
                self.readback_layout.addItem(self.hspacer_lvio_left, 0, 4)
                self.readback_layout.addWidget(self.PyDMSymbol_lvio, 0, 5)
                self.readback_layout.addItem(self.hspacer_lvio_right, 0, 6)

                self.header_layout.addWidget(self.widget_offset, 0, 0)
                self.header_layout.addWidget(self.PyDMLabel_desc, 0, 1)
                self.header_layout.addWidget(self.pushButton_settings, 0, 2)

                self.scale.flipScale = True
                self.scale_layout.addWidget(self.scale, 0, 1, 5, 1)
                self.scale_layout.addWidget(self.PyDMSymbol_lls, 0, 0)
                self.scale_layout.addItem(self.vspacer_llm, 1, 0)
                self.scale_layout.addWidget(self.PyDMSymbol_athm, 2, 0)
                self.scale_layout.addItem(self.vspacer_hlm, 3, 0)
                self.scale_layout.addWidget(self.PyDMSymbol_hls, 4, 0)

                self.control_layout.addWidget(self.PyDMCheckbox_set, 0, 0, alignment=Qt.AlignCenter)
                self.control_layout.addWidget(self.PyDMLineEdit_val, 1, 0)
                self.control_layout.addWidget(self.PyDMPushButton_stop, 2, 0)
                self.control_layout.addWidget(self.PyDMPushButton_rlv_plus, 0, 1)
                self.control_layout.addWidget(self.lineEdit_rlv, 1, 1)
                self.control_layout.addWidget(self.PyDMPushButton_rlv_minus, 2, 1)

                self.motor_layout.addItem(self.scale_layout, 1, 0)
                self.motor_layout.addItem(self.header_layout, 0,1)
                self.motor_layout.addWidget(self.frame_controls, 1,1)
                self.motor_layout.addItem(self.readback_layout, 2,1)

                if inverted == False:
                    self.scale.invertedAppearance = False
                    self.motor_layout.addWidget(self.PyDMLabel_hlm, 0, 0)
                    self.motor_layout.addWidget(self.PyDMLabel_llm, 2, 0)
                    self.PyDMLabel_llm.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignHCenter|Qt.AlignBottom)
                elif inverted == True:
                    self.scale.invertedAppearance = True
                    self.motor_layout.addWidget(self.PyDMLabel_hlm, 2, 0)
                    self.motor_layout.addWidget(self.PyDMLabel_llm, 0, 0)
                    self.PyDMLabel_llm.setAlignment(Qt.AlignHCenter|Qt.AlignBottom)
                    self.PyDMLabel_hlm.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        if self.frame_controls.layout() is not None:
            # Trick to remove the existing layout by re-parenting it in an empty widget.
            QWidget().setLayout(self.frame_controls.layout())
        self.frame_controls.setLayout(self.control_layout)

        if self.frame_motor.layout() is not None:
            QWidget().setLayout(self.frame_motor.layout())
        self.frame_motor.setLayout(self.motor_layout)

        # Top widget
        self.top_layout = QGridLayout()
        self.top_layout.addWidget(self.frame_motor, 0,0)
        self.top_layout.setContentsMargins(1, 1, 1, 1)
        self.top_layout.setHorizontalSpacing(2)
        self.top_layout.setVerticalSpacing(2)

        if self.layout() is not None:
            QWidget().setLayout(self.layout())
        self.setLayout(self.top_layout)

        self.adjustSize()

    def set_fields(self):
        if self.config_fields_file is None:
            self.config_fields_file = THIS_FOLDER + '/' +  CONFIG_FIELDS_FILE #Use fields default configuration

        with open(self.config_fields_file) as f:
            self.fields_map = yaml.load(f)

    def load_images(self):
        json_format = '{"0": "%s", "1": "%s"}'
        self.PyDMSymbol_lvio.imageFiles = json_format % (THIS_FOLDER + '/icons/exclamation0.svg', THIS_FOLDER + '/icons/exclamation1.svg')
        self.PyDMSymbol_movn.imageFiles = json_format % (THIS_FOLDER + '/icons/cached0.svg',      THIS_FOLDER + '/icons/cached1.svg')
        self.PyDMSymbol_lls.imageFiles  = json_format % (THIS_FOLDER + '/icons/exclamation0.svg', THIS_FOLDER + '/icons/exclamation1.svg')
        self.PyDMSymbol_athm.imageFiles = json_format % (THIS_FOLDER + '/icons/home0.svg',        THIS_FOLDER + '/icons/home1.svg')
        self.PyDMSymbol_hls.imageFiles  = json_format % (THIS_FOLDER + '/icons/exclamation0.svg', THIS_FOLDER + '/icons/exclamation1.svg')


    def load_ui(self):
        f = THIS_FOLDER + '/' + self.get_ui_filename()
        self.ui = uic.loadUi(f, baseinstance=self)
        self.load_images()

    def load_settings_ui(self):
        if self.settings_window != None:
            self.settings_window.show()
            self.settings_window.raise_()
            return
        self.fields_map['MOTOR'] = self._channel     # Add motor prefix to fields dict
        self.settings_window = QMotorSettings(parent=self, fields_map=self.fields_map)
        try:
            self.app.make_connections() # Connect settings window to PVs
        except:
            pass

    def set_press_values(self):
        self.PyDMPushButton_rlv_plus.updatePressValue(str(self.lineEdit_rlv.value()))
        #self.PyDMPushButton_rlv_plus.sendValue()
    
    def set_press_values_lais(self, value):
        self.PyDMPushButton_rlv_minus.pressValue = '-' + str(value)
        self.PyDMPushButton_rlv_plus.pressValue = str(value)

    def set_all_channels(self, channel):
        if channel is None:
            return
        # Monitors
        self.PyDMLabel_desc.channel           = channel + self.fields_map['DESC']
        self.PyDMLabel_rbv.channel            = channel + self.fields_map['RBV']
        self.PyDMSymbol_lvio.channel          = channel + self.fields_map['LVIO']
        self.PyDMSymbol_movn.channel          = channel + self.fields_map['MOVN']
        self.scale.channel                    = channel + self.fields_map['RBV']
        self.PyDMSymbol_athm.channel          = channel + self.fields_map['ATHM']
        self.PyDMSymbol_lls.channel           = channel + self.fields_map['LLS']
        self.PyDMSymbol_hls.channel           = channel + self.fields_map['HLS']
        self.PyDMLabel_hlm.channel            = channel + self.fields_map['HLM']
        self.PyDMLabel_llm.channel            = channel + self.fields_map['LLM']
        # Controls
        #self.PyDMPushButton_rlv_minus.channel = channel + self.fields_map['RLV']
        self.PyDMPushButton_rlv_plus.channel  = channel + self.fields_map['RLV']
        self.PyDMCheckbox_set.channel         = channel + self.fields_map['SET']
        self.PyDMLineEdit_val.channel         = channel + self.fields_map['VAL']
        self.PyDMPushButton_stop.channel      = channel + self.fields_map['STOP']
        # Icon tooltips
        self.PyDMSymbol_lvio.setToolTip(self.fields_map['LVIO_TOOLTIP'])
        self.PyDMSymbol_movn.setToolTip(self.fields_map['MOVN_TOOLTIP'])
        self.PyDMSymbol_lls.setToolTip(self.fields_map['LLS_TOOLTIP'])
        self.PyDMSymbol_athm.setToolTip(self.fields_map['ATHM_TOOLTIP'])
        self.PyDMSymbol_hls.setToolTip(self.fields_map['HLS_TOOLTIP'])

    @Property(str)
    def channel(self):
        """
        The channel address in use for this widget.

        Returns
        -------
        channel : str
            Channel address
        """
        return str(self._channel)

    @channel.setter
    def channel(self, value):
        """
        The channel address to use for this widget.

        Parameters
        ----------
        value : str
            Channel address
        """
        if self._channel != value:
            self._channel = str(value)
            self.set_all_channels(self._channel)

    @Property(Qt.Orientation)
    def orientation(self):
        """
        The orientation of the motor scale.

        Returns
        -------
        orientation : Qt.Orientation
            Orientation of the motor scale
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """
        The orientation of the motor scale.

        Parameters
        ----------
        orientation : Qt.Orientation
            Channel address
        """
        if self._orientation != orientation:
            self._orientation = orientation
            self.build_layout(orientation, self._flipped, self._inverted_scale)

    @Property(bool)
    def flipped(self):
        """
        Whether or not the motor layout is flipped.

        Returns
        -------
        bool
        """
        return self._flipped

    @flipped.setter
    def flipped(self, flipped):
        """
        Whether or not the motor layout is flipped.

        Parameters
        ----------
        flipped : bool
        """
        if self._flipped != flipped:
            self._flipped = flipped
            self.build_layout(self._orientation, flipped, self._inverted_scale)

    @Property(bool)
    def invertedScale(self):
        """
        Whether or not the motor scale is inverted.

        Returns
        -------
        bool
        """
        return self._inverted_scale

    @invertedScale.setter
    def invertedScale(self, inverted):
        """
        Whether or not the motor scale is inverted.

        Parameters
        ----------
        flipped : bool
        """
        if self._inverted_scale != inverted:
            self._inverted_scale = inverted
            self.build_layout(self._orientation, self._flipped, inverted)


if __name__ == '__main__':
    app = PyDMApplication(use_main_window=False)
    widget = QMotor(init_channel='ca://dmc:galil:test:A')
    app.establish_widget_connections(widget)
    sys.exit(app.exec_())
