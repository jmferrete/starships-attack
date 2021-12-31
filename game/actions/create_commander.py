# -*- coding: utf-8 -*-


class CreateCommander(object):

    def __init__(self, commander_service, starship_service):
        self.commander_service = commander_service
        self.starship_service = starship_service

    def execute(self, commander_name, starship_name):
        commander = self.commander_service.create_commander(commander_name)
        initial_starship = self.starship_service.create_starship(starship_name, commander.id)
        commander.add_starship(initial_starship)

        return commander
