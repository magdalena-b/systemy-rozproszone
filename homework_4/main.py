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
        # print(i)
        sat = ActorSystem().createActor(Satellite)
        satellites[i] = sat
        # print(satellites[i])

    # print(satellites[110] )


    msg = Request(satellites, 0, 100, 10, 0.5, satAPI)

    # ActorSystem().ask(station1, msg, 0.1)
    ActorSystem().tell(dispatcher, msg)