#!/usr/bin/env python

'''farmware-unlock
'''

from farmware_tools import device
device.emergency_unlock()
device.log(message='farware-unlock exectued', message_type='success')
