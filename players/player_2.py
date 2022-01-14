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
        coop_count = 0
        if turn_index == 0:
            self.doom = False
            if opponent.name == "Topone":
                print("pas si tôt !")
                return Action.CHEAT
        if turn_index >= 2:
            if opponent.name == "Rats":
                print("Dératisation en cours")
                self.doom = True
            if opponent.name == "Topone" and turn_index == 2 :
                coop_count += 1
            if self.doom:
                return Action.CHEAT
            if history[turn_index-2]["opponent_action"] == Action.COOPERATE:
                coop_count += 1
            if history[turn_index-1]["opponent_action"] == Action.COOPERATE:
                coop_count += 1
            if coop_count >= 2:
                if opponent.name == "Bojji":
                    return Action.COOPERATE
                return Action.CHEAT
            else:
                print("Vous n'auriez pas dû...")
                self.doom = True
                return Action.CHEAT
        return Action.COOPERATE
