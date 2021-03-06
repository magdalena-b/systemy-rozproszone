from thespian.actors import *
from satelliteAPI import SatelliteAPI
from message import Request, Report
import concurrent.futures

import time



class Satellite(Actor):
    
    def receiveMessage(self, message, sender):

        errors = {}
        report = Report()
        report.start_time = time.time()

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
        

        report.percent = len(done) / (len(done) + len(not_done)  ) * 100
        report.error_map = errors
        report.station_info = message.station_info

        self.send(sender, report)