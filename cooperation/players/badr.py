from cooperation.player import Player
from cooperation.types import Action

class ImprovedBadr(Player):
    NAME = "Badr"

    def __init__(self):
        super().__init__()
        self.history = {}  

    def play(self, opponent: str) -> Action:
        if opponent not in self.history or not self.history[opponent]:
            return Action.COOPERATE
        return self.history[opponent]

    def result(self, opponent: str, my_action: Action, opponent_action: Action, result: int):
        self.history[opponent] = opponent_action
