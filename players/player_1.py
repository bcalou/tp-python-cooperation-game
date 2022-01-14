from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Rats"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        if opponent == "Colsplif" or opponent == "Bojji" or opponent == "Cooplease":
            print("Coopérons comme prévu :")
            if turn_index > 0 and history[turn_index - 1]["opponent_action"] == Action.CHEAT:
                print("Les Rats ont le sens de l'honneur mais ne sont pas naïfs !")
                return Action.CHEAT
            else:
                if turn_index == 9:
                    print("Nous restont tout de même des Rats. Sheesh.")
                    return Action.CHEAT
                else:
                    return Action.COOPERATE


        if opponent == "Tonic" or opponent == "Topone":
            print("Malgré vos grands discourts... les Rats vaincront !")


        if turn_index == 0:
            return Action.CHEAT
        elif turn_index == 1:
            return Action.COOPERATE
        
        elif turn_index > 2:
            if history[1]["opponent_action"] == Action.CHEAT:
                return Action.CHEAT
            else:
                return Action.COOPERATE
        else:
            return Action.COOPERATE
