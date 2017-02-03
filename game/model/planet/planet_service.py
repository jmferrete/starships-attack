# -*- coding: utf-8 -*-


from game.model.planet.planet import Planet


class PlanetService(object):

    def __init__(self):
        pass

    def colonize_planet(self, name, owner_id):
        return Planet(name, owner_id)

    def improve_metal_mine(self, planet):
        planet.metal_mine_level += 1

    def improve_oil_station(self, planet):
        planet.oil_station_level += 1
