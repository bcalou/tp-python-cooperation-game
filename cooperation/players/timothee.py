from cooperation.player import Player
from cooperation.types import Action


class Timothee(Player):
    NAME = "Timothee"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
