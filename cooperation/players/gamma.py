from cooperation.player import Player
from cooperation.types import Action


class Gamma(Player):
    NAME = "Ewen"
    friendly = {
        "Colin" : True,
        "Jame" : True,
        "Wilfried" : True,
        "Lucas" : True,
        "Pierre-Baptiste" : True,
        "Antoine" : True,
        "Pierre" : True
    }

    def play(self, opponent: str ) -> Action:
        if len(self._fight_history) == 0: 
            if self.friendly[opponent]:
                return Action.COOPERATE
            else :
                return Action.CHEAT

        elif self.friendly[opponent] and self._fight_history[-1]["opponent_action"] == Action.CHEAT:
            self._say("Ah batard, tu triches !")
            self.friendly[opponent] = False

        if self.friendly[opponent]:
            self._say("*serre la main*")
            return Action.COOPERATE
        else :
            self._say("Je n'oublie jamais !")
            return Action.CHEAT