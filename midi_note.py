""" CONTAINS THE NOTE OBJECT TO BE USED IN OTHER MODULES 
"""
from numpy import zeros

class Note():
    duration = -1
    stop_time = -1
    def __init__(self,type,channel,note,velocity,time,start_time):
        self.type = type
        self.channel = channel
        self.note = note
        self.velocity = velocity
        self.time = time
        self.start_time = start_time
    
    def to_numpy(self):
        v = zeros(129)
        v[self.note] = 1
        return v