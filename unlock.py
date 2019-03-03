#!/usr/bin/env python

'''farmware-unlock
'''

from farmware_tools import get_config_value, device
device.emergency_unlock()
device.log(message='farware-unlock exectued", message_type='success')
