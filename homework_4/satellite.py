from thespian.actors import *
from satelliteAPI import SatelliteAPI
from message import Request, Report





class Satellite(Actor):

    # id: int
    
    def receiveMessage(self, message, sender):
        print("Satellites say hi back to " + str(sender))

        errors = {}

        for i in range(message.first_sat_id, message.first_sat_id + message.sat_range):
            try:
                status = message.satelliteAPI.get_status(i)
                if status != message.satelliteAPI.Status.OK:
                    errors[i] = status
            except ActorSystemRequestTimeout:
                print("Error")

        # status = satAPI.get_status(id)
        # print(status)
        
        report = Report()
        report.error_map = errors
        report.station = message.station
        report.station_name = message.station_name
        self.send(sender, report)