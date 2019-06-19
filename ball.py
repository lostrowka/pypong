import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface, color: pygame.color, start_pos: list):
        """Create new ball

        Args:
            screen: pygame screen of game
            color: color of player's rectangle
            start_pos: starting position (width, height)

        """
        super().__init__()
        self.screen = screen
        self.color = color
        self.radius = 10
        self.location = start_pos
        self.dx = 0.1
        self.dy = 0.1

    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, self.location, self.radius)

