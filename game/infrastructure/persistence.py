# -*- coding: utf-8 -*-


import redis, pickle


class Database(object):

    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        self.r = redis.Redis(connection_pool=self.pool)

    def put(self, id, elem):
        self.r.set(id, pickle.dumps(elem))

    def get(self, id):
        result = self.r.get(id)
        if result is not None:
            return pickle.loads(result)

    def delete(self, id):
        self.r.delete(id)


