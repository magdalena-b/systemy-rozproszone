from thespian.actors import *
from satelliteAPI import SatelliteAPI

class Request():
       
    def __init__(self, satellite, first_sat_id, sat_range, timeout, satAPI, dispatcher, station_info):
        self.satellite = satellite
        self.first_sat_id = first_sat_id
        self.sat_range = sat_range
        self.timeout = timeout
        self.satelliteAPI = satAPI
        self.dispatcher = dispatcher
        self.station_info = station_info


class Report():

    def __init__(self):
        self.query_id = -1
        self.error_map = {}
        self.percent = 0
        self.station_info = None

    