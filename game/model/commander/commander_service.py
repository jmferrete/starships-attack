# -*- coding: utf-8 -*-


from game.model.commander.commander import Commander


class CommanderService(object):

    def __init__(self):
        pass

    def create_commander(self, name):
        return Commander(name)

