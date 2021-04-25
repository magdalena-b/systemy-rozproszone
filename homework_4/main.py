from thespian.actors import *

from satelliteAPI import SatelliteAPI
from station import Station, Station_Info
from satellite import Satellite
from dispatcher import Dispatcher
from message import Request, Report





if __name__ == "__main__":
    system = ActorSystem("multiprocQueueBase")
    system = ActorSystem()
    station1 = system.createActor(Station)
    station1_info = Station_Info(station1, "Pirx", 0)

    dispatcher = system.createActor(Dispatcher)
    satAPI = SatelliteAPI()
    satellite = system.createActor(Satellite)

    msg = Request(satellite, station1_info.query_counter, 100, 100, 0.3, satAPI, dispatcher, station1_info)
    system.tell(station1, msg)
    