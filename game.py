from configparser import ConfigParser

import numpy as np
import pygame

from ball import Ball
from player import Player
from text import Text


class Game:
    def __init__(self, screen: pygame.Surface, config: ConfigParser):
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
        self.tempx = self.ball.dx
        self.tempy = self.ball.dy
        self.comp_diff = float(config['DEFAULT']['Difficulty'])
        self.next_collision_point = self.get_next_collision_point()

    def draw_rects(self):
        self.player1.draw_rect()
        self.player2.draw_rect()
        self.ball.draw_circle()
        self.text.draw_score(self.score)

    def animate(self) -> bool:
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
            print(self.next_collision_point)
        return False

    def animate_computer(self):
        ball_y = self.ball.y
        cross_point = self.player1.rect.y + self.next_collision_point
        if cross_point < ball_y:
            self.player1.rect.y += abs(self.ball.dy)
        elif cross_point > ball_y:
            self.player1.rect.y -= abs(self.ball.dy)

    def pause(self):
        self.tempx = self.ball.dx
        self.tempy = self.ball.dy
        self.ball.dx = 0
        self.ball.dy = 0
        self.paused = True

    def unpause(self):
        self.ball.dx = self.tempx
        self.ball.dy = self.tempy
        self.paused = False

    def reset(self):
        self.score['player1'] = 0
        self.score['player2'] = 0
        self.ball.x = int(self.width / 2)
        self.ball.y = int(self.height / 2)

    def get_next_collision_point(self):
        print("diff: ", self.comp_diff)
        random_num = np.random.normal(0, self.comp_diff, 1)
        print(random_num)
        return self.bar_width / 2 + random_num * self.bar_width / 4
