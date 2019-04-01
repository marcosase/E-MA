from pydm.widgets.qtplugin_base import qtplugin_factory
from .motor import QMotor

WIDGET_CATEGORY = 'SOL Widgets'

QMotorPlugin = qtplugin_factory(QMotor, group=WIDGET_CATEGORY)