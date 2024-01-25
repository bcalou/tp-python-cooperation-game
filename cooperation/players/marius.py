from cooperation.player import Player
from cooperation.types import Action


class Marius(Player):
    NAME = "Marius"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
