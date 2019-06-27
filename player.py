import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface, num: int, color: pygame.Color, start_pos: list):
        """Create new player

        Args:
            screen: pygame screen Surface
            num: number of player (1 or 2)
            color: color of player's rectangle
            start_pos: starting position (width, height)

        """
        super().__init__()
        self.screen = screen
        self.number = num
        self.color = color
        self.location = start_pos
        self.rect = pygame.rect.Rect(self.location)

    def move_down(self):
        """Move player down (keyboard steering)."""
        if self.rect.bottom < self.screen.get_height():
            self.rect.move_ip(0, 5)

    def move_up(self):
        """Move player up (keyboard steering)."""
        if self.rect.top > 0:
            self.rect.move_ip(0, -5)

    def move_mouse(self, off_y: int):
        """Move player rect with mouse

        Args:
            off_y: offset between rect top and mouse click y coord

        """
        mouse_y = pygame.mouse.get_pos()[1]
        if 0 < mouse_y - off_y and mouse_y - off_y + self.rect.height < self.screen.get_height():
            self.rect.y = mouse_y - off_y

    def draw_rect(self):
        """Draw rect on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
