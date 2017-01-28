# -*- coding: utf-8 -*-


import uuid


class Commander(object):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.starships = []

    def addStarship(self, starship):
        self.starships.append(starship)


