# -*- coding: utf-8 -*-


from game.infrastructure.persistence import Database


class CommanderRepository(object):

    def __init__(self):
        self.database = Database()

    def find(self, commander_id):
        return self.database.get(commander_id)

    def put(self, commander):
        self.database.put(commander.id, commander)

    def delete(self, commander_id):
        self.database.delete(commander_id)

