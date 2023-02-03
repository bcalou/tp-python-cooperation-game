from cooperation.types import Action, Turn
from cooperation.log import Log
import random


class Player():
    NAME = "Abstract player"

    def __init__(self, log: Log):
        self.score = 0
        self._log = log
        self._game_history: list[Turn] = []
        self._fight_history: list[Turn] = []

    def prepare_new_fight(self):
        """Clear the fight history"""
        self._fight_history = []

    def wins(self, value: int):
        """Add to the score"""
        self._log.add(f"{self.NAME} gagne {value} pièce(s)")

        self.score += value

    def looses(self, value: int):
        """Removes from the score"""
        self._log.add(f"{self.NAME} perd {value} pièce(s)")

        self.score -= value

    def get_cooperation_percenatage(self) -> str:
        """Get the percentage of turn where the player cooperated"""

        if len(self._game_history) == 0:
            return "..."

        cooperation_count = len(list(filter(
            lambda turn: turn["self_action"] == Action.COOPERATE,
            self._game_history
        )))

        return f"{int(cooperation_count / len(self._game_history) * 100)}%"

    def save_turn(self, self_action: Action, opponent_action: Action):
        """Store the given action in the fight history"""
        turn: Turn = {
            "self_action": self_action,
            "opponent_action": opponent_action
        }

        self._fight_history.append(turn)
        self._game_history.append(turn)

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        return Action.COOPERATE

    def _say(self, message: str):
        """Say something that will be stored in the log"""
        self._log.add(f"{self.NAME} dit: {message}")
