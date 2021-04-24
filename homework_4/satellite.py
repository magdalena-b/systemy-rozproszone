from thespian.actors import *
from satelliteAPI import SatelliteAPI





class Satellite(Actor):

    id: int
    satAPI: SatelliteAPI

    def __init__(self, id):
        self.id = id
        self.satAPI = SatelliteAPI()


    def receiveMsg_Request(self, message, sender):
        pass
        