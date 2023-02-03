from cooperation.types import Action
from cooperation.player import Player


class Delta(Player):
    NAME = "Wilfried"

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        return Action.CHEAT if opponent == "Lucas" or opponent == "Jame" else Action.COOPERATE
