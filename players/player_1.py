from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Rats"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        main_action = Action.COOPERATE
        if turn_index == 0:
            return Action.COOPERATE
        elif turn_index == 1:
            return Action.CHEAT
        elif turn_index == 2:
            return Action.COOPERATE
        else:
            three_first_turns = [history[0]["opponent_action"], history[1]["opponent_action"], history[2]["opponent_action"]]
            if Action.CHEAT not in three_first_turns:
                main_action = Action.CHEAT
            elif Action.COOPERATE not in three_first_turns:
                main_action = Action.COOPERATE
            elif (history[0]["opponent_action"] == Action.COOPERATE and history[1]["opponent_action"] == Action.CHEAT and history[2]["opponent_action"] == Action.COOPERATE):
                main_action = main_action = Action.CHEAT
            elif (history[0]["opponent_action"] == Action.CHEAT and history[1]["opponent_action"] == Action.COOPERATE and history[2]["opponent_action"] == Action.CHEAT):
                main_action = main_action = Action.CHEAT
            else:
                main_action = Action.CHEAT
            return main_action
