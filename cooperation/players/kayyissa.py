from cooperation.player import Player
from cooperation.types import Action


class Kayyissa(Player):
    NAME = "Kayyissa"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
