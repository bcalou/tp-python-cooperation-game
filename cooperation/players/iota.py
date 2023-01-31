from cooperation.types import Action
from cooperation.player import Player


class Iota(Player):
    NAME = "Lucas"

    def play(self, opponent: 'Player') -> Action:
        """Choose what to do, cheat or cooperate"""
        print(self._fight_history)
        return Action.COOPERATE
