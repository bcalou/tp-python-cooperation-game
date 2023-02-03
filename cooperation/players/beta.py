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

        return Action.COOPERATE if cheat_ratio > 0 else Action.CHEAT
