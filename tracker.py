""" Tracker powered by Zero
    Some issue or problem? Write a message in ZeroSeventty@gmail.com
"""

from __future__ import print_function
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import time
import json
import datetime
import sys
import requests
from os import system
import subprocess
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
start_time = datetime.datetime.now() #First time instance
activeList = AcitivyList([]) # First instance
first_time = True #First time


""" Function Zone """

def gettin_active_window():
    """We gonna get the info about the active on-time window"""
    
    _active_window_name = None
    if sys.platform in windowsOS:
        window = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(window)
        buff = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(window, buff, length + 1)
        _active_window_name = buff.value
    else:
        print(f"Script not supported in {sys.platform} contact an administrator.")

    return _active_window_name


""" Catch no-json with any error jumps """
try:
    activeList.initialize_me()
except Exception:
    print('Endpoint json, creating one...') #it create a json file if it not exists in the instance running

def post():
    subprocess.call('node post.js', shell=True)

""" Engine of the timer """
try:
    while True:
        try:
            previous_site = ""
            if sys.platform not in linuxOS:
                new_window_name = gettin_active_window()

            if active_window_name != new_window_name:
                print(active_window_name)
                activity_name = active_window_name

                if not first_time:
                    end_time = datetime.datetime.now()
                    time_entry = TimeEntry(start_time, end_time,0,0,0,0)
                    time_entry._get_specific_times()    
                    exists = False
                    for registrer in activeList.activities:
                        if registrer.name == activity_name:
                            exists = True
                            registrer.time_entries.append(time_entry)

                    if not exists:
                        registrer = Activity(activity_name, [time_entry])
                        activeList.activities.append(registrer)
                    with open('endpoint.json','w') as json_file:
                        json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
                        start_time = datetime.datetime.now()

                first_time = False
                active_window_name = new_window_name
                time.sleep(10)
                post()
        except Exception as e:
            f = open("log.txt","a")
            f.write(f"Error log catch an error called: {str(e)} {datetime.datetime.now()}")
            continue #Catch the error if isn't keyboardInterrupt and run again.
except KeyboardInterrupt: 
    print("Timer stopped")
"""Keyboard exception crlt c or z"""
