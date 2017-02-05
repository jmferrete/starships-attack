#!/usr/bin/env python
# -*- coding: utf-8 -*-


from game.infrastructure import persistence
from game.model.commander import commander_service, commander_repository
from game.model.planet import planet_service, planet_repository

COMMANDER_NAME='titan'
PLANET_1_NAME='zeus'
PLANET_2_NAME='afrodita'

if __name__ == '__main__':
    persistence.Database().clean()
    commander_service = commander_service.CommanderService()
    commander_repository = commander_repository.CommanderRepository()
    planet_service = planet_service.PlanetService()
    planet_repository = planet_repository.PlanetRepository()

    commander = commander_service.create_commander(name=COMMANDER_NAME)
    commander_repository.put(commander)
    planet1 = planet_service.colonize_planet(name=PLANET_1_NAME, owner_id=commander.id, metal_mine_level=5, oil_station_level=5)
    planet2 = planet_service.colonize_planet(name=PLANET_2_NAME, owner_id=commander.id, metal_mine_level=3, oil_station_level=3)
    planet_repository.put(planet1)
    planet_repository.put(planet2)

