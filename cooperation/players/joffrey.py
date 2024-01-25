from cooperation.types import Action
from cooperation.player import Player
import random


class Joffrey(Player):
    NAME = "Joffrey"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
