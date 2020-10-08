import datetime
import json
from dateutil import parser

class Activity:
    """ This class will make the activity instance obj"""
    def __init__(self, name, time):
        self.name = name # This constructor gon' catch the name of the window already open
        self.time = time #This constructor gon' catch the time catched

class TimeEntry:
    """ This class will make the time entry instance obj"""
    def __init__(self, start_time, end_time, days, hours, minutes, seconds):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = start_time - end_time
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
