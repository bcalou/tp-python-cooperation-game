from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Cooplease"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        if opponent.name == "Rats":
            print("\033[93mWilliam: AHAHAHAH! Bien fait!\033[0m")
            return Action.CHEAT
        else:
            if len(history) == 0:
                print("\033[93mLandry: Hey! Devenons amis!\033[0m")
                return Action.COOPERATE
            elif turn_index >= 8:
                if opponent.name == "Colsplif":
                    print("\033[93mLandry: Promesse respectée!\033[0m")
                    return Action.COOPERATE
                else:
                    print("\033[93mLandry: AHAHAHAH! Je suis diabolique\033[0m")
                    return Action.CHEAT
            else:
                last_action : Action = history[-1]["opponent_action"]
                if last_action == Action.COOPERATE:
                    print("\033[93mLandry: C'est cool ça, continuons! :)\033[0m")
                else:
                    print("\033[93mLandry: Héééééé! Pas cool :(\033[0m")
                if turn_index == 9:
                    print("\033[93mWilliam: Et n'hésite pas à laisser un poce bleu\033[0m")
                return history[-1]["opponent_action"]
        
