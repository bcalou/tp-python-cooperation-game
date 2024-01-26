from cooperation.player import Player
from cooperation.types import Action


class Badr(Player):
    NAME = "Badr"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
    
    def play(self, opponent: str) -> Action:
        return self.last_opponent_action

    def result(self, opponent: str, my_action: Action, opponent_action: Action, result: int):
        self.last_opponent_action = opponent_action
