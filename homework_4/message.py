from thespian.actors import *
from satelliteAPI import SatelliteAPI

class Request():
    
    satellites: dict
    query_id: int
    first_sat_id: int
    sat_range: int
    timeout: int
    satelliteAPI: SatelliteAPI
   
    def __init__(self, satellites, query_id, first_sat_id, sat_range, timeout, satAPI, dispatcher):
        self.satellites = satellites
        self.query_id = query_id
        self.first_sat_id = first_sat_id
        self.sat_range = sat_range
        self.timeout = timeout
        self.satelliteAPI = satAPI
        self.dispatcher = dispatcher


class Report():

    query_id: int
    error_map: dict
    percent: int

    def __init__(self):
        self.query_id = -1
        self.error_map = {}
        self.percent = 0

    