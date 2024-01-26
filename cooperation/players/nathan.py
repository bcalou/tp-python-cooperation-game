from cooperation.player import Player
from cooperation.types import Action


class Nathan(Player):
    NAME = "Nathan"

    def play(self, opponent: str) -> Action:

        cheaters = ["Ewen", "Marius", "Timothee", "Hugo"]

        if opponent in cheaters:
            return Action.CHEAT

        times_cheated = 0
        times_cooperated = 0

        if len(self._fight_history) == 0:
            return Action.COOPERATE

        for turn in self._fight_history:
            if turn["opponent_action"] == Action.CHEAT:
                times_cheated += 1
            else:
                times_cooperated += 1

        # print("times cheated ", opponent, ": ", times_cheated)
        # print("times cooperated ", opponent, ": ", times_cooperated)

        probability_of_cheating = (times_cheated * 100) / len(self._fight_history)
        probability_of_cooperating = (times_cooperated * 100) / len(self._fight_history)

        # print("probability of cheating ", opponent, ": ", probability_of_cheating)
        # print("probability of cooperating ", opponent, ": ", probability_of_cooperating)

        if probability_of_cheating > 0:
            return Action.CHEAT

        return Action.COOPERATE

