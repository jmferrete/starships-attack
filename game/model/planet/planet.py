# -*- coding: utf-8 -*-


import uuid


class Planet(object):

    def __init__(self, name, onwer_id):
        self.id = uuid.uuid4()
        self.name = name
        self.onwer_id = onwer_id
        self.metal_mine_level = 0


