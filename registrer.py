import datetime
import json
from dateutil import parser

class Activity:
    """ Activity name/time driver """
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'name':self.name,
            'time_entries':self.make_time_entires_to_json()
        }

    def make_time_entires_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list
    

class TimeEntry():
    """Time format driver"""
    """ Time constructor"""
    def __init__(self, start_time, end_time, days, hours, minutes, seconds):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = start_time - end_time
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    """ Time formater thx stackoverflow"""
    def get_specific_times(self):
        self.days, self.seconds = self.total_time.days, self.total_time.seconds
        self.hours = self.days * 24 + self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 60

    """ Serialize whole the time tracked"""
    def serialize(self):
        return {
            'start_time':self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'days' : self.days,
            'hours' : self.hours,
            'minutes' : self.minutes,
            'seconds' : self.seconds
        }