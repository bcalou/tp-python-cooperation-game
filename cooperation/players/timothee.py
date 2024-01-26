from cooperation.player import Player
from cooperation.types import Action


class Timothee(Player):
    NAME = "Timothee"

    def play(self, opponent: str) -> Action:
        return Action.CHEAT
        if len(self._game_history) == 0:
            return Action.CHEAT

        avg_action = 0
        for turn in self._game_history:
            avg_action += 0 if turn["opponent_action"] == Action.CHEAT else 1
        avg_action /= len(self._game_history)

        if avg_action < 0.5:
            return Action.CHEAT

        return Action.COOPERATE





