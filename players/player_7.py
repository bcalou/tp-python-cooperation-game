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
        if opponent.name == "Bojji":
            have_cheat : bool = False
            if(turn_index >= 1):
                for i in history:
                    if(i["opponent_action"] == Action.CHEAT):                   
                        have_cheat = True
            if(turn_index == 9):
                return Action.CHEAT
            if(have_cheat):
                return Action.CHEAT
            else:
                return Action.COOPERATE
        elif opponent.name == "Colsplif":
            if(turn_index == 0):
                return Action.COOPERATE
            for i in history:
                    if(i["opponent_action"] == Action.CHEAT):                   
                        have_cheat = True
            if(have_cheat):
                return Action.CHEAT
            else:
                return Action.COOPERATE
        
        elif opponent.name == "Topone":
            
            return Action.CHEAT

        else:
            liste = [Action.COOPERATE, Action.CHEAT]
            if turn_index == 1:
                return Action.CHEAT
            else:
                return random.choice(liste)

