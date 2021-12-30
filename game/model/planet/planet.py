# -*- coding: utf-8 -*-


import uuid
from datetime import datetime

BASE_METAL_PRODUCTION = 20
METAL_MINE_LEVEL_INCREMENT = 25
BASE_OIL_PRODUCTION = 10
OIL_STATION_LEVEL_INCREMENT = 15


class Planet(object):

    def __init__(self, name, onwer_id, metal_mine_level=0, oil_station_level=0):
        self.id = uuid.uuid4()
        self.name = name
        self.onwer_id = onwer_id
        self.metal_mine_level = metal_mine_level
        self.oil_station_level = oil_station_level
        self.metal_units = 0
        self.oil_units = 0
        self.last_update_time = datetime.utcnow()
