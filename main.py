from typing import Optional

from fastapi import FastAPI, status
from starlette.responses import RedirectResponse

from game.actions.create_commander import CreateCommander
from game.model.commander.commander import CommanderInfo
from game.model.commander.commander_service import CommanderService
from game.model.starship.starship_service import StarshipService

app = FastAPI()

commander_service = CommanderService()
starship_service = StarshipService()


@app.get("/")
def redirect_to_docs():
    return RedirectResponse("/docs", status_code=status.HTTP_308_PERMANENT_REDIRECT)


@app.post("/commander", status_code=status.HTTP_201_CREATED)
def create_commander(commander_info: CommanderInfo):
    commander = CreateCommander(commander_service, starship_service).execute(
        commander_info.commander_name, commander_info.starship_name)
    return commander
