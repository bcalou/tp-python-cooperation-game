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
        if(turn_index == 0):
            print("Salut à vous équipe "+opponent.name+" on est une équipe sympa <3")
        return Action.COOPERATE
