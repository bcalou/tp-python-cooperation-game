from cooperation.player import Player
from cooperation.types import Action


class Gamma(Player):
    NAME = "Ewen"
    friendly = {
        "Colin": True,
        "Jame": False,
        "Wilfried": True,
        "Lucas": False,
        "Pierre-Baptiste": True,
        "Antoine": True,
        "Pierre": True
    }

    def play(self, opponent) -> Action:

        return Action.COOPERATE

        """if len(self._fight_history)%10 == 0: 
            if self.friendly[opponent.NAME]:
                return Action.COOPERATE
            else :
                return Action.CHEAT

        elif self._fight_history[-1] == Action.CHEAT:
            self.friendly[opponent.NAME] = False

        if self.friendly[opponent.NAME]:
            return Action.COOPERATE
        else :
            return Action.CHEAT"""
