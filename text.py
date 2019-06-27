import pygame


class Text:
    def __init__(self, screen: pygame.Surface, font: str):
        """Init Text object. This class is used to draw texts on screen. It can be divided into score text and
        info texts using different fonts

        Args:
            screen: pygame screen Surface
            font: name of text font used

        """
        self.screen = screen
        self.score_font = pygame.font.SysFont(font, 50)
        self.help_font = pygame.font.SysFont(font, 15)

    def draw_start_screen(self):
        """Draw text for start screen - game name and info."""
        pong = self.score_font.render(f"PONG", 1, (255, 255, 255))
        self.screen.blit(pong, (self.screen.get_width() / 2 - pong.get_width() / 2, self.screen.get_height() / 4))

        # Array of info texts (line by line)
        help_text = ["S - start game", "R - reset game", "P - pause/unpaue", "C - play with computer",
                     "Adjust difficulty in settings", "1-9 - set ball speed"]
        for txt in help_text:
            surf = self.help_font.render(txt, 1, (255, 255, 255))
            self.screen.blit(surf, (self.screen.get_width() / 2 - surf.get_width() / 2, self.screen.get_height() / 2 + help_text.index(txt) * 20))

    def draw_reset_text(self):
        """Draw text after point score."""
        pong = self.help_font.render(f"press any key to continue", 1, (255, 255, 255))
        self.screen.blit(pong, (self.screen.get_width() / 2 - pong.get_width() / 2, self.screen.get_height() / 2 + 20))

    def draw_score(self, score: dict):
        """Draw current score."""
        txt = self.score_font.render(f"{score['player1']}      {score['player2']}", 1, (255, 255, 255))
        self.screen.blit(txt, (self.screen.get_width() / 2 - txt.get_width() / 2, 10))

