from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Topone"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        if (turn_index==0) :
            return Action.CHEAT
        else :
            if (Turn.opponent_action[turn_index-1] == Action.CHEAT) :
                return Action.CHEAT
            else :
                return Action.COOPERATE
