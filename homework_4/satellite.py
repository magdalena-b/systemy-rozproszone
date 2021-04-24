from thespian.actors import *
from satelliteAPI import SatelliteAPI





class Satellite(Actor):

    id: int
    
    def receiveMessage(self, message, sender):
        print(message)
        