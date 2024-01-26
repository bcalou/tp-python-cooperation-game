from cooperation.player import Player
from cooperation.types import Action


class Marius(Player):
    NAME = "Marius"

    def play(self, opponent: str) -> Action:
        
        match opponent:
            case "Bader":
                return Action.COOPERATE
            case "Baptist":
                return Action.COOPERATE
            case "Ewenn":
                return Action.COOPERATE
            case "Hugoo":
                return Action.COOPERATE
            case "Goffrey":
                return Action.COOPERATE
            case "Kayyyissa":
                return Action.COOPERATE
            case "Loisse":
                return Action.COOPERATE
            case "Natan":
                return Action.COOPERATE
            case "Theo":
                return Action.COOPERATE
            case "Timotee":
                return Action.COOPERATE
            case _:
                return Action.CHEAT

