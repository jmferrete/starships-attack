# -*- coding: utf-8 -*-


from game.model.base.repository import Repository


class CommanderRepository(Repository):

    def __init__(self):
        self.PREFIX="COMMANDER_"
        Repository.__init__(self)

    def find(self, commander_id):
        return Repository.find(self, (self.PREFIX + str(commander_id)))

    def put(self, commander):
        Repository.put(self, (self.PREFIX + str(commander.id)), commander)

    def delete(self, commander):
        Repository.delete(self, (self.PREFIX + str(commander.id)))
