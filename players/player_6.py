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
        have_cheat: bool = False
        if(turn_index == 0):
            print("Salut à vous équipe "+opponent.name)
        match opponent:
            case "Rats":
                return Action.CHEAT
            case "Topone":
                return Action.CHEAT
            case "Tonic":
                if(turn_index == 5):
                    return Action.CHEAT
                else:
                    return self._classicTurn(turn_index, history, have_cheat)
            case "YELLOW APPLE":
                if(turn_index == 1):
                    return Action.CHEAT
                else:
                    return self._classicTurn(turn_index, history, have_cheat)
            case _:
                return self._classicTurn(turn_index, history, have_cheat)

    def _classicTurn(self, turn_index, history, have_cheat):
        if(turn_index >= 1):
            for turn in history:
                if(turn["opponent_action"] == Action.CHEAT):
                    have_cheat = True
        if(turn_index == 9):
            return Action.CHEAT
        if(have_cheat):
            return Action.CHEAT
        else:
            return Action.COOPERATE
