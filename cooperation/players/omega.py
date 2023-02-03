from cooperation.player import Player
from cooperation.types import Action


class Omega(Player):
    NAME = "Antoine"

    _action: Action = Action.COOPERATE
    _current_opponent: Player = ""
    _current_turn: int = -1
    _opponent_previous_actions: list[int] = []

    def play(self, opponent: 'Player') -> Action:

        self._current_turn += 1

        if opponent != self._current_opponent:
            # First turn
            self._current_turn = 0
            self._current_opponent = opponent
            self._opponent_previous_actions = []
            return Action.CHEAT if opponent == "Pierre" else Action.COOPERATE
        else:
            opponent_previous_action = self._get_previous_opponent_action()
            self._fill_opponent_actions_list(opponent_previous_action)

            if self._average_opponent_action() >= 0.75:
                return Action.COOPERATE
            else:
                return Action.CHEAT

    def _get_previous_opponent_action(self) -> Action:
        return self._fight_history[-1]['opponent_action']

    def _fill_opponent_actions_list(self, action: Action):
        if action == Action.CHEAT:
            self._opponent_previous_actions.append(0)
        else:
            self._opponent_previous_actions.append(1)

    def _average_opponent_action(self) -> float:
        average: float = 0
        for action in self._opponent_previous_actions:
            average += action

        average /= self._current_turn
        return average
