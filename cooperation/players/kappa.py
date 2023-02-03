from cooperation.player import Player
from cooperation.types import Action


class Kappa(Player):
    NAME = "Pierre-Baptiste"

    def play(self, opponent: str):
        print(opponent)
        if opponent == "Jame" or opponent == "Lucas":
            return Action.CHEAT
        else:
            has_cheated: bool = False
            for fight in self._fight_history:
                if fight["opponent_action"] == Action.CHEAT:
                    has_cheated = True
                    self._say("On peut tromper 1 fois 1 personne")
                    break

            return Action.CHEAT if has_cheated else Action.COOPERATE


