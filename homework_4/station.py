from thespian.actors import *
from message import *

class Station(Actor):
    
    name: str
    query_id: int

    def __init__(self):
        print("Inited Station")
        self.query_id = 0


    def receiveMessage(self, message, sender):
        if isinstance(message, Request):
            print("station got request")
            self.send(message.dispatcher, message)



