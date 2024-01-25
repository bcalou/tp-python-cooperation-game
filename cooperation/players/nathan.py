from cooperation.player import Player
from cooperation.types import Action


class Nathan(Player):
    NAME = "Nathan"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
