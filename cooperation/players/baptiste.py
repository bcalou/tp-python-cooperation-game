from cooperation.player import Player
from cooperation.types import Action


class Baptiste(Player):
    NAME = "Baptiste"

    def play(self, opponent: str) -> Action:
        if len(self._fight_history) < 10:
            return Action.COOPERATE
        else:
            recent_fights = self._fight_history[-10:]
            cheat_count = sum(turn["opponent_action"] == Action.CHEAT for turn in recent_fights)
            if cheat_count > 5:
                return Action.CHEAT
            else:
                return Action.COOPERATE