from defs import Action, Turn
import random

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Topone"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        #punch=
        if (opponent.name=="Rats" or opponent.name=="Bojji") :
            print("Bande de rats. Les rats ne vaincront pas.")
            return Action.CHEAT
        elif (turn_index==0) :
            print("Top 0 même au dessus du top 1")
            return Action.CHEAT
        else :
            if (history[turn_index-1]["opponent_action"]== Action.CHEAT) :
                return Action.CHEAT
            else :
                print("Que de l'amour pour mon Top 1")
                return Action.COOPERATE
