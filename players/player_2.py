import random
from defs import Action, Turn
from random import randint

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Tonic"

    def play(turn_index: int, history: list[Turn]) -> Action:
        coop_count = 0
        if turn_index >= 2:
            if history[turn_index-2]["opponent_action"] == Action.COOPERATE:
                coop_count += 1
            if history[turn_index-1]["opponent_action"] == Action.COOPERATE:
                coop_count += 1
            if coop_count == 2:
                return Action.CHEAT
            if coop_count == 1:
                return Action.COOPERATE
            else:
                doom = True
        return Action.COOPERATE
