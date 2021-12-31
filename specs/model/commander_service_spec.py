# -*- coding: utf-8 -*-

from expects import *

from game.model.commander import commander_service

A_COMMANDER_NAME = "an-example-commander-name"

with describe('Commander service'):
    with context('Create commander'):
        with it('builds the commander'):
            commander = _a_commander_service().create_commander(name=A_COMMANDER_NAME)

            expect(commander).to(have_properties(name=A_COMMANDER_NAME))


def _a_commander_service():
    return commander_service.CommanderService()
