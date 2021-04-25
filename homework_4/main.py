from thespian.actors import *

from satelliteAPI import SatelliteAPI
from station import Station
from satellite import Satellite
from dispatcher import Dispatcher
from message import Request, Report





if __name__ == "__main__":
    # system = ActorSystem("multiprocTCPBase")
    system = ActorSystem()
    station1 = system.createActor(Station)
    station1.name = "Pirx"
    dispatcher = system.createActor(Dispatcher)

    satAPI = SatelliteAPI()
    # satellites = {}

    # for i in range(100, 200):
    #     sat = system.createActor(Satellite)
    #     sat.id = i
    #     satellites[i] = sat

    satellite = system.createActor(Satellite)

    msg = Request(satellite, 0, 100, 30, 0.01, satAPI, dispatcher, station1)
    # ActorSystem().tell(dispatcher, msg)
    # Station.send(dispatcher, msg)

    system.tell(station1, msg)
