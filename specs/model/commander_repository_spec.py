# -*- coding: utf-8 -*-

from expects import *

from game.model.commander import commander_service
from game.model.commander import commander_repository

A_COMMANDER_NAME = "an-example-commander-name"

with describe('Commander repository'):
    with context('Find commander'):
        with it('by ID'):
            commander = _a_commander_service().create_commander(name=A_COMMANDER_NAME)
            commander_repository = _a_commander_repository()
            commander_repository.put(commander)

            found_commander = commander_repository.find(commander.id)

            expect(found_commander).to(have_properties(name=A_COMMANDER_NAME))

    with context('Delete commander'):
        with it('by ID'):
            commander = _a_commander_service().create_commander(name=A_COMMANDER_NAME)
            commander_repository = _a_commander_repository()
            commander_repository.put(commander)

            commander_repository.delete(commander)
            found_commander = commander_repository.find(commander.id)

            expect(found_commander).to(be(None))


def _a_commander_service():
    return commander_service.CommanderService()


def _a_commander_repository():
    return commander_repository.CommanderRepository()
