from cooperation.player import Player
from cooperation.types import Action


class Beta(Player):
    NAME = "Jame"

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        cheat_ratio = 0
        if opponent == "Lucas":
            return Action.CHEAT

        for game in self._fight_history:
            last_oponent_action = game["opponent_action"]
            if last_oponent_action == Action.CHEAT:
                cheat_ratio += 1

        fight_number = len(self._fight_history) + 1

        if fight_number == 10:
            print(f"Good Game {opponent} see you next time")

        return Action.COOPERATE if cheat_ratio > 0 else Action.CHEAT
