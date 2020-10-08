from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import time
import json
import datetime
import sys
from os import system
from activity import *
import uiautomation as auto
if sys.platform in ['Windows','win32','cygwin']:
    pass #Pass for now

""" Declarative Zone """

activeWindowName = ""
activityName = ""
startTime = datetime.datetime.now()
first_time = True #First time running?

""" Function Zone """



""" EndZone """

print(startTime)