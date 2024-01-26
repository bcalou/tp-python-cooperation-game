import random
from cooperation.player import Player
from cooperation.types import Action

class Badr(Player):
    NAME = "Badr"
    history = {}

    INITIAL_COOPERATE_WEIGHT = 0.4
    INITIAL_CHEAT_WEIGHT = 0.6

    def play(self, opponent: str) -> Action:

        if opponent not in self.history:
            return random.choices(
                [Action.COOPERATE, Action.CHEAT], 
                weights=[self.INITIAL_COOPERATE_WEIGHT, self.INITIAL_CHEAT_WEIGHT], 
                k=1
            )[0]
        
        return self.history[opponent]

    def result(self, opponent: str, my_action: Action, opponent_action: Action, result: int):
        if isinstance(opponent_action, Action):
            self.history[opponent] = opponent_action
        else:
            raise ValueError("L'action de l'adversaire doit être une instance de Action.")

