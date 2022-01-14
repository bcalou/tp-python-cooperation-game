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
            print("Désolé, les affaires sont les affaires...")
            return Action.CHEAT
        elif opponent.name == "Rats" or opponent.name == "Bojji":
            return Action.COOPERATE
        elif opponent.name == "Topone":
            return Action.COOPERATE
        elif opponent.name == "Maxwelle":
            return Action.COOPERATE
        elif opponent.name == "Tonic":
            return Action.COOPERATE
        elif opponent.name == "Lucalixte":
            return Action.COOPERATE
        elif opponent.name == "YELLOW APPLE":
            return Action.CHEAT
            
        return Action.COOPERATE
