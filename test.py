from datetime import datetime
a={}
def minute(s:str):
    h, m= s.split(':')
    return int(h)*60 + m

class tp:
    def __init__(self, name, start, end, m)->None:
        self.name= name
        self.start= start
        self.end= end
        self.m= m
        self.time= minute(end) - minute(start)