from cooperation.player import Player
from cooperation.types import Action


class Theo(Player):
    NAME = "Théo"
    count: int = 0

    def play(self, opponent: str) -> Action:
        self.count += 1
        return Action.COOPERATE if self.count%2==0 else Action.CHEAT
