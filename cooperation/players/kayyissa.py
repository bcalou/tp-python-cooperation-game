from cooperation.player import Player
from cooperation.types import Action


class Kayyissa(Player):
    NAME = "Kayyissa"

    def play(self, opponent: str) -> Action:
        action: Action = Action.CHEAT

        for i in range(len(self._fight_history)):
            if self._fight_history[len(self._fight_history)]["opponent_action"] == Action.COOPERATE:
                action = Action.COOPERATE
            else:
                action = Action.CHEAT
            if i == 9:
                action = Action.CHEAT
            
        return action
