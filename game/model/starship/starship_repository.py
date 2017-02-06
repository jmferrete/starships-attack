# -*- coding: utf-8 -*-


from game.model.base.repository import Repository


class StarshipRepository(Repository):

    def __init__(self):
        self.schema="starship:"
        Repository.__init__(self)

    def find(self, starship_id):
        return Repository.find(self, (self.schema + str(starship_id)))

    def put(self, starship):
        Repository.put(self, (self.schema + str(starship.id)), starship)

    def delete(self, starship):
        Repository.delete(self, (self.schema + str(starship.id)))

