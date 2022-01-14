from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Colsplif"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        if opponent.name == "YELLOW APPLE" or opponent.name == "Cooplease":
            return self.classic(history)
        elif opponent.name == "Rats" or opponent.name == "Bojji":
            return Action.CHEAT
        elif opponent.name == "Topone":
            if turn_index == 0 or turn_index == 9:
                return Action.CHEAT
            else:
                return self.classic(history)
        elif opponent.name == "Maxwelle":
            if turn_index == 0:
                return Action.COOPERATE
            elif turn_index == 9:
                return Action.CHEAT
            else:
                return self.classic(history)

        if turn_index == 9:
            return Action.CHEAT
        for turn in history:
            if turn["opponent_action"] == Action.CHEAT:
                return Action.CHEAT
        return Action.COOPERATE

    def classic(self, history: list[Turn]):
        for turn in history:
            if turn["opponent_action"] == Action.CHEAT:
                return Action.CHEAT
        return Action.COOPERATE
