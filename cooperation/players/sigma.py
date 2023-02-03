from cooperation.player import Player
from cooperation.types import Action, Turn
import random


class Sigma(Player):
    NAME = "Pierre"

    def play(self, opponent: str) -> Action:

        #print(self.get_cooperation_percenatage())
        self.prepare_new_fight()

        #if opponent == 'Lucas' or opponent == 'Jame':
        #    self._say('Pour toujours avoir triché lors de la dernière partie')
        #    return Action.CHEAT
        
        cheat_percenatage: float = 0

        for fight in self._fight_history:
            #print(f"LAST FIGHT OPPONENT ACTION : {self._fight_history[-1]['opponent_action']}")
            if fight['opponent_action'] == Action.CHEAT:
                cheat_percenatage += 10

        if cheat_percenatage > 30:
            return Action.CHEAT
        else:
            return Action.COOPERATE

            
        #
        #else:
        #    if self.get_cooperation_percenatage() 
#
        #    
        #    return Action.COOPERATE if random.randbytes(1) == 1 else Action.CHEAT
        return Action.COOPERATE
        
            


