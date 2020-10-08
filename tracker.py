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
    if sys.platform in windowsOS:
        window = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(window)
        buff = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(window, buff, length + 1)
        if buff.value:
            activeWindowName = buff.value
            return activeWindowName
        else:
            activeWindowName = None
    else:
        print(f"{sys.platform} isn't supported yet, contact an administrator.")
        return activeWindowName



""" EndZone """
print("script seek each 5 secs the task that you're working on\n")
while True:
    print(gettingActiveWindow())
    time.sleep(5)
    

""" Working at this point """    








"""Keyboard exception crlt c or z"""
