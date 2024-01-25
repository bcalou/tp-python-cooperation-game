from cooperation.player import Player
from cooperation.types import Action


class Hugo(Player):
    NAME = "Hugo"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
