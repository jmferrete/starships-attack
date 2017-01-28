# -*- coding: utf-8 -*-

from expects import *

from game.model.starship import starship_service

A_COMMANDER_ID="an-example-commander-id"
A_STARSHIP_NAME="an-example-starship-name"

with describe('Starship service'):
    with context('Create starship'):
        with it('builds the starship'):
            starship = _a_starship_service().create_starship(name=A_STARSHIP_NAME, owner_id=A_COMMANDER_ID)

            expect(starship).to(have_properties(name=A_STARSHIP_NAME))


def _a_starship_service():
    return starship_service.StarshipService()

