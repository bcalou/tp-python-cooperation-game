from cooperation.player import Player
from cooperation.types import Action


class Lois(Player):
    NAME = "Loïs"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
