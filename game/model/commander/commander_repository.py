# -*- coding: utf-8 -*-


from game.infrastructure.persistence import Database


class CommanderRepository(object):

    def __init__(self):
        self.database = Database()

    def find(self, id):
        return self.database.get(id)

    def put(self, commander):
        self.database.put(commander.id, commander)

