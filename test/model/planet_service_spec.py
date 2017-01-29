# -*- coding: utf-8 -*-

from expects import *

from game.model.planet import planet_service

A_COMMANDER_ID="an-example-commander-id"
A_PLANET_NAME="an-example-planet-name"

with describe('Planet service'):
    with context('Colonize planet'):
        with it('discover the planet'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)

            expect(planet).to(have_properties(name=A_PLANET_NAME))


def _a_planet_service():
    return planet_service.PlanetService()

