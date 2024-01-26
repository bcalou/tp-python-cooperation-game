from cooperation.player import Player
from cooperation.types import Action


class Nathan(Player):
    NAME = "Nathan"

    def play(self, opponent: str) -> Action:
        match opponent:
            case "Hugo":
                return Action.CHEAT
            case "Badr":
                return Action.COOPERATE
            case "Baptiste":
                return Action.CHEAT
            case "Ewen":
                return Action.COOPERATE
            case "Joffrey":
                return Action.COOPERATE
            case "Kayyissa":
                return Action.CHEAT
            case "Lois":
                return Action.COOPERATE
            case "Marius":
                return Action.COOPERATE
            case "Théo":
                return Action.COOPERATE
            case "Timothee":
                return Action.CHEAT
            case _:
                return Action.COOPERATE

        return Action.COOPERATE
