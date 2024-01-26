from cooperation.player import Player
from cooperation.types import Action, Turn


class Theo(Player):
    NAME = "Théo"

    def play(self, opponent: str) -> Action:
        if(len(self._game_history) <= 0):
            return Action.COOPERATE

        first_turn: Turn = self._game_history[0]
        print(first_turn)

        action: Action = first_turn.get("opponent_action")
        print("Action", action)

        return Action.COOPERATE if action == Action.COOPERATE else Action.CHEAT
