from cooperation.log import Log
from cooperation.player import Player
from cooperation.types import Action


class Ewen(Player):
    NAME = "Ewen"

    __last_action: Action

    def __init__(self, log: Log):
        super().__init__(log)
        self.__last_action = Action.CHEAT

    def play(self, opponent: str) -> Action:
        return Action.CHEAT
