from configparser import ConfigParser

import numpy as np
import pygame

from ball import Ball
from player import Player
from text import Text


class Game:
    def __init__(self, screen: pygame.Surface, config: ConfigParser):
        """Init game

        1. Create player objects
        2. Create ball object
        3. Create text object
        4. Set score to 0:0

        Args:
            screen: pygame screen Surface
            config: config parser with game configuration options

        """
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.bar_width = int(config['DEFAULT']['Bar width'])

        self.player1 = Player(screen, 1, pygame.Color('blue'), [20, self.height / 2 - self.bar_width / 2, 15, self.bar_width])
        self.player2 = Player(screen, 2, pygame.Color('red'), [self.width - 35, self.height / 2 - self.bar_width / 2, 15, self.bar_width])
        self.ball = Ball(screen, pygame.Color('white'), [int(self.width / 2), int(self.height / 2)])
        self.text = Text(screen, config['DEFAULT']['Font type'])

        self.score = {'player1': 0, 'player2': 0}
        self.paused = False

        # temporary values that store last ball speed during pause
        self.tempx = self.ball.dx
        self.tempy = self.ball.dy

        self.comp_diff = float(config['DEFAULT']['Difficulty'])
        # expected offset of next computer move
        self.next_collision_point = self.get_next_collision_point()

    def draw_rects(self):
        """Draw game objects"""
        self.player1.draw_rect()
        self.player2.draw_rect()
        self.ball.draw_circle()
        self.text.draw_score(self.score)

    def animate(self) -> bool:
        """Step in game's animation. Move ball and detect collisions.

        Returns:
            true if animate() resulted in score change (point scored)

        """
        self.ball.move_ball()
        res = self.ball.detect_collisions([self.player1, self.player2])
        if res == 1:
            self.score['player1'] += 1
            return True
        elif res == 2:
            self.score['player2'] += 1
            return True
        elif res == 3:
            self.next_collision_point = self.get_next_collision_point()
        return False

    def animate_computer(self):
        """Step for computer animation. Adjust computer bar position to maintain collision point."""
        ball_y = self.ball.y
        cross_point = self.player1.rect.y + self.next_collision_point
        if cross_point < ball_y:
            self.player1.rect.y += abs(self.ball.dy)
        elif cross_point > ball_y:
            self.player1.rect.y -= abs(self.ball.dy)

    def pause(self):
        """Pause game by stopping the ball."""
        self.tempx = self.ball.dx
        self.tempy = self.ball.dy
        self.ball.dx = 0
        self.ball.dy = 0
        self.paused = True

    def unpause(self):
        """Unpause game, set ball to move again."""
        self.ball.dx = self.tempx
        self.ball.dy = self.tempy
        self.paused = False

    def reset(self):
        """Reset game (reset score and ball position."""
        self.score['player1'] = 0
        self.score['player2'] = 0
        self.ball.x = int(self.width / 2)
        self.ball.y = int(self.height / 2)

    def get_next_collision_point(self):
        """Determine next cross offset for ball and computer player bar center."""
        random_num = np.random.normal(0, self.comp_diff, 1)
        return self.bar_width / 2 + random_num * self.bar_width / 4
