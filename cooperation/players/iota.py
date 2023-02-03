from cooperation.log import Log
from cooperation.types import Action
from cooperation.player import Player


class Iota(Player):
    NAME = "Lucas"
    turn = 0

    def play(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        
        Iota.turn += 1

        if(Iota.turn <= 3):
            return Action.COOPERATE
        return Action.CHEAT

    def triche(self, opponent: str) -> Action:
        """Choose what to do, cheat or cooperate"""
        
        from cooperation.players import alpha, beta, gamma, delta, kappa, omega, sigma

        faux_log = Log()
        d_players: dict[str, Player]= {}
        d_players[alpha.Alpha.NAME] = alpha.Alpha(faux_log)
        d_players[beta.Beta.NAME] = beta.Beta(faux_log)
        d_players[gamma.Gamma.NAME] = gamma.Gamma(faux_log)
        d_players[delta.Delta.NAME] = delta.Delta(faux_log)
        d_players[kappa.Kappa.NAME] = kappa.Kappa(faux_log)
        d_players[omega.Omega.NAME] = omega.Omega(faux_log)
        d_players[sigma.Sigma.NAME] = sigma.Sigma(faux_log)

        if opponent in d_players:
            return d_players[opponent].play(self.NAME)
        else:
            return Action.CHEAT