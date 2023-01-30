from cooperation.types import Action, Turn


class Player():
    NAME = "Abstract player"

    def __init__(self):
        self.score = 0
        self.fight_history = []

    def prepare_new_fight(self):
        """Clear the fight history"""
        self.fight_history = []

    def wins(self, value: int):
        """Add to the score"""
        print(f"{self.NAME} gagne {value} pièce(s)")

        self.score += value

    def looses(self, value: int):
        """Removes from the score"""
        print(f"{self.NAME} perd {value} pièce(s)")

        self.score -= value

    def save_turn(self, self_action: Action, opponent_action: Action):
        """Store the given action in the fight history"""
        self.fight_history.append({
            "self_action": self_action,
            "opponent_action": opponent_action
        })

    def play(self, turn_index: int) -> Action:
        """Choose what to do, cheat or cooperate"""
        return Action.COOPERATE
