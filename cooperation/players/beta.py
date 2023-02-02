from cooperation.player import Player
from cooperation.types import Action


class Beta(Player):
    NAME = "Jame"

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        cheat_ratio = 0
        for game in self._game_history:
            if game["opponent_action"] == 0:
                cheat_ratio += 1
            else:
                cheat_ratio -= 1
        return Action.COOPERATE if cheat_ratio > 0 else Action.CHEAT
