# -*- coding: utf-8 -*-
from datetime import datetime

from game.model.planet.planet import Planet, METAL_MINE_LEVEL_INCREMENT, BASE_METAL_PRODUCTION, BASE_OIL_PRODUCTION, \
    OIL_STATION_LEVEL_INCREMENT
from game.model.planet.planet_repository import PlanetRepository


class PlanetService(object):

    def __init__(self):
        self.planet_repository = PlanetRepository()

    def colonize_planet(self, name, owner_id, metal_mine_level=0, oil_station_level=0):
        return Planet(name, owner_id, metal_mine_level, oil_station_level)

    def improve_metal_mine(self, planet):
        planet.metal_mine_level += 1

    def improve_oil_station(self, planet):
        planet.oil_station_level += 1

    def update_planet_resources(self, planet):
        new_update_time = datetime.utcnow()
        minutes_since_last_update = ((new_update_time - planet.last_update_time).seconds // 60) % 60

        planet.metal_units = self.calculate_new_metal_units(minutes_since_last_update, planet)
        planet.oil_units = self.calculate_new_oil_units(minutes_since_last_update, planet)

        self.planet_repository.put(planet)

    def calculate_new_metal_units(self, minutes_since_last_update, planet):
        return int(planet.metal_units + minutes_since_last_update * (
                BASE_METAL_PRODUCTION * (planet.metal_mine_level * METAL_MINE_LEVEL_INCREMENT + 100) / 100))

    def calculate_new_oil_units(self, minutes_since_last_update, planet):
        return int(planet.oil_units + minutes_since_last_update * (
                BASE_OIL_PRODUCTION * (planet.oil_station_level * OIL_STATION_LEVEL_INCREMENT + 100) / 100))
