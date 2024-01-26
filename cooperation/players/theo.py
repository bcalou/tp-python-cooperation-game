from cooperation.player import Player
from cooperation.types import Action, Turn


class Theo(Player):
    NAME = "Théo"

    CHEATERS = ["Ewen", "Hugo", "Timothee"]

    count: int = 0
    round_size: int = 0

    def play(self, opponent: str) -> Action:
        # print(f"{self.round_size} {self.count} {len(self._fight_history)}")
        if self.round_size == 0 and self.count > 0 and len(self._fight_history) == 0 :
            self.round_size = self.count

        self.count += 1

        if(opponent in self.CHEATERS):
            return Action.CHEAT
        
        if(len(self._fight_history) <= 1):
            return Action.COOPERATE

        if len(self._fight_history) >= self.round_size-1 :
            return Action.CHEAT

        first_turn: Turn = self._fight_history[1]

        action: Action = first_turn.get("opponent_action")

        return Action.COOPERATE if action == Action.COOPERATE else Action.CHEAT
