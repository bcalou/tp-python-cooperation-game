from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Colsplif"

    def play(turn_index: int, history: list[Turn]) -> Action:
        if turn_index == 9:
            return Action.CHEAT
        for turn in history:
            if turn["opponent_action"] == Action.CHEAT:
                return Action.CHEAT
        return Action.COOPERATE
