# -*- coding: utf-8 -*-


from game.model.planet.planet import Planet


class PlanetService(object):

    def __init__(self):
        pass

    def colonize_planet(self, name, owner_id):
        return Planet(name, owner_id)

