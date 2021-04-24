from thespian.actors import *


class Request():
    pass

class Station(Actor):
    
    name: str

    def __init__(self, name):
        self.name = name