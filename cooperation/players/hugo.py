from cooperation.player import Player
from cooperation.types import Action
import random


class Hugo(Player):
    NAME = "Hugo"

    def play(self, opponent: str) -> Action:

        mother_fuckers: list[str]
        gud_guys: list[str]

        cool_score: float = self.get_cool_score()

        if cool_score >= 0.65:

            return (random.choices([Action.CHEAT, Action.COOPERATE], [0.1, 0.9])[0])

        else:

            self._say("U smart a**, waddya think u doin ?")

            return Action.CHEAT

    def get_ennemy_cool_score(self) -> float:

        cool_factor = 0

        for i in self._fight_history:
            if i.opponent_action == Action.COOPERATE:

                cool_factor += 1

        return cool_factor/len(self._fight_history)

    def get_my_cool_score(self, ennemy_cool_score):
        return 0
