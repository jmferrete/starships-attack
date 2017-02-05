# -*- coding: utf-8 -*-


from game.model.base.repository import Repository


class StarshipRepository(Repository):

    def __init__(self):
        self.PREFIX="STARSHIP_"
        Repository.__init__(self)

    def find(self, starship_id):
        return Repository.find(self, (self.PREFIX + str(starship_id)))

    def put(self, starship):
        Repository.put(self, (self.PREFIX + str(starship.id)), starship)

    def delete(self, starship):
        Repository.delete(self, (self.PREFIX + str(starship.id)))

