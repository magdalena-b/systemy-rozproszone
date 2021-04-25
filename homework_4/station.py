from thespian.actors import *
from message import *


class Station_Info():

    def __init__(self, station, name, query_counter):
        self.station = station
        self.name = name
        self.query_counter = query_counter


class Station(Actor):
    
    def receiveMessage(self, message, sender):
        if isinstance(message, Request):
            self.send(message.dispatcher, message)
        
        if isinstance(message, Report):
            print(message.station_info.name + " got a report:")
            print("Query = " + str(message.station_info.query_counter))
            print("Execution time = " + str(message.execution_time))
            print("Percent = " + str(message.percent))
            print(message.error_map)
            print("\n\n")

        if isinstance(message, int):
            sat_id = str(message)
            f = open("db.txt", "r")
            lines = f.readlines()
            f.close()
            
            for line in lines:
                if sat_id in line:
                    error_counter = line.split()[1]
                    if int(error_counter) > 0:
                        print("_______________ERROR COUNTER FOR " + sat_id + " IS " + error_counter) 




            