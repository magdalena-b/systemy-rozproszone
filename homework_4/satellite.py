from thespian.actors import ActorSystem, ActorTypeDispatcher, ActorExitRequest


class Satellite():

    id: int

    def __init__(self, id):
        self.id = id