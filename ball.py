from typing import List

import pygame

from player import Player


class Ball(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface, color: pygame.color, start_pos: list):
        """Create new ball

        Args:
            screen: pygame screen Surface
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
        """Move ball for given difference (step in ball's position)"""
        self.x += self.dx
        self.y += self.dy

    def detect_collisions(self, player_list: List[Player]) -> int:
        """Detect collisions with frame borders or players

        Args:
            player_list: list of players ([player1, player2]) to detect collisions with

        Returns:
            1 if player1 scores
            2 if player2 scores
            3 if player2 bounces the ball (used to draw new collision point)
            0 if any other collision or none at all occur (no special actions need to be taken outside the ball obj)

        """
        # window border collisions
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
        # player bars collisions
        if self.x - self.radius + self.dx <= 35 < self.x - self.radius and rect1.top < self.y < rect1.bottom:
            self.dx *= -1
        if self.x + self.radius < width - 35 <= self.x + self.radius + self.dx and rect2.top < self.y < rect2.bottom:
            self.dx *= -1
            return 3
        return 0

    def set_speed(self, speed: int):
        """Set speed of ball (preserve sign)

        Args:
            speed: new speed of ball

        """
        self.dx = speed if self.dx > 0 else -speed
        self.dy = speed if self.dy > 0 else -speed

    def draw_circle(self):
        """Draw ball on screen"""
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.radius)

