# -*- coding: utf-8 -*-


from game.infrastructure.persistence import Database


class Repository(object):

    def __init__(self):
        self.database = Database()

    def find(self, obj_id):
        return self.database.get(obj_id)

    def findAll(self, obj_id):
        objs = []
        ids = self.database.getKeys(obj_id)

        for id in ids:
            objs.append(self.database.get(id))

        return objs

    def put(self, obj_id, obj):
        self.database.put(obj_id, obj)

    def delete(self, obj_id):
        self.database.delete(obj_id)


