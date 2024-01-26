from cooperation.player import Player
from cooperation.types import Action
import time


class Baptiste(Player):
    NAME = "Baptiste"

    def play(self, opponent: str) -> Action:
        current_time = time.perf_counter()

        last_digit = int(str(current_time)[-1])
        if last_digit % 2 == 0:
            return Action.COOPERATE
        else:
            return Action.CHEAT
