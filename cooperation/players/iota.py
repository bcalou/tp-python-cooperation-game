from cooperation.types import Action
from cooperation.player import Player


class Iota(Player):
    NAME = "Lucas"

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        return Action.CHEAT