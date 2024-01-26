from cooperation.player import Player
from cooperation.types import Action, Turn


class Theo(Player):
    NAME = "Théo"

    CHEATERS = ["Ewen", "Hugo", "Timothee"]

    def play(self, opponent: str) -> Action:
        if(opponent in self.CHEATERS):
            return Action.CHEAT
        
        if(len(self._game_history) <= 0):
            return Action.COOPERATE

        first_turn: Turn = self._fight_history[0]

        action: Action = first_turn.get("opponent_action")

        return Action.COOPERATE if action == Action.COOPERATE else Action.CHEAT
