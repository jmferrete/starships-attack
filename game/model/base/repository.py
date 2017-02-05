# -*- coding: utf-8 -*-


from game.infrastructure.persistence import Database


class Repository(object):

    def __init__(self):
        self.database = Database()

    def find(self, obj_id):
        return self.database.get(obj_id)

    def put(self, id, obj):
        self.database.put(id, obj)

    def delete(self, id):
        self.database.delete(id)


