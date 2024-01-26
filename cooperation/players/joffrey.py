from cooperation.types import Action
from cooperation.player import Player
import random


class Joffrey(Player):
    NAME = "Joffrey"
    vague = 0
    coop_count = 0
    trap_count = 0

    def play(self, opponent: str) -> Action:
        self.vague+=1
        self._say("C'est la vague "+str(self.vague))
        if (len(self._fight_history)==0):
            self._say("Salut mon pote !!!")
            self._say("On coopère pour la premiere vague ?")
            return Action.COOPERATE
        if(self._fight_history[-1]["opponent_action"]==Action.COOPERATE):
            self._say("Tu as coopere, "+str(self.coop_count)+" COPAIN !!!")
            self.coop_count+=1
        if(self._fight_history[-1]["opponent_action"]==Action.CHEAT):
            self._say("Tu as triché, "+str(self.trap_count)+" fois TRAHISON !!!")
            self.trap_count+=1
        self._say("Pour l'instant, tu as fait "+str(self.coop_count)+" cooperation et "+str(self.trap_count)+" trahisons")
        
        return self._fight_history[-1]["opponent_action"]
