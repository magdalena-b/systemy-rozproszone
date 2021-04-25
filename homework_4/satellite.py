from thespian.actors import *
from satelliteAPI import SatelliteAPI
from message import Request, Report
import concurrent.futures





class Satellite(Actor):

    # id: int
    
    def receiveMessage(self, message, sender):
        print("Satellites say hi back to " + str(sender))

        errors = {}

        with concurrent.futures.ThreadPoolExecutor() as pool:
            tasks = [
                pool.submit(
                    lambda: message.satelliteAPI.get_status(i)
                ) for i in range (message.first_sat_id, message.first_sat_id + message.sat_range)
            ]

            done, not_done = concurrent.futures.wait(tasks, return_when = concurrent.futures.ALL_COMPLETED, timeout = 0.1)

            for task in done:
                sat_id, status = task.result()
                if status != message.satelliteAPI.Status.OK:
                    errors[sat_id] = status

        
        report = Report()
        report.error_map = errors
        report.station = message.station
        report.station_name = message.station_name
        self.send(sender, report)