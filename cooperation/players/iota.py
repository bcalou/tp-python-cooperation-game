from cooperation.log import Log
from cooperation.types import Action
from cooperation.player import Player


class Iota(Player):
    NAME = "Lucas"
    turn = 0

    d_players: dict[str, Player]= {}

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        
        Iota.turn += 1

        if(Iota.turn <= 3):
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
        if self.turn == 0:
            self.d_players[alpha.Alpha.NAME] = alpha.Alpha(faux_log)
            self.d_players[beta.Beta.NAME] = beta.Beta(faux_log)
            self.d_players[gamma.Gamma.NAME] = gamma.Gamma(faux_log)
            self.d_players[delta.Delta.NAME] = delta.Delta(faux_log)
            self.d_players[kappa.Kappa.NAME] = kappa.Kappa(faux_log)
            self.d_players[omega.Omega.NAME] = omega.Omega(faux_log)
            self.d_players[sigma.Sigma.NAME] = sigma.Sigma(faux_log)

        action: Action = self.d_players[opponent].play(self.NAME)
        self._say(f"Bah alors {opponent}, tu joues {action}")

        if opponent in self.d_players:
            return action
        else:
            return Action.CHEAT