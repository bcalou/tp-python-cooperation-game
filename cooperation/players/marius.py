from cooperation.player import Player
from cooperation.types import Action


class Marius(Player):
    NAME = "Marius"

    def play(self, opponent: str) -> Action:
        
        match opponent:
            case "Badr":
                return Action.COOPERATE
            case "Baptiste":
                return Action.COOPERATE
            case "Ewen":
                return Action.CHEAT
            case "Hugo":
                return Action.CHEAT
            case "Joffrey":
                return Action.CHEAT
            case "Kayyissa":
                return Action.CHEAT
            case "Lois":
                return Action.COOPERATE
            case "Nathan":
                return Action.CHEAT
            case "Theo":
                return Action.COOPERATE
            case "Timothee":
                return Action.CHEAT
            case _:
                return Action.CHEAT

