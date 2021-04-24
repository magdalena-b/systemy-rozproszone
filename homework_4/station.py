from thespian.actors import ActorSystem, ActorTypeDispatcher, ActorExitRequest


class Station():
    
    name: str

    def __init__(self, name):
        self.name = name