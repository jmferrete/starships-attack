# -*- coding: utf-8 -*-


from game.model.base.repository import Repository


class PlanetRepository(Repository):

    def __init__(self):
        self.schema="planet:"
        Repository.__init__(self)

    def find(self, planet_id):
        return Repository.find(self, (self.schema + str(planet_id)))

    def findAll(self):
        return Repository.findAll(self, self.schema)

    def put(self, planet):
        Repository.put(self, (self.schema + str(planet.id)), planet)

    def delete(self, planet):
        Repository.delete(self, (self.schema + str(planet.id)))

