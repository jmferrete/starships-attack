# -*- coding: utf-8 -*-

from expects import *

from game.model.planet import planet_service
from game.model.planet import planet_repository

A_COMMANDER_ID="an-example-commander-id"
A_PLANET_NAME="an-example-planet-name"

with describe('Planet repository'):
    with context('Find planet'):
        with it('by ID'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)
            planet_repository = _a_planet_repository()
            planet_repository.put(planet)

            found_planet = planet_repository.find(planet.id)

            expect(found_planet).to(have_properties(name=A_PLANET_NAME))

    with context('Delete planet'):
        with it('by ID'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)
            planet_repository = _a_planet_repository()
            planet_repository.put(planet)

            planet_repository.delete(planet)
            found_planet = planet_repository.find(planet.id)

            expect(found_planet).to(be(None))

def _a_planet_service():
    return planet_service.PlanetService()

def _a_planet_repository():
    return planet_repository.PlanetRepository()
