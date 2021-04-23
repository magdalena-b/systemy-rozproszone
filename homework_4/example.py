# https://sabaini.at/peterlog/posts/2020/Feb/16/thespian-a-python-actor-system/

from thespian.actors import ActorSystem, ActorTypeDispatcher, ActorExitRequest


class Greeting:
    # Just a class to hold a greeting and some addresses
    def __init__(self, msg):
        self.message = msg
        self.send_to = []

    def __str__(self):
        return self.message


class Hello(ActorTypeDispatcher):
    def receiveMsg_str(self, message, sender):
        # This method will handle all messages of type str()
        if message == 'hi':
            # Create two actors of type World and Punctuate
            world = self.createActor(World)
            punct = self.createActor(Punctuate)
            # Create a greeting and set the punctuate and orig. sender addresses
            greeting = Greeting('Hello')
            greeting.send_to = [punct, sender]
            # Send the greeting to the World actor
            self.send(world, greeting)


class World(ActorTypeDispatcher):
    def receiveMsg_Greeting(self, message, sender):
        # This will receive all messages of type Greeting
        # Update the message and pass it to the first address 
        message.message = message.message + ", World"
        next_to = message.send_to.pop(0)
        self.send(next_to, message)


class Punctuate(ActorTypeDispatcher):

    def receiveMsg_Greeting(self, message, sender):
        # This will receive all messages of type Greeting
        # Update message again and send back to orig. sender
        message.message = message.message + "!!!"
        next_to = message.send_to.pop(0)
        self.send(next_to, message)


if __name__ == "__main__":
    hello = ActorSystem().createActor(Hello)
    # Send message to first actor, then send an exit request
    print(ActorSystem().ask(hello, 'hi', 0.2))
    ActorSystem().tell(hello, ActorExitRequest())