from cooperation.log import Log
from cooperation.player import Player
from cooperation.types import Action


class Ewen(Player):
    NAME = "Ewen"

    __threshold: float = 0.6

    def __init__(self, log: Log):
        super().__init__(log)

    def play(self, opponent: str) -> Action:

        if len(self._game_history) == 9:
            self.__threshold = (self.__threshold + (1 - self.__get_opponent_coop())) / 2

        # The man's honest, sorry :)
        if opponent == "Joffrey":
            return Action.CHEAT

        if len(self._game_history) < 3:
            return Action.CHEAT
        elif self.__get_opponent_coop() > self.__threshold:
            return Action.CHEAT
        else:
            return Action.COOPERATE


    def __get_opponent_coop(self) -> float:
        coop: float = 0

        for action in self._game_history:
            coop += 1 if action == Action.COOPERATE else 0

        coop /= len(self._game_history)
        return coop
        

