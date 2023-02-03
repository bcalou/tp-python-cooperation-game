from cooperation.types import Action
from cooperation.player import Player
import random


class Delta(Player):
    NAME = "Wilfried"
    prev_score = 0

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""

        action = Action.CHEAT if self.score <= Delta.prev_score else Action.COOPERATE
        Delta.prev_score = self.score
        return action
