from thespian.actors import *
from satelliteAPI import SatelliteAPI
from message import Request, Report





class Satellite(Actor):

    id: int
    
    def receiveMessage(self, satAPI, sender):
        print("Satellite says hi back to " + str(sender))
        status = satAPI.get_status(id)
        print(status)
        report = Report()
        self.send(sender, report)