from cooperation.player import Player
from cooperation.types import Action


class Badr(Player):
    NAME = "Badr"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
