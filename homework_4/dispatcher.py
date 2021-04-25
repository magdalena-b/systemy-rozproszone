from thespian.actors import *
from message import Request, Report
from satellite import Satellite

class Dispatcher(ActorTypeDispatcher):

    def receiveMsg_Request(self, message, sender):
        sat = self.createActor(Satellite)
        self.send(sat, message)


    def receiveMsg_Report(self, message, sender):
        self.send(message.station_info.station, message)