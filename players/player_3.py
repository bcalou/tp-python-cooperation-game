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
        if len(history) == 0:
            print("Landry: Hey! Devenons amis!")
            return Action.COOPERATE
        elif turn_index >= 8:
            if opponent.name in ["Colsplif", "Bojji", "Lucalixte", "Rats", "YELLOW APPLE"]:
                print("Landry: Promesse respectée!")
                if turn_index == 9:
                    return history[-1]["opponent_action"]
                return Action.COOPERATE
            else:
                print("Landry: AHAHAHAH! Je suis diabolique")
                return Action.CHEAT
        else:
            last_action : Action = history[-1]["opponent_action"]
            if last_action == Action.COOPERATE:
                print("Landry: C'est cool ça, continuons! :)")
            else:
                print("Landry: Héééééé! Pas cool :(")
            if turn_index == 9:
                print("William: Et n'hésite pas à laisser un poce bleu")
            return history[-1]["opponent_action"]
        
