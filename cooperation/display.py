import pygame
from cooperation.player import Player


class Display:
    DISPLAY_WIDTH = 1500
    SCREEN_CENTER = DISPLAY_WIDTH // 2
    DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_WIDTH)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 180, 0)
    RED = (255, 0, 0)
    BLUE = (0, 120, 120)
    MARGIN = 50

    def __init__(self, players: list[Player], maximum_score: int):
        self._players = players
        self._surface = pygame.display.set_mode(self.DISPLAY_SIZE)

        pygame.font.init()
        self._font = pygame.font.SysFont('Arial', 50)

        self._point_width = self.DISPLAY_WIDTH // 2 // maximum_score
        self._player_height = self.DISPLAY_WIDTH // len(self._players)

    def update(self, playing: list[Player]):
        """Show the current game state"""
        self._surface.fill(self.WHITE)

        for index, player in enumerate(self._players):
            self._print_player_infos(player, index, playing)

        pygame.display.flip()

    def take_screenshot(self, filename: str):
        """Take a screenshot"""

        pygame.image.save(self._surface, f"{filename}.png")

    def _print_player_infos(
        self,
        player: Player,
        index: int,
        playing: list[Player]
    ):
        """Print info for the given player"""
        score_bar_width = abs(player.score * self._point_width)

        color = self.GREEN if player.score > 0 else self.RED
        score_bar_x = (
            self.SCREEN_CENTER
            if player.score > 0
            else self.SCREEN_CENTER - score_bar_width
        )

        self._print_score_bar(color, score_bar_x, score_bar_width, index)
        self._print_player_text(player, index, playing)

    def _print_score_bar(
        self,
        color: tuple[int, int, int],
        score_bar_x: int,
        score_bar_width: int,
        index: int
    ):
        """Print a score bar"""
        pygame.draw.rect(
            self._surface,
            color,
            [
                score_bar_x,
                self.MARGIN // 2 + index * self._player_height,
                score_bar_width,
                self._player_height // 2
            ]
        )

    def _print_player_text(
        self,
        player: Player,
        index: int,
        playing: list[Player]
    ):
        """Print the name and the score of the given player"""
        prefix = "--> " if player in playing else ""

        self._print_text(
            f"{prefix}{player.NAME} ({player.get_cooperation_percenatage()})",
            (self.MARGIN, self.MARGIN + index * self._player_height),
            self.BLUE if player in playing else self.BLACK
        )

        self._print_text(
            str(player.score),
            (self.SCREEN_CENTER, self.MARGIN + index * self._player_height),
            self.BLACK
        )

    def _print_text(
        self,
        text: str,
        coordinates: tuple[int, int],
        color: tuple[int, int, int]
    ):
        """Print the given text at the given coordinates"""
        text_surface = self._font.render(text, True, color)

        self._surface.blit(text_surface, coordinates)
