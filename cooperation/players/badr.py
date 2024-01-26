from cooperation.player import Player
from cooperation.types import Action
import random

class Badr(Player):
    NAME = "Badr"
    history = {}
    opponent_history = {}

    INITIAL_COOPERATE_WEIGHT = 0.4
    INITIAL_CHEAT_WEIGHT = 0.6
    FORGIVENESS_CHANCE = 0.1 

    def play(self, opponent: str) -> Action:
        if opponent not in self.history:
            return random.choices(
                [Action.COOPERATE, Action.CHEAT], 
                weights=[self.INITIAL_COOPERATE_WEIGHT, self.INITIAL_CHEAT_WEIGHT], 
                k=1
            )[0]

        last_opponent_action = self.opponent_history[opponent][-1]
        if last_opponent_action == Action.CHEAT and random.random() < self.FORGIVENESS_CHANCE:
            return Action.COOPERATE
        return last_opponent_action

    def result(self, opponent: str, my_action: Action, opponent_action: Action, result: int):
        if isinstance(opponent_action, Action):
            if opponent not in self.opponent_history:
                self.opponent_history[opponent] = []
            self.opponent_history[opponent].append(opponent_action)
        else:
            raise ValueError("L'action de l'adversaire doit être une instance de Action.")

