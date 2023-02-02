from cooperation.types import Action
from cooperation.player import Player


class Delta(Player):
    NAME = "Wilfried"
    C = 0

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        Delta.C += 1
        return Action.CHEAT if Delta.C % 2 == 0 else Action.COOPERATE
