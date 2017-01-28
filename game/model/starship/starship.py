# -*- coding: utf-8 -*-


import uuid


class Starship(object):

    def __init__(self, name, owner_id):
        self.id = uuid.uuid4()
        self.name = name
        self.onwer_id = owner_id


