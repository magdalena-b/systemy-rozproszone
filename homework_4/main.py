from thespian.actors import *

from satelliteAPI import SatelliteAPI
from station import Station
from satellite import Satellite
from dispatcher import Dispatcher
from message import Request, Report





if __name__ == "__main__":
    station1 = ActorSystem().createActor(Station)
    station1.name = "Lol"
    dispatcher = ActorSystem().createActor(Dispatcher)

    satAPI = SatelliteAPI()
    satellites = {}

    for i in range(100, 200):
        sat = ActorSystem().createActor(Satellite)
        sat.id = i
        satellites[i] = sat

    msg = Request(satellites, 0, 100, 10, 0.01, satAPI, dispatcher)
    # ActorSystem().tell(dispatcher, msg)
    # Station.send(dispatcher, msg)

    ActorSystem().tell(station1, msg)
