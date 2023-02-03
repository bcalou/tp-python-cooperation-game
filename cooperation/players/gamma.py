from cooperation.player import Player
from cooperation.types import Action

class Gamma(Player):
    NAME = "Ewen"
    def play(self, opponent: Player, ) -> Action:
        return Action.COOPERATE