from cooperation.player import Player
from cooperation.types import Action
import random


class Alpha(Player):
    NAME = "Colin"

    def play(self, opponent: str) -> Action:
        willCheat: bool = bool(random.getrandbits(1))
        return Action.CHEAT if willCheat else Action.COOPERATE
