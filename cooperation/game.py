import random
from cooperation.player import Player
from cooperation.types import Action


class CooperationGame:
    TURNS_PER_FIGHT = 10
    COOPERATION_WIN = 2
    BETRAYER_WIN = 3
    BETRAYED_LOSS = 1

    def __init__(self, players: list[Player]):
        self._players = players

    def play(self):
        """Run the tournament"""
        random.shuffle(self._players)

        # This double for loop results in every duel necessary
        for player_index, player_a in enumerate(self._players):
            for _, player_b in enumerate(self._players[player_index + 1:]):
                self._fight(player_a, player_b)

    def _fight(self, player_a: Player, player_b: Player):
        """Make two player fight for N turn"""
        print("\n\n==================================================")
        print(f"{player_a.NAME} VS {player_b.NAME}")
        print("==================================================")

        player_a.prepare_new_fight()
        player_b.prepare_new_fight()

        for turn_index in range(self.TURNS_PER_FIGHT):
            print(f"\nROUND {turn_index + 1}")

            self._fight_turn(player_a, player_b, turn_index)

    def _fight_turn(self, player_a: Player, player_b: Player, turn_index: int):
        """Compare both player actions for a turn"""
        player_a_action = self._get_player_action(player_a, turn_index)
        player_b_action = self._get_player_action(player_b, turn_index)

        if player_a_action == player_b_action == Action.COOPERATE:
            self._cooperate(player_a, player_b)
        elif player_a_action == player_b_action == Action.CHEAT:
            self._cheat(player_a, player_b)
        else:
            self._betray(player_a, player_b, player_a_action)

        player_a.save_turn(player_a_action, player_b_action)
        player_b.save_turn(player_b_action, player_a_action)

    def _get_player_action(self, player: Player, turn_index: int):
        """Get the action for the given player, defaulting to cooperation"""
        try:
            return player.play(turn_index)
        except ValueError:
            print(f"Erreur d'éxecution pour {player.NAME}")
            return Action.COOPERATE

    def _cooperate(self, player_a: Player, player_b: Player):
        """The two players cooperate, both win"""
        print(f"{player_a.NAME} et {player_b.NAME} coopèrent")

        player_a.wins(self.COOPERATION_WIN)
        player_b.wins(self.COOPERATION_WIN)

    def _cheat(self, player_a: Player, player_b: Player):
        """The two player cheat, both loose"""
        print(f"{player_a.NAME} et {player_b.NAME} ont triché tous les deux…")

    def _betray(self, player_a: Player, player_b: Player, action: Action):
        """One player betrays the other and take its money"""
        if action == Action.CHEAT:
            print(f"{player_a.NAME} a trahi {player_b.NAME} !")

            player_a.wins(self.BETRAYER_WIN)
            player_b.looses(self.BETRAYED_LOSS)

        else:
            print(f"{player_b.NAME} a trahi {player_a.NAME} !")

            player_b.wins(self.BETRAYER_WIN)
            player_a.looses(self.BETRAYED_LOSS)
