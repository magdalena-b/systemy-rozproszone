from thespian.actors import *
from message import Request, Report

class Dispatcher(ActorTypeDispatcher):

    def __init__(self):
        pass

    def receiveMsg_Request(self, message, sender):
        print("Received request with id " + str(message.query_id)) 

        for i in range(message.first_sat_id, message.first_sat_id + message.sat_range):
            try:
                # ActorSystem().ask(message.satellites[i], message.satelliteAPI, 0.001)
                self.send(message.satellites[i], message.satelliteAPI)
            except ActorSystemRequestTimeout:
                print("Error")


    def receiveMsg_Report(self, message, sender):
        print("Received report")
