#Tracker powered by Zero more info in github
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import time
import json
import datetime
import sys
from os import system
from activity import *
import uiautomation as auto
# Development os block
windowsOS = ['Windows','win32','cygwin']
macOS = ['Mac','darwin','os2','os2emx']
linuxOS = ['linux','linux2']
# Development os block
""" Maybe i'll add another os compatibility like macOS and linux"""

""" Declarative Zone """

activeWindowName = ""
activityName = ""
startTime = datetime.datetime.now()
first_time = True #First time running?


""" Function Zone """

def gettingActiveWindow():
    """We gonna get the info about the active on-time window"""
    
    activeWindowName = None
    if sys.platform in []:
        pass






""" EndZone """

print(gettingActiveWindow())