from thespian.actors import *

from satelliteAPI import SatelliteAPI
from station import Station, Station_Info
from satellite import Satellite
from dispatcher import Dispatcher
from message import Request, Report

import time
import concurrent.futures


if __name__ == "__main__":
    system = ActorSystem("multiprocQueueBase")
    system = ActorSystem()

    def send_request(station_info):
        station_info.query_counter += 1
        first_sat_id = 100
        sat_range = 100
        timeout = 0.3
        msg = Request(first_sat_id, sat_range, timeout, satAPI, dispatcher, station_info)
        system.tell(station_info.station, msg)

    def init_station(name):
        station = system.createActor(Station)
        station_info = Station_Info(station, name, 0)

        send_request(station_info)
        time.sleep(0.1)
        send_request(station_info)



    dispatcher = system.createActor(Dispatcher)
    satAPI = SatelliteAPI()
    satellite = system.createActor(Satellite)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(init_station("Pirx"), init_station("Glob"), init_station("Ripley"))

    