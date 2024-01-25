from cooperation.player import Player
from cooperation.types import Action


class Ewen(Player):
    NAME = "Ewen"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
