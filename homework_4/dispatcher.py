from thespian.actors import *
from message import Request, Report

class Dispatcher(ActorTypeDispatcher):

    def __init__(self):
        pass

    # receive msg from station
    def receiveMsg_Request(self, message, sender):
        print("Received request with id " + str(message.query_id)) 

        sats = message.satellites
        query_id = message.query_id
        first_id = message.first_sat_id
        sat_range = message.sat_range
        timeout = message.timeout
        satAPI = message.satelliteAPI

        for i in range(first_id, first_id + sat_range):
            ActorSystem().ask(message.satellites[i], 'Hi', 0.5)



    # send msg to satellite
    def receiveMsg_Report(self, message, sender):
        print("Received report")

    # receive msg from satellite
    
    # senf msg to station