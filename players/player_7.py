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
            return Action.COOPERATE
        elif opponent.name == "Colsplif":
            return Action.CHEAT

        elif opponent.name == "Maxwelle":
            return Action.COOPERATE
        
        elif opponent.name == "Lucalixte":
            return Action.CHEAT
            
        
        elif opponent.name == "Topone":
            
            return Action.COOPERATE
        
        elif  opponent.name == "Cooplease":
            return Action.COOPERATE


        else:
            return Action.COOPERATE

            
