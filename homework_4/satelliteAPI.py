from thespian.actors import *
import time, enum, random

class SatelliteAPI(Actor):

    class Status(enum.Enum):
        OK = 1
        BATTERY_LOW = 2
        PROPULSION_ERROR = 3
        NAVIGATION_ERROR = 4

    def get_status(self, sat_id):
        p = random.uniform(0, 1)
        # try:
        #     time.sleep( (100 + random.randint(0, 400)) / 1000 )
        # except:
        #     print("Error occured in get_status")
        
        # while True:
        #     time.sleep(1)

        if p < 0.8:
            return sat_id, self.Status.OK
        elif p < 0.9:
            return sat_id, self.Status.BATTERY_LOW
        elif p < 0.95:
            return sat_id, self.Status.NAVIGATION_ERROR
        else:
            return sat_id, self.Status.PROPULSION_ERROR

