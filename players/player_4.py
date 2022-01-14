from defs import Action, Turn, random

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Lucalixte"

    def play(turn_index: int, history: list[Turn]) -> Action:
        print("history", history)
        number = random.randint(0, 1)
        if number == 0:
            return Action.COOPERATE
        else :
            return Action.CHEAT
