import pygame
import configparser

from ball import Ball
from player import Player


def main():

    pygame.init()

    config = configparser.ConfigParser()
    config.read('config.ini')

    size = width, height = int(config['DEFAULT']['Width']), int(config['DEFAULT']['Height'])

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)

    barwidth = int(config['DEFAULT']['Bar width'])

    player1 = Player(screen, 1, pygame.Color('blue'), [20, height / 2 - barwidth / 2, 15, barwidth])
    player2 = Player(screen, 2, pygame.Color('red'), [width - 35, height / 2 - barwidth / 2, 15, barwidth])

    ball = Ball(screen, pygame.Color('white'), [int(width / 2), int(height / 2)])

    off_y = 0
    mouse_down = False
    quit = False

    while not quit:

        screen.fill((0, 0, 0))

        player1.draw_rect()
        player2.draw_rect()
        ball.draw_circle()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player2.rect.collidepoint(event.pos):
                        mouse_down = True
                        off_y = event.pos[1] - player2.rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    player2.move_mouse(off_y)

        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            player1.move_down()
        if key[pygame.K_w]:
            player1.move_up()

        pygame.display.update()
        clock.tick(50)

    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()
