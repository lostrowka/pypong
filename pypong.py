import pygame
import configparser

from game import Game


def main():
    # init all imported pygame modules
    pygame.init()

    # load configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # get size from configuration
    size = int(config['DEFAULT']['Width']), int(config['DEFAULT']['Height'])

    # init pygame clock and screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)

    # create Game object (see Game.__init__ for additional info)
    game = Game(screen, config)

    # variables used in main game loop
    off_y = 0
    mouse_down = False
    quit = False
    with_comp = False

    # possible states:
    # 0 - start menu
    # 1 - player vs player
    # 2 - computer vs player
    # 3 - stop after point scored
    state = 0

    while not quit:

        # make screen blank (prepare for re-draw)
        screen.fill((0, 0, 0))

        # determine actions according to current state
        if state == 0:
            game.text.draw_start_screen()
        elif state == 1 or state == 2:
            game.draw_rects()
            if state == 2:
                game.animate_computer()
            if game.animate():
                state = 3
        elif state == 3:
            game.draw_rects()
            game.text.draw_reset_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit loop on window quit click
                quit = True

            # handle mouse movement for player2
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

            # key press handlers
            if event.type == pygame.KEYDOWN:
                # always reset regardless current state
                if event.key == pygame.K_r:
                    game.reset()
                    state = 0
                # main screen
                if state == 0:
                    # click s - start player vs player
                    if event.key == pygame.K_s:
                        state = 1
                    # click c - start computer vs player
                    if event.key == pygame.K_c:
                        state = 3
                # player vs player or computer vs player
                elif state == 1 or state == 2:
                    # click 1-9 - change speed
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        game.ball.set_speed(event.key - 48)
                    # click p - pause/unpause
                    if event.key == pygame.K_p:
                        if game.paused:
                            game.unpause()
                        else:
                            game.pause()
                    # click c - computer enable/disable
                    if event.key == pygame.K_c:
                        if state == 1:
                            with_comp = True
                            state = 2
                        else:
                            with_comp = False
                            state = 1
                # game pause after point score
                elif state == 3:
                    # change state to last game mode on any key press
                    if with_comp:
                        state = 2
                    else:
                        state = 1

        # handle key pressed if in player vs player mode
        if state == 1:
            key = pygame.key.get_pressed()
            if key[pygame.K_s]:
                game.player1.move_down()
            if key[pygame.K_w]:
                game.player1.move_up()

        # update canvas
        pygame.display.update()
        clock.tick(50)

    # close pygame
    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()
