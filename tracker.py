#Tracker powered by Zero more info in github
from __future__ import print_function
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import time
import json
import datetime
import sys
from os import system
from registrer import *

# Development os block
windowsOS = ['Windows','win32','cygwin']
macOS = ['Mac','darwin','os2','os2emx']
linuxOS = ['linux','linux2']
# Development os block
""" Maybe i'll add another os compatibility like macOS and linux"""

""" Declarative Zone """

active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
activeList = ActivityList([])
first_time = True #First time running?


""" Function Zone """

def gettingActiveWindow():
    """We gonna get the info about the active on-time window"""
    
    active_window_name_ = None
    if sys.platform in windowsOS:
        window = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(window)
        buff = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(window, buff, length + 1)
        if buff.value:
            active_window_name_ = buff.value
            return active_window_name_
        else:
            active_window_name_ = None
    else:
        print(f"{sys.platform} isn't supported yet, contact an administrator.")
        return active_window_name_


""" Catch no-json with any error jumps """
try:
    activeList.initialize_me()
except Exception:
    print('No json')



""" EndZone """
print("script seek each 5 secs the task that you're working on\n")
while True:
    print(gettingActiveWindow())
    time.sleep(2)
    

""" Working at this point """    








"""Keyboard exception crlt c or z"""
