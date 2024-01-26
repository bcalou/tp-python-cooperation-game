from cooperation.types import Action
from cooperation.player import Player
import random


class Joffrey(Player):
    NAME = "Joffrey"

    def play(self, opponent: str) -> Action:
        self._say("Salut mon pote !!!")
        return Action.COOPERATE if len(self._fight_history)==0 else self._fight_history[-1]["opponent_action"]
