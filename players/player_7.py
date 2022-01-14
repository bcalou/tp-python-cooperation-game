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
            have_cheat = False
            if(turn_index == 0):
                return Action.COOPERATE
            for i in history:
                    if(i["opponent_action"] == Action.CHEAT):                   
                        have_cheat = True
            if(have_cheat):
                return Action.CHEAT
            else:
                return Action.COOPERATE
        elif opponent.name == "Colsplif":
            have_cheat = False
            if(turn_index == 0):
                return Action.COOPERATE
            for i in history:
                    if(i["opponent_action"] == Action.CHEAT):                   
                        have_cheat = True
            if(have_cheat):
                return Action.CHEAT
            else:
                return Action.COOPERATE

        elif opponent.name == "Maxwelle":
            if(turn_index == 0):
                return Action.COOPERATE
            else:
                return Action.CHEAT
        
        elif opponent.name == "Lucalixte":
            if(turn_index == 0):
                return Action.COOPERATE
            else:
                return Action.CHEAT
        
        elif opponent.name == "Topone":
            
            return Action.CHEAT
        
        elif  opponent.name == "Cooplease":
            return Action.COOPERATE


        else:
            if random.randint(0,2)>1:
                return Action.COOPERATE
            else:
                return Action.CHEAT

            
