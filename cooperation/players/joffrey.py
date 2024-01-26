from cooperation.types import Action
from cooperation.player import Player
import random


class Joffrey(Player):
    NAME = "Joffrey"

    def play(self, opponent: str) -> Action:
        self._say("Salut mon pote !!!")
        if (len(self._fight_history)==0):
            self._say("On coopère pour la première fois")
            return Action.COOPERATE
        if(self._fight_history[-1]["opponent_action"]==Action.COOPERATE):
            self._say("Tu as coopéré, COPAIN !!!")
        if(self._fight_history[-1]["opponent_action"]==Action.CHEAT):
            self._say("Tu as triché, TRAHISON !!!")
        return self._fight_history[-1]["opponent_action"]
