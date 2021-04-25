from thespian.actors import *
from message import Request, Report

class Dispatcher(ActorTypeDispatcher):

    def __init__(self):
        pass

    def receiveMsg_Request(self, message, sender):
        print("Received request with id " + str(message.station_info.query_counter)) 
        self.send(message.satellite, message)


    def receiveMsg_Report(self, message, sender):
        print("Dispatcher received report")
        self.send(message.station_info.station, message)