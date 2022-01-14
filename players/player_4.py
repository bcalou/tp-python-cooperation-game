from defs import Action, Turn
import random

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Lucalixte"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        if opponent.name == "Cooplease":
            return Action.CHEAT
        elif opponent.name == "YELLOW APPLE":
            return Action.CHEAT
        elif opponent.name == "Bojji":
            return Action.CHEAT
        elif opponent.name == "Maxwelle":
            return Action.CHEAT
        else:
            Action.COOPERATE
