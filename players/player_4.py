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
            if turn_index == 9:
                    return Action.CHEAT
            return Action.COOPERATE
        elif opponent.name == "Topone":
                return Action.CHEAT
        elif opponent.name == "YELLOW APPLE":
            if turn_index == 9:
                    return Action.CHEAT
            return Action.COOPERATE
        elif opponent.name == "Bojji":
            if turn_index == 9:
                    return Action.CHEAT
            return Action.COOPERATE
        elif opponent.name == "Rats":
            return Action.CHEAT
        elif opponent.name == "Maxwelle":
            if turn_index == 9:
                    return Action.CHEAT
            return Action.COOPERATE
        elif opponent.name == "Colsplif":
            if turn_index == 9:
                    return Action.CHEAT
            return Action.COOPERATE
        have_cheat : bool = False
        elif opponent.name == "Tonic":
            return Action.CHEAT
        else:
            Action.CHEAT
