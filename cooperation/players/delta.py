from cooperation.types import Action
from cooperation.player import Player
import random


class Delta(Player):
    NAME = "Wilfried"

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        arr = [Action.CHEAT, Action.COOPERATE]

        return random.choice(arr)
