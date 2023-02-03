from cooperation.log import Log
from cooperation.types import Action
from cooperation.player import Player


class Iota(Player):
    NAME: str = "Lucas"
    banned: list[str] = []

    d_players: dict[str, Player]= {}

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""

        # Système de bannissement
        if len(self._fight_history) > 0:
            last_turn = self._fight_history[-1]
            if last_turn["opponent_action"] == Action.CHEAT:
                self.banned.append(opponent)

        if opponent in self.banned:
            return Action.CHEAT

        if len(self._fight_history) <= 5: # Faire croire qu'on coopère au début
            return Action.COOPERATE

        return Action.CHEAT

    def triche(self, opponent: str) -> Action:
        """Avec cette méthode, je prévois l'action de mon adversaire, et je joue
        comme lui. La coopération fait avancer tout le monde, mais la seule
        réponse à la triche est la triche.
        Pour une triche, on remarque que ce n'est pas si efficace que ça, car
        cette "triche" ne permet pas de gagner plus d'argent que les autres,
        mais simplement de pas en perdre. Des améliorations sont à venir.
        """
        
        from cooperation.players import alpha, beta, gamma, delta, kappa, omega, sigma

        faux_log: Log = Log()
        if (self._fight_history) == 0:
            self.d_players[alpha.Alpha.NAME] = alpha.Alpha(faux_log)
            self.d_players[beta.Beta.NAME] = beta.Beta(faux_log)
            self.d_players[gamma.Gamma.NAME] = gamma.Gamma(faux_log)
            self.d_players[delta.Delta.NAME] = delta.Delta(faux_log)
            self.d_players[kappa.Kappa.NAME] = kappa.Kappa(faux_log)
            self.d_players[omega.Omega.NAME] = omega.Omega(faux_log)
            self.d_players[sigma.Sigma.NAME] = sigma.Sigma(faux_log)

        action: Action = self.d_players[opponent].play(self.NAME)
        self._say(f"{opponent} va jouer {action}. Je suis ma stratégie")

        if opponent in self.d_players:
            return action if len(self._fight_history) < 3 else Action.CHEAT
        else:
            return Action.CHEAT