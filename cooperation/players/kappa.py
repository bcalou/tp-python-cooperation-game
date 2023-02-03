from cooperation.player import Player
from cooperation.types import Action


class Kappa(Player):
    NAME = "Pierre-Baptiste"

    def play(self, opponent: str):
        if opponent == "Jame" or \
                opponent == "Pierre" or \
                opponent == "Lucas":
            return Action.CHEAT

        number_of_fights_seen = 0
        for fight in self._fight_history:
            number_of_fights_seen += 1
            if fight["opponent_action"] == Action.CHEAT:
                has_cheated = True
                self.say_generation(number_of_fights_seen)
                return Action.CHEAT


        return Action.COOPERATE


    def say_generation(self, number_of_fights_seen:int):
        if number_of_fights_seen < len(self._fight_history):
            self._say("Mais pas 1000 fois 1000 personnes")
            return
        self._say("On peut tromper 1 fois 1 personne")
