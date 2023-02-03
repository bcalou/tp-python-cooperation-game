from cooperation.player import Player
from cooperation.types import Action


class Omega(Player):
    NAME = "Antoine"

    _action: Action = Action.COOPERATE
    _current_opponent: Player = ""
    _current_turn: int = -1
    _opponent_previous_actions: list[Action] = []

    def play(self, opponent: 'Player') -> Action:

        self._current_turn += 1
        print(self._current_opponent)

        if opponent != self._current_opponent:
            self._current_turn = 0
            self._current_opponent = opponent
            return Action.CHEAT
        else:
            opponent_previous_action = self._get_previous_opponent_action()
            self._opponent_previous_actions.append(opponent_previous_action)
            return opponent_previous_action

    def _get_previous_opponent_action(self) -> Action:
        return self._fight_history[-1]['opponent_action']
