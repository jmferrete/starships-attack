# -*- coding: utf-8 -*-


import redis, pickle


class Database(object):

    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        self.r = redis.Redis(connection_pool=self.pool)

    def put(self, id, elem):
        self.r.set(id, pickle.dumps(elem))

    def get(self, id):
        return pickle.loads(self.r.get(id))


