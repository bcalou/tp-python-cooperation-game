from cooperation.player import Player
from cooperation.types import Action


class Baptiste(Player):
    NAME = "Baptiste"

    def play(self, opponent: str) -> Action:
        
        if opponent == "Nathan":
            return Action.CHEAT

        if not self._game_history:
            return Action.COOPERATE
        else:
            last_turn = self._game_history[-1]
            return last_turn["opponent_action"]
