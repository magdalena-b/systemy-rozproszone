from thespian.actors import *
from satelliteAPI import SatelliteAPI





class Satellite(Actor):

    id: int
    
    def receiveMessage(self, satAPI, sender):
        print("Satellite says hi back")
        status = satAPI.get_status(id)
        print(status)