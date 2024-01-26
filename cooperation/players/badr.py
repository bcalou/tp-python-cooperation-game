import random
from cooperation.player import Player
from cooperation.types import Action

class Badr(Player):
    NAME = "Badr"
    history = {}
    opponent_history = {}

    INITIAL_COOPERATE_WEIGHT = 0.4
    INITIAL_CHEAT_WEIGHT = 0.6
    FORGIVENESS_CHANCE = 0.1
    ADAPTATION_RATE = 0.05  

    def play(self, opponent: str) -> Action:
        if opponent not in self.history:
            return random.choices(
                [Action.COOPERATE, Action.CHEAT], 
                weights=[self.INITIAL_COOPERATE_WEIGHT, self.INITIAL_CHEAT_WEIGHT], 
                k=1
            )[0]

        if self.detect_pattern(opponent):
            return self.counter_strategy(opponent)
        
        last_opponent_action = self.opponent_history[opponent][-1]
        if last_opponent_action == Action.CHEAT and random.random() < self.FORGIVENESS_CHANCE:
            return Action.COOPERATE
        return last_opponent_action

    def result(self, opponent: str, my_action: Action, opponent_action: Action, result: int):
        if isinstance(opponent_action, Action):
            if opponent not in self.opponent_history:
                self.opponent_history[opponent] = []
            self.opponent_history[opponent].append(opponent_action)
            self.adjust_weights(opponent, my_action, opponent_action, result)
        else:
            raise ValueError("L'action de l'adversaire doit être une instance de Action.")

    def detect_pattern(self, opponent: str) -> bool:
        return False

    def counter_strategy(self, opponent: str) -> Action:
        return Action.COOPERATE

    def adjust_weights(self, opponent: str, my_action: Action, opponent_action: Action, result: int):
        pass