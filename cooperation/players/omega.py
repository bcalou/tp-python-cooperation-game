from cooperation.player import Player
from cooperation.types import Action


class Omega(Player):
    NAME = "Antoine"

    Action = Action.COOPERATE

    def play(self, opponent: 'Player') -> Action:
        return Action.COOPERATE

    def average_previous(self):
        for previous_opponent in self._fight_history:
            Action = previous_opponent["opponent_action"]

