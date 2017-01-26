# -*- coding: utf-8 -*-


from game.commander.commander import Commander


class CommanderService(object):

    def __init__(self):
        pass

    def create_commander(self, name):
        return Commander(name)

