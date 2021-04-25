from thespian.actors import *
from satelliteAPI import SatelliteAPI
from message import Request, Report
import concurrent.futures





class Satellite(Actor):
    
    def receiveMessage(self, message, sender):
        print("Satellites say hi back to " + str(sender))

        errors = {}

        with concurrent.futures.ThreadPoolExecutor() as pool:
            tasks = [
                pool.submit(
                    lambda: message.satelliteAPI.get_status(i)
                ) for i in range (message.first_sat_id, message.first_sat_id + message.sat_range)
            ]

            done, not_done = concurrent.futures.wait(tasks, return_when = concurrent.futures.ALL_COMPLETED, timeout = message.timeout )

            for task in done:
                sat_id, status = task.result()
                if status != message.satelliteAPI.Status.OK:
                    errors[sat_id] = status

            print("Done: " + str(len(done)))
            print("Not done: " + str(len(not_done)))



        
        report = Report()

        report.percent = len(done) / (len(done) + len(not_done)  ) * 100
        print("Percent: ")
        print(report.percent)

        report.error_map = errors
        message.station_info.query_counter += 1
        report.station_info = message.station_info
        self.send(sender, report)