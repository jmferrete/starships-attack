#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from game.model.planet.planet_repository import PlanetRepository


RELOAD_TIME = 5
METAL_INCREASE_BY_LEVEL = 100
OIL_INCREASE_BY_LEVEL = 30


if __name__ == '__main__':
    planet_repository = PlanetRepository()

    while True:
        print("Recalculating resources...")
        all_planets = planet_repository.find_all()

        for planet in all_planets:
            print("Planet -> {}".format(planet.name))
            print("    Metal -> {}".format(planet.metal_units))
            print("    Oil -> {}".format(planet.oil_units))
            planet.metal_units += planet.metal_mine_level * METAL_INCREASE_BY_LEVEL
            planet.oil_units += planet.oil_station_level * OIL_INCREASE_BY_LEVEL
            planet_repository.put(planet)

        print("Done.")
        time.sleep(RELOAD_TIME)


