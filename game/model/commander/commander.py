# -*- coding: utf-8 -*-


import uuid

from pydantic import BaseModel


class Commander(object):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.starships = []

    def add_starship(self, starship):
        self.starships.append(starship)


class CommanderInfo(BaseModel):
    commander_name: str
    starship_name: str
