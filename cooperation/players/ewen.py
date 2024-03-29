from cooperation.log import Log
from cooperation.player import Player
from cooperation.types import Action


class Ewen(Player):
    NAME = "Ewen"

    def __init__(self, log: Log):
        super().__init__(log)

    def play(self, opponent: str) -> Action:
        # The unicorn algorithm 🦄
        #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⠀⢳⠀⢀⣀⣀⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠙⢻⣿⣿⣯⣉⠀⠉⠉⠛⠷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⢦⡀⠀⣿⡟⢮⣝⠻⣦⡆⠀⠀⣤⡙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⣠⣤⡀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⡇⠀⠉⠙⣿⡇⠀⠙⢷⣌⠻⣆⠀⠘⣷⣄⢹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⢰⠋⠀⠉⠳⣄⣠⣴⣾⣯⣍⡙⠛⠻⢿⣷⡶⣤⣿⡇⠀⠀⠀⠻⣆⠹⣧⠀⢻⣿⡄⠚⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⡼⠀⡀⠀⠀⠙⢿⣿⠈⢻⣏⠉⠳⣤⡀⠈⠻⢦⡉⠋⣦⠀⠀⠀⢹⣇⢻⡆⢸⡇⢿⡄⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⡇⠀⢧⠀⠀⠀⠀⠙⢧⡀⢻⣆⠀⠈⢷⡄⠀⠀⢻⣄⠘⣧⡀⠀⣀⣿⣾⣷⣼⣧⣼⣷⣶⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⣷⠀⠸⡀⠀⠀⠀⠀⠈⢿⡄⢻⡆⠀⠈⣷⠀⠀⠀⣻⣤⣴⣿⣿⣿⣿⡟⠋⠉⠹⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠸⡆⠀⢳⡀⠀⠀⠀⠀⢸⣿⠈⣿⠀⠀⣹⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠙⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⢳⡀⠀⠓⢄⣤⣶⣿⣿⣿⠁⣹⣷⡿⠟⠉⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠈⠻⣿⣿⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⢳⣤⣶⣿⣿⣿⣿⣿⣿⣶⣿⣿⣦⡀⠀⠀⠠⣶⣿⣿⣿⣿⠘⢿⣿⣿⣿⣿⣆⠀⠀⣸⡟⣠⠈⢻⡄⠀⠀⠀⠀⠀⠀
        #⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠻⣿⣿⣿⡟⠀⠈⠻⣿⣿⣿⣿⣧⣼⣿⠞⠁⠀⠀⠹⣆⠀⠀⠀⠀⠀
        #⣴⣾⣿⣿⡿⠿⣿⣿⡉⠁⠀⠻⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⢙⡿⠁⠀⠀⠀⠈⠉⠙⣿⠹⠋⠁⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀
        #⢹⣿⣿⣿⠄⠀⢸⡟⣧⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣦⣴⠟⠁⠀⠀⠀⠀⠙⠁⣰⠟⢦⡀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀
        #⠀⠻⣿⡿⠀⠀⠈⣧⠹⣧⠀⠀⠀⠀⠈⠛⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠴⠒⢒⣶⠏⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀
        #⠀⠀⠀⠀⠀⠀⠀⢻⡀⠹⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠟⠁⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠈⢻⡄
        #⠀⠀⠀⠀⠀⠀⠀⢸⣧⣴⠊⠿⣿⣦⡀⠀⠠⡤⠤⠤⠤⠤⠴⠖⢲⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠷⣄⠀⠀⠀⠀⠀⢀⣿
        #⠀⠀⠀⠀⠀⠀⠀⠘⣏⣿⠀⢰⡈⠉⠛⠛⠛⢿⡆⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⠀⠀⠙⠂⠀⠀⣠⡾⠃
        #⠀⠀⠀⠀⠀⠀⠀⢠⡷⣿⡆⠈⢿⣶⣄⡀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠘⢧⡀⢀⡠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠉⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⢸⣧⠹⣇⠀⠀⠻⣿⣿⣷⣾⣽⣷⡀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠞⠋⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠙⣦⡀⠀⠈⠛⢷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⣀⣀⣠⡤⠴⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⠀⣿⣞⢷⡈⢷⡀⠀⠈⠀⠈⠙⠛⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⢯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡜⢳⡄⠹⣆⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⢠⡄⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣟⠹⣦⡈⢷⣄⠀⠀⢀⣼⣿⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        #⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣞⣷⣄⠙⢧⣠⣼⣿⣿⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⣿⠀⠀
        # Feel free to propose possible optimisations
        return Action.CHEAT