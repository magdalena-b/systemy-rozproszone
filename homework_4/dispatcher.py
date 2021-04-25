from thespian.actors import *
from message import Request, Report
from satellite import Satellite

import time
import threading

global_lock = threading.Lock()

class Dispatcher(ActorTypeDispatcher):
    global global_lock

    def receiveMsg_Request(self, message, sender):
        sat = self.createActor(Satellite)
        self.send(sat, message)


    def receiveMsg_Report(self, message, sender):
        message.end_time = time.time()
        message.execution_time = (message.end_time - message.start_time) * 1000

        def update_db():
            while global_lock.locked():
                continue

            global_lock.acquire()
            f = open("db.txt", "a")
            for key in message.error_map:
                f.write(str(key) + "\n")

            f.flush()
            global_lock.release()

        thread = threading.Thread(target = update_db)
        thread.start()
        thread.join()

        self.send(message.station_info.station, message)