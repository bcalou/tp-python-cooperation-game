import random
from defs import Action, Turn
from random import randint

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Tonic"

    doom: bool = False

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        random_int = randint(1,4)
        if random_int == 1 :
            print('Toi tu crèves')
            return Action.CHEAT
        print("Toi tu vis")
        return Action.COOPERATE