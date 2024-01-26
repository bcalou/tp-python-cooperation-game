from cooperation.player import Player
from cooperation.types import Action


class Kayyissa(Player):
    NAME = "Kayyissa"

    def play(self, opponent: str) -> Action:
        cheat: bool = False
        for turn in self._fight_history:
            if turn["opponent_action"] == Action.CHEAT:
                cheat = True
        if cheat:
            return Action.CHEAT
        return Action.COOPERATE
