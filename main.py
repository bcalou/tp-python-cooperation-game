import pygame
from cooperation.display import Display
from cooperation.log import Log
from cooperation.game import Game
from cooperation.player import Player
from cooperation.players.alpha import Alpha
from cooperation.players.beta import Beta
from cooperation.players.gamma import Gamma
from cooperation.players.delta import Delta
from cooperation.players.iota import Iota
from cooperation.players.omega import Omega
from cooperation.players.sigma import Sigma
from cooperation.players.kappa import Kappa


def main():
    log = Log()
    players_list = get_players_list(log)
    max_score = get_max_score(players_list)

    display = Display(players_list, max_score)
    game = Game(players_list, log, display)

    game.play()

    display.take_screenshot(log.get_filename())


def get_players_list(log: Log) -> list[Player]:
    """Get a list of instanciated players"""
    return [
        Alpha(log),
        Beta(log),
        Gamma(log),
        Delta(log),
        Iota(log),
        Omega(log),
        Sigma(log),
        Kappa(log)
    ]


def get_max_score(players_list: list[Player]) -> int:
    """Get the theorical maximum score based on the number of players"""

    return Game.TURNS_PER_FIGHT * Game.BETRAYER_WIN * (len(players_list) - 1)


if __name__ == "__main__":
    main()
