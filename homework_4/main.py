from thespian.actors import *

from satelliteAPI import SatelliteAPI
from station import Station, Station_Info
from satellite import Satellite
from dispatcher import Dispatcher
from message import Request, Report

import time



if __name__ == "__main__":
    system = ActorSystem("multiprocQueueBase")
    system = ActorSystem()

    def send_request(station_info):
        station_info.query_counter += 1
        first_sat_id = 100
        sat_range = 100
        timeout = 0.3
        msg = Request(satellite, first_sat_id, sat_range, timeout, satAPI, dispatcher, station_info)
        system.tell(station_info.station, msg)



    dispatcher = system.createActor(Dispatcher)
    satAPI = SatelliteAPI()
    satellite = system.createActor(Satellite)

    # Pirx 

    station1 = system.createActor(Station)
    station1_info = Station_Info(station1, "Pirx", 0)

    send_request(station1_info)
    time.sleep(0.5)
    send_request(station1_info)

    # Glob

    station2 = system.createActor(Station)
    station2_info = Station_Info(station2, "Glob", 0)
    
    send_request(station2_info)
    time.sleep(0.2)
    send_request(station2_info)

    # Ripley

    station3 = system.createActor(Station)
    station3_info = Station_Info(station2, "Ripley", 0)

    send_request(station3_info)
    time.sleep(0.2)
    send_request(station3_info)

    