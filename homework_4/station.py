from thespian.actors import *
from message import *


class Station_Info():

    def __init__(self, station, name, query_counter):
        self.station = station
        self.name = name
        self.query_counter = query_counter


class Station(Actor):
    
    def __init__(self):
        print("Inited Station")
        self.report = Report()


    def receiveMessage(self, message, sender):
        if isinstance(message, Request):
            print("station got request")
            self.send(message.dispatcher, message)
        
        if isinstance(message, Report):
            print(message.station_info.name + " got a report:")
            print("Query = " + str(message.station_info.query_counter))
            print(message.error_map)
            
