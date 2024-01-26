from cooperation.player import Player
from cooperation.types import Action


class Marius(Player):
    NAME = "Marius"

    def play(self, opponent: str) -> Action:
        
        print("big flemme d'aller lire les autres fonctions jvais rentrer dans vos têtes")
        match opponent:
            case "Badr":
                return Action.CHEAT
            case "Baptiste":
                return Action.CHEAT
            case "Ewen":
                return Action.CHEAT
            case "Hugo":
                return Action.COOPERATE
            case "Joffrey":
                return Action.COOPERATE
            case "Kayyissa":
                return Action.COOPERATE
            case "Loïs":
                return Action.CHEAT
            case "Nathan":
                return Action.CHEAT
            case "Théo":
                return Action.COOPERATE
            case "Timothee":
                return Action.CHEAT
            case _:
                return Action.CHEAT

