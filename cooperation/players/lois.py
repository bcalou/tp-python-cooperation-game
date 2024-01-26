from cooperation.player import Player
from cooperation.types import Action
import random

class Lois(Player):
    NAME = "Loïs"

    def play(self, opponent: str) -> Action:
        return (random.choices([Action.COOPERATE, Action.CHEAT], [0.4, 0.6])[0])
