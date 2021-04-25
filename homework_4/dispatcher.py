from thespian.actors import *
from message import Request, Report
from satellite import Satellite

import time

class Dispatcher(ActorTypeDispatcher):

    def receiveMsg_Request(self, message, sender):
        sat = self.createActor(Satellite)
        self.send(sat, message)


    def receiveMsg_Report(self, message, sender):
        message.end_time = time.time()
        message.execution_time = (message.end_time - message.start_time) * 1000
        print("Ex time = " + str(message.execution_time ) )
        self.send(message.station_info.station, message)