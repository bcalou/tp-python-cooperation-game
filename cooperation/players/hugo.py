from cooperation.player import Player
from cooperation.types import Action


class Hugo(Player):
    NAME = "Hugo"

    def play(self, opponent: str) -> Action:

        mother_fuckers: list[str]
        gud_guys: list[str]

        if opponent == "Kayyissa":
            self._say("Sorry mam, life's hard wiv wemen")

        else:
            self._say("F*CK U AHAHAH !!!!!!")

        return Action.CHEAT


def is_gud(str):

    return 0
