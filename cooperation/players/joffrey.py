from cooperation.types import Action
from cooperation.player import Player
import random


class Joffrey(Player):
    NAME = "Joffrey"

    def play(self, opponent: str) -> Action:
        return Action.COOPERATE
    '''
    if(len(self._fight_history)==0){
        return Action.COOPERATE
    }
    return self._fight_history[-1]["opponent_action"];
    '''
