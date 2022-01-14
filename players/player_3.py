from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Landry et William [Coop cool]"

    def play(turn_index: int, history: list[Turn]) -> Action:
        if len(history) == 0:
            print("Hey! Devenons amis!")
            return Action.COOPERATE
        else:
            last_action : Action = history[-1]["opponent_action"]
            if last_action == Action.COOPERATE:
                print("C'est cool ça, continuons! :)")
            else:
                print("Héééééé! Pas cool :(")
            return history[-1]["opponent_action"]
        
