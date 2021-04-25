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
            f = open("db.txt", "r")
            lines = f.readlines()
            f.close()

            lines_to_delete = []
            modified_lines = []

            for line in lines:
                sat_id, counter = line.split()
                for key in message.error_map:
                    if sat_id == str(key):
                        lines_to_delete.append(line)
                        counter_int = int(counter)
                        counter_int += 1
                        modified_line = str(key) + " " + str(counter_int) + "\n"
                        modified_lines.append(modified_line)

            with open("db.txt", "w") as f:
                for line in lines:
                    if line in lines_to_delete:
                        continue
                    f.write(line)
                for mod_line in modified_lines:
                    f.write(mod_line)

            global_lock.release()

        thread = threading.Thread(target = update_db)
        thread.start()
        thread.join()

        self.send(message.station_info.station, message)