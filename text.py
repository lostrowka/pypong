import pygame


class Text:
    def __init__(self, screen: pygame.Surface, font: str):
        self.screen = screen
        self.score_font = pygame.font.SysFont(font, 50)
        self.help_font = pygame.font.SysFont(font, 15)

    def draw_start_screen(self):
        pong = self.score_font.render(f"PONG", 1, (255, 255, 255))
        self.screen.blit(pong, (self.screen.get_width() / 2 - pong.get_width() / 2, self.screen.get_height() / 4))

        help_text = ["S - start game", "R - reset game", "P - pause/unpaue", "C - play with computer", "Adjust difficulty in settings", "1-9 - set ball speed"]
        for txt in help_text:
            surf = self.help_font.render(txt, 1, (255, 255, 255))
            self.screen.blit(surf, (self.screen.get_width() / 2 - surf.get_width() / 2, self.screen.get_height() / 2 + help_text.index(txt) * 20))

    def draw_reset_text(self):
        pong = self.help_font.render(f"press any key to continue", 1, (255, 255, 255))
        self.screen.blit(pong, (self.screen.get_width() / 2 - pong.get_width() / 2, self.screen.get_height() / 2 + 20))

    def draw_score(self, score: dict):
        txt = self.score_font.render(f"{score['player1']}      {score['player2']}", 1, (255, 255, 255))
        self.screen.blit(txt, (self.screen.get_width() / 2 - txt.get_width() / 2, 10))

