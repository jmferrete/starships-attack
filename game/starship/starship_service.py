# -*- coding: utf-8 -*-


from game.starship.starship import Starship


class StarshipService(object):

    def __init__(self):
        pass

    def create_starship(self, name, owner_id):
        return Starship(name, owner_id)
