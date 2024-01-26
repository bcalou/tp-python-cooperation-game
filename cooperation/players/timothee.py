from random import random

from cooperation.player import Player
from cooperation.types import Action


class Timothee(Player):
    NAME = "Timothee"

    def play(self, opponent: str) -> Action:
        if opponent == "Ewen": #t'es ban
            return Action.CHEAT

        if len(self._game_history) <= 1:
            return Action.COOPERATE

        avg_action = 0
        for turn in self._game_history:
            if turn["opponent_action"] != Action.CHEAT:
                avg_action += 1
        avg_action /= len(self._game_history)

        if avg_action > 0.2:
            return Action.CHEAT

        return Action.COOPERATE
