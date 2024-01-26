from cooperation.player import Player
from cooperation.types import Action


class Kayyissa(Player):
    NAME = "Kayyissa"

    def play(self, opponent: str) -> Action:
        action: Action = Action.COOPERATE

        #for i in range(len(self._fight_history)):
        #    if self._fight_history[len(self._fight_history)]["opponent_action"] == Action.COOPERATE:
        #        action = Action.CHEAT
        #    else:
        #        action = Action.COOPERATE

        totalCheat: float = 0
        totalCoop: float = 0
        lastMove: Action = Action.CHEAT

        for turn in self._fight_history:
            if turn["opponent_action"] == Action.CHEAT:
                totalCheat += 1
            else:
                totalCoop += 1
            lastMove = turn["opponent_action"]
        

        if totalCheat > totalCoop or lastMove == Action.COOPERATE:
            action = Action.CHEAT
        else:
            action = Action.COOPERATE

        return action
