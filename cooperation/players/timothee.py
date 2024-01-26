from cooperation.player import Player
from cooperation.types import Action


class Timothee(Player):
    NAME = "Timothee"

    def play(self, opponent: str) -> Action:
        if len(self._game_history) == 0:
            return Action.COOPERATE

        if len(self._game_history) > 7:
            return Action.CHEAT

        avg_action = 0
        for turn in self._game_history:
            if turn["opponent_action"] != Action.CHEAT:
                avg_action += 1
        avg_action /= len(self._game_history)

        if avg_action > 0.5:
            return Action.CHEAT

        return Action.COOPERATE
