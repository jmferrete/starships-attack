# -*- coding: utf-8 -*-


from game.model.base.repository import Repository


class CommanderRepository(Repository):

    def __init__(self):
        self.schema="commander:"
        Repository.__init__(self)

    def find(self, commander_id):
        return Repository.find(self, (self.schema + str(commander_id)))

    def put(self, commander):
        Repository.put(self, (self.schema + str(commander.id)), commander)

    def delete(self, commander):
        Repository.delete(self, (self.schema + str(commander.id)))
