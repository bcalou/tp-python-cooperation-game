from defs import Action, Turn
from random import randint

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Maxwelle"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        return Action.COOPERATE if randint(0,1) == 1 else Action.CHEAT
