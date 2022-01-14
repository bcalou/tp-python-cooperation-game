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
        win: int = 0
        lose: int = 0
        
        if turn_index == 0:
            return Action.COOPERATE
          
        for turn in history:
            if turn["opponent_action"] == Action.CHEAT and turn["self_action"] == Action.COOPERATE:
                lose +=1
            elif turn["self_action"] == Action.CHEAT and turn["opponent_action"] == Action.COOPERATE:
                win +=1
            
        if turn_index == 9 and win <= lose:
            return Action.CHEAT
        elif win > lose:
            return Action.COOPERATE
        elif lose > win:
            return Action.CHEAT
        else:
            return Action.COOPERATE
