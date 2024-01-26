import random
from cooperation.player import Player
from cooperation.types import Action

class Badr(Player):
    NAME = "Badr"
    history = {}  
    


    def play(self, opponent: str) -> Action:
        if opponent not in self.history or not self.history[opponent]:
            return random.choices(
                [Action.COOPERATE, Action.CHEAT], 
                weights=[0.4, 0.6], 
                k=1
            )[0]
        
        return self.history[opponent]

    def result(self, opponent: str, my_action: Action, opponent_action: Action, result: int):
        self.history[opponent] = opponent_action
