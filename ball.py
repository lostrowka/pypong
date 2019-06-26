from typing import List

import pygame

from player import Player


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
        self.start_pos = start_pos
        self.x = self.start_pos[0]
        self.y = self.start_pos[1]
        self.dx = 3
        self.dy = 3

    def move_ball(self):
        self.x += self.dx
        self.y += self.dy

    def detect_collisions(self, player_list: List[Player]):
        """Detect collisions with frame borders

        Args:
            player_list: list of players ([player1, player2]) to detect collisions with

        """
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen.get_height():
            self.dy *= -1
        if self.x - self.radius <= 0:
            self.x = self.start_pos[0]
            self.y = self.start_pos[1]
            self.dx *= -1
            return 2
        if self.x + self.radius >= self.screen.get_width():
            self.x = self.start_pos[0]
            self.y = self.start_pos[1]
            self.dx *= -1
            return 1

        rect1 = player_list[0].rect
        rect2 = player_list[1].rect
        width = self.screen.get_width()
        if self.x - self.radius + self.dx <= 35 < self.x - self.radius and rect1.top < self.y < rect1.bottom:
            self.dx *= -1
        if self.x + self.radius < width - 35 <= self.x + self.radius + self.dx and rect2.top < self.y < rect2.bottom:
            self.dx *= -1
            return 3
        return 0

    def set_speed(self, speed: int):
        """Set speed of ball

        Args:
            speed: new speed of ball

        """
        self.dx = speed if self.dx > 0 else -speed
        self.dy = speed if self.dy > 0 else -speed

    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.radius)

