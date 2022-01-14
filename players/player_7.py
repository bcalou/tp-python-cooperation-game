from defs import Action, Turn
import random
class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "YELLOW APPLE"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        liste = [Action.COOPERATE, Action.CHEAT]
        if turn_index == 1:
            return Action.CHEAT
        else:
            return random.choice(liste, p=[0.66,0.33])
