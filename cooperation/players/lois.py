from cooperation.player import Player
from cooperation.types import Action
import random

class Lois(Player):
    NAME = "Loïs"
    def play(self, opponent: str) -> Action:
        WEIGHT_1 = 0.5
        WEIGHT_2 = 0.5
        if (self._fight_history[-1].opponent_action == Action.CHEAT):
            WEIGHT_1 = 0.3
            WEIGHT_2 = 0.7
        return (random.choices([Action.COOPERATE, Action.CHEAT], [WEIGHT_1, WEIGHT_2])[0])