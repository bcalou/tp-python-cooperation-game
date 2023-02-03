from cooperation.types import Action
from cooperation.player import Player


class Delta(Player):
    NAME = "Wilfried"

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""

        self._say("Be sure who's your partner ;)")

        return Action.COOPERATE if opponent == "Lucas" or opponent == "Jame" else Action.CHEAT
