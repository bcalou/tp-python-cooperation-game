from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Bojji"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
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
