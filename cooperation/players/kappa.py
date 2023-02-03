from cooperation.player import Player
from cooperation.types import Action


class Kappa(Player):
    NAME = "Pierre-Baptiste"
    black_list: list[str] =[
        "Jame",
        "Pierre"
        "Lucas"
    ]
    gray_list: list[str] = [

    ]
    def play(self, opponent: str):
        if opponent in self.black_list:
            return Action.CHEAT

        number_of_fights_seen = 0
        for fight in self._fight_history:
            number_of_fights_seen += 1
            if fight["opponent_action"] == Action.CHEAT:
                self.say_generation(number_of_fights_seen)
                return Action.CHEAT
            if number_of_fights_seen == 9:
                return Action.CHEAT


        return Action.COOPERATE


    def say_generation(self, number_of_fights_seen:int):
        if number_of_fights_seen < len(self._fight_history):
            self._say("Mais pas 1000 fois 1 personnes")
            return
        self._say("On peut tromper 1 fois 1 personne")
