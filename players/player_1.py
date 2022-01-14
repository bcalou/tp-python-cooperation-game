from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Player 1"

    def play(turn_index: int, history: list[Turn]) -> Action:
        main_action = Action.COOPERATE
        if turn_index == 1:
            return Action.COOPERATE
        elif turn_index == 2:
            return Action.CHEAT
        elif turn_index == 3:
            return Action.COOPERATE
        else:
            three_first_turns = [history[0]["opponent_action"], history[1]["opponent_action"], history[2]["opponent_action"]]
            if Action.CHEAT not in three_first_turns:
                main_action = Action.CHEAT
            elif Action.COOPERATE not in three_first_turns:
                main_action = Action.COOPERATE
            elif (history[0]["opponent_action"] == Action.COOPERATE and history[1]["opponent_action"] == Action.CHEAT and history[2]["opponent_action"] == Action.COOPERATE):
                if turn_index % 2 == 0:
                    main_action = main_action = Action.CHEAT
                else:
                    main_action = main_action = Action.COOPERATE
            return main_action
