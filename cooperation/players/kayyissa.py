from cooperation.player import Player
from cooperation.types import Action


class Kayyissa(Player):
    NAME = "Kayyissa"

    def play(self, opponent: str) -> Action:

        cheat: bool = True
        for turn in self._fight_history:
            if turn["opponent_action"] == Action.COOPERATE:
                cheat = False

        if cheat:
            self._say("déso fallait être gentil")
            return Action.CHEAT

        self._say("déso pour la première fois")
        return Action.COOPERATE
