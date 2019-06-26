import pygame
import configparser

from game import Game

def main():

    pygame.init()

    config = configparser.ConfigParser()
    config.read('config.ini')

    size = int(config['DEFAULT']['Width']), int(config['DEFAULT']['Height'])

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)

    game = Game(screen, config)

    off_y = 0
    mouse_down = False
    quit = False

    # possible states:
    # 0 - start menu
    # 1 - in game
    # 2 - after point
    # 3 - computer
    state = 0

    with_comp = False

    while not quit:

        screen.fill((0, 0, 0))

        if state == 0:
            game.text.draw_start_screen()
        elif state == 1 or state == 3:
            game.draw_rects()
            if state == 3:
                game.animate_computer()
            if game.animate():
                state = 2
        elif state == 2:
            game.draw_rects()
            game.text.draw_reset_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game.player2.rect.collidepoint(event.pos):
                        mouse_down = True
                        off_y = event.pos[1] - game.player2.rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    game.player2.move_mouse(off_y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
                    state = 0
                if state == 0:
                    if event.key == pygame.K_s:
                        state = 1
                    if event.key == pygame.K_c:
                        state = 3
                elif state == 1 or state == 3:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        game.ball.set_speed(event.key - 48)
                    if event.key == pygame.K_p:
                        if game.paused:
                            game.unpause()
                        else:
                            game.pause()
                    if event.key == pygame.K_c:
                        if state == 1:
                            with_comp = True
                            state = 3
                        else:
                            with_comp = False
                            state = 1
                elif state == 2:
                    if with_comp:
                        state = 3
                    else:
                        state = 1

        if state == 1:
            key = pygame.key.get_pressed()
            if key[pygame.K_s]:
                game.player1.move_down()
            if key[pygame.K_w]:
                game.player1.move_up()

        pygame.display.update()
        clock.tick(50)

    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()
