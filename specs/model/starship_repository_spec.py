# -*- coding: utf-8 -*-

from expects import *

from game.model.starship import starship_service
from game.model.starship import starship_repository

A_COMMANDER_ID="an-example-commander-id"
A_STARSHIP_NAME="an-example-starship-name"

with describe('Starship repository'):
    with context('Find starship'):
        with it('by ID'):
            starship = _a_starship_service().create_starship(name=A_STARSHIP_NAME, owner_id=A_COMMANDER_ID)
            starship_repository = _a_starship_repository()
            starship_repository.put(starship)

            found_starship = starship_repository.find(starship.id)

            expect(found_starship).to(have_properties(name=A_STARSHIP_NAME))

    with context('Delete starship'):
        with it('by ID'):
            starship = _a_starship_service().create_starship(name=A_STARSHIP_NAME, owner_id=A_COMMANDER_ID)
            starship_repository = _a_starship_repository()
            starship_repository.put(starship)

            starship_repository.delete(starship)
            found_starship = starship_repository.find(starship.id)

            expect(found_starship).to(be(None))

def _a_starship_service():
    return starship_service.StarshipService()

def _a_starship_repository():
    return starship_repository.StarshipRepository()
