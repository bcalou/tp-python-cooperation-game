from cooperation.player import Player
from cooperation.types import Action
import random
import time


class Alpha(Player):
    NAME = "Colin"
    _turn: int = 0
    _opponent_is_traitor: bool = False


    def play(self, opponent: str) -> Action:
        self._turn += 1

        if len(self._fight_history) == 0:
            self._opponent_is_traitor = False
            return Action.COOPERATE
        
        if self._fight_history[-1]['opponent_action'] == Action.CHEAT:
            self._say("You bitch !")
            self._opponent_is_traitor = True

        return Action.CHEAT if self._opponent_is_traitor else Action.COOPERATE



        #####################    THINKING DELAY    ############################
        # def mapValue(self, value: float, inMin: float, inMax: float, outMin: float, outMax: float):
        #     return outMin + (float(value - inMin) / float(inMax - inMin) * (outMax
        #                     - outMin))

        # reflexionTime: float = self.mapValue(random.random(), 0, 1, 1, 5)
        # beginTime: float = time.time()
        # currentTime: float = time.time()

        # while currentTime - beginTime < reflexionTime:
        #     self._say("Just thinking, you know")
        #     currentTime = time.time()



        ####################    RANDOM     ####################
        #  willCheat: bool = bool(random.getrandbits(1))
        # return Action.CHEAT if willCheat else Action.COOPERATE
    