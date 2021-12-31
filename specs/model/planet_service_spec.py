# -*- coding: utf-8 -*-

from expects import *

from game.model.planet import planet_service

A_COMMANDER_ID = "an-example-commander-id"
A_PLANET_NAME = "an-example-planet-name"

with describe('Planet service'):
    with context('Colonize planet'):
        with it('discover the planet'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)

            expect(planet).to(have_properties(name=A_PLANET_NAME))

    with context('Improve resources'):
        with it('improve the metal mine'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)

            _a_planet_service().improve_metal_mine(planet)

            expect(planet).to(have_properties(metal_mine_level=1))

        with it('improve the oil extraction station'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)

            _a_planet_service().improve_oil_station(planet)

            expect(planet).to(have_properties(oil_station_level=1))

    with context('Updating resources'):
        with it('calculates the production of metal units for a planet with the metal mine at the starting level'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)
            minutes_since_last_update = 5

            metal_units = _a_planet_service().calculate_new_metal_units(minutes_since_last_update, planet)

            expect(metal_units).to(be(100))

        with it('calculates the production of metal units for a planet with the metal mine at level 3'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)
            planet.metal_mine_level = 3
            minutes_since_last_update = 5

            metal_units = _a_planet_service().calculate_new_metal_units(minutes_since_last_update, planet)

            expect(metal_units).to(be(175))

        with it('calculates the production of oil units for a planet with the oil mine at the starting level'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)
            minutes_since_last_update = 5

            oil_units = _a_planet_service().calculate_new_oil_units(minutes_since_last_update, planet)

            expect(oil_units).to(be(50))

        with it('calculates the production of oil units for a planet with the oil mine at level 3'):
            planet = _a_planet_service().colonize_planet(name=A_PLANET_NAME, owner_id=A_COMMANDER_ID)
            planet.oil_station_level = 3
            minutes_since_last_update = 5

            oil_units = _a_planet_service().calculate_new_oil_units(minutes_since_last_update, planet)

            expect(oil_units).to(be(72))


def _a_planet_service():
    return planet_service.PlanetService()
