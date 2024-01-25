from cooperation.player import Player
from cooperation.types import Action


class Baptiste(Player):
    NAME = "Baptiste"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
