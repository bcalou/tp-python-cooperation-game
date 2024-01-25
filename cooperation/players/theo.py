from cooperation.player import Player
from cooperation.types import Action


class Theo(Player):
    NAME = "Théo"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
