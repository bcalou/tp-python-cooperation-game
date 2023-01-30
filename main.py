from cooperation.game import CooperationGame
from cooperation.player import Player
from cooperation.players.colin import Alpha
from cooperation.players.beta import Beta
from cooperation.players.gamma import Gamma
from cooperation.players.delta import Delta
from cooperation.players.iota import Iota
from cooperation.players.omega import Omega
from cooperation.players.sigma import Sigma
from cooperation.players.kappa import Kappa


def main():
    game = CooperationGame(get_players_list())

    game.play()


def get_players_list() -> list[Player]:
    """Get a list of instanciated players"""
    return [
        Alpha(),
        Beta(),
        Gamma(),
        Delta(),
        Iota(),
        Omega(),
        Sigma(),
        Kappa()
    ]


if __name__ == "__main__":
    main()
