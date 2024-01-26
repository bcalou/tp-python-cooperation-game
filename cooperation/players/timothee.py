from cooperation.player import Player
from cooperation.types import Action


class Timothee(Player):
    NAME = "Timothee"

    def play(self, opponent: str) -> Action:
        match opponent:
            case "Badr":
                return Action.COOPERATE
            case "Baptiste":
                return Action.CHEAT
            case "Ewen":
                return Action.COOPERATE
            case "Hugo":
                return Action.CHEAT
            case "Joffrey":
                return Action.CHEAT
            case "Kayyissa":
                return Action.CHEAT
            case "Lois":
                return Action.COOPERATE
            case "Marius":
                return Action.CHEAT
            case "Nathan":
                return Action.COOPERATE
            case "Theo":
                return Action.COOPERATE
        return Action.COOPERATE

