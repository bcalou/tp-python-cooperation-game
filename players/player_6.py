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
        if(opponent.name == "Rats"):
            return self._classicTurn(turn_index, history, have_cheat, True)
        if(opponent.name == "Cooplease"):
            return self._classicTurn(turn_index, history, have_cheat, True)
        if(opponent.name == "Lucalixte"):
            return self._classicTurn(turn_index, history, have_cheat, True)
        if(opponent.name == "YELLOW APPLE"):
            return self._classicTurn(turn_index, history, have_cheat, True)
        if(opponent.name == "Colsplif"):
            print("Bande de copiteur !!!")
            return Action.CHEAT
        if(opponent.name == "Topone"):
            print("Alors comme ça on essaie de nous anarquer ?!")
            return Action.CHEAT
        if(opponent.name == "Tonic"):
            if(turn_index >= 2):
                return Action.CHEAT
            else:
                return Action.COOPERATE
        return self._classicTurn(turn_index, history, have_cheat, False)

    def _classicTurn(self, turn_index, history, have_cheat, friend):
        if(turn_index >= 1):
            for turn in history:
                if(turn["opponent_action"] == Action.CHEAT):
                    have_cheat = True
        if(turn_index == 9 and not friend):
            return Action.CHEAT
        if(have_cheat):
            return Action.CHEAT
        else:
            return Action.COOPERATE
