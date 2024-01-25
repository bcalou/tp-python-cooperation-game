from cooperation.display import Display
from cooperation.log import Log
from cooperation.game import Game
from cooperation.player import Player
from cooperation.players.badr import Badr
from cooperation.players.baptiste import Baptiste
from cooperation.players.ewen import Ewen
from cooperation.players.hugo import Hugo
from cooperation.players.joffrey import Joffrey
from cooperation.players.kayyissa import Kayyissa
from cooperation.players.lois import Lois
from cooperation.players.marius import Marius
from cooperation.players.nathan import Nathan
from cooperation.players.theo import Theo
from cooperation.players.timothee import Timothee


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
        Badr(log),
        Baptiste(log),
        Ewen(log),
        Hugo(log),
        Joffrey(log),
        Kayyissa(log),
        Lois(log),
        Marius(log),
        Nathan(log),
        Theo(log),
        Timothee(log)
    ]


def get_max_score(players_list: list[Player]) -> int:
    """Get the theorical maximum score based on the number of players"""

    return Game.TURNS_PER_FIGHT * Game.BETRAYER_WIN * (len(players_list) - 1)


if __name__ == "__main__":
    main()
