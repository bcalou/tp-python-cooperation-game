from cooperation.player import Player
from cooperation.types import Action


class Nathan(Player):
    NAME = "Nathan"

    def play(self, opponent: str) -> Action:

        if opponent == "Ewen":
            return Action.CHEAT

        times_cheated = 0
        times_cooperated = 0

        if len(self._fight_history) == 0:
            return Action.CHEAT

        for opponent_action in self._fight_history:
            if opponent_action == Action.CHEAT:
                times_cheated += 1
            else:
                times_cooperated += 1

        probability_of_cheating = (times_cheated * 100) / len(self._fight_history)

        if probability_of_cheating > 50:
            return Action.CHEAT

        return Action.COOPERATE

