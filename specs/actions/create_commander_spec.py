# -*- coding: utf-8 -*-

from expects import *

from game.model.commander.commander_service import CommanderService
from game.model.starship.starship_service import StarshipService

from game.actions.create_commander import CreateCommander

A_COMMANDER_NAME = "an-example-commander-name"
A_STARSHIP_NAME = "an-example-starship-name"

with describe('Create commander action'):
    with it('Can create a commander with an initial starship'):
        create_commander_action = CreateCommander(CommanderService(), StarshipService())

        commander = create_commander_action.execute(A_COMMANDER_NAME, A_STARSHIP_NAME)

        expect(commander).to(have_properties(name=A_COMMANDER_NAME))
        expect(commander.starships).to(have_length(1))
        expect(commander.starships[0]).to(have_properties(name=A_STARSHIP_NAME))
