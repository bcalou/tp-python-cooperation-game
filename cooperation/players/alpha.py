from cooperation.player import Player
from cooperation.types import Action
import random
import time


class Alpha(Player):
    NAME = "Colin"

    def mapValue(self, value: float, inMin: float, inMax: float, outMin: float, outMax: float):
        return outMin + (float(value - inMin) / float(inMax - inMin) * (outMax
                        - outMin))

    def play(self, opponent: str) -> Action:
        reflexionTime: float = self.mapValue(random.random(), 0, 1, 1, 5)
        beginTime: float = time.time()
        currentTime: float = time.time()

        while currentTime - beginTime < reflexionTime:
            self._say("Just thinking, you know")
            currentTime = time.time()

        willCheat: bool = bool(random.getrandbits(1))
        return Action.CHEAT if willCheat else Action.COOPERATE
    