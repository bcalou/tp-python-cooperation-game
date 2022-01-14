from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Colsplif"

    def __init__(self):
        self.tonicTurn = 0
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        if opponent.name == "Cooplease":
            return self.classic(history)
        elif opponent.name == "Rats" or opponent.name == "Bojji":
            return Action.CHEAT
        elif opponent.name == "Topone":
            if turn_index == 9:
                return Action.CHEAT
            else:
                return self.classic(history)
        elif opponent.name == "Maxwelle" and turn_index == 0:
            return Action.COOPERATE
        elif opponent.name == "Tonic":
            self.tonicTurn += 1
            for turn in history:
                if turn["opponent_action"] == Action.CHEAT:
                    return Action.CHEAT
            if self.tonicTurn % 2 == 1:
                return Action.COOPERATE
            else:
                return Action.CHEAT
            

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
