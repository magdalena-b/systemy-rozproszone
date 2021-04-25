from thespian.actors import *
from message import Request, Report

class Dispatcher(ActorTypeDispatcher):

    def __init__(self):
        pass

    def receiveMsg_Request(self, message, sender):
        self.send(message.satellite, message)


    def receiveMsg_Report(self, message, sender):
        self.send(message.station_info.station, message)