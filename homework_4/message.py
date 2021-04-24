from thespian.actors import *


class Request():
    
    query_id: int
    first_sat_id: int
    sat_range: int
    timeout: int

    def __init__(self, query_id, first_sat_id, sat_range, timeout):
        self.query_id = query_id
        self.first_sat_id = first_sat_id
        self.sat_range = sat_range
        self.timeout = timeout


class Report():

    request: Request
    error_map: dict
    percent: int

    def __init__(self, request):
        self.request = request
        error_map = {}
        percent = 0

    