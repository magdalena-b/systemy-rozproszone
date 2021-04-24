from thespian.actors import *


class Request():
    pass

class Station(Actor):
    
    name: str

    def receiveMessage(self, message, sender):
        print(message)

