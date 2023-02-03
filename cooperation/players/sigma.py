from cooperation.player import Player
from cooperation.types import Action, Turn
import random


class Sigma(Player):
    NAME = "Pierre"

    def play(self, opponent: str) -> Action:

        self.prepare_new_fight()

        if opponent == 'Lucas' or opponent == 'Jame':
            self._say('Pour toujours avoir triché lors de la dernière partie')
            return Action.CHEAT
            
        else:
            #if self.get_cooperation_percenatage() >=
            return Action.COOPERATE if random.randbytes(1) == 1 else Action.CHEAT
                
            
        

