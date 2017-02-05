# -*- coding: utf-8 -*-


import uuid


class Planet(object):

    def __init__(self, name, onwer_id, metal_mine_level=0, oil_station_level=0):
        self.id = uuid.uuid4()
        self.name = name
        self.onwer_id = onwer_id
        self.metal_mine_level = metal_mine_level
        self.oil_station_level = oil_station_level
        self.metal_units = 0
        self.oil_units = 0


