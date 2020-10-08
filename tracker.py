from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import time
import json
import datetime
import sys
from os import system
from activity import *
# import win32gui
import uiautomation as auto

#Declarative Zone#



#Function Zone#



#EndZone#
while True:
    print(getActiveTimeWindow())
    time.sleep(1)