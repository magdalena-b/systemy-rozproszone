from thespian.actors import ActorSystem, ActorTypeDispatcher, ActorExitRequest
from satelliteAPI import SatelliteAPI


class Satellite():

    id: int
    satAPI: SatelliteAPI

    def __init__(self, id):
        self.id = id
        self.satAPI = SatelliteAPI()


    def receiveMsg(self, message, sender):
        pass
        