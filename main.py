import pygame
import game
import display


pygame.init()

#create screen

screen = pygame.display.set_mode([400,400])
pygame.display.set_caption('2048')

game.newGame()

# define a variable to control the main loop
running = True

while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # quit the game if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        # check for player input, if present and a direction updates in that direction
        elif event.type == pygame.KEYDOWN:
            # up arrow or w key pressed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                game.update(game.direction.UP)
                break
            # down arrow or s key pressed
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                game.update(game.direction.DOWN)
                break
            # left arrow or a key pressed
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                game.update(game.direction.LEFT)
                break
            # right arrow or d key pressed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                game.update(game.direction.RIGHT)
                break
            # escape key pressed
            elif event.key == pygame.K_ESCAPE:
                # TODO: change to an option screen to ensure player wishes to quit
                running = False

#  draw
    display.draw(screen)

#  check dead, if dead give options quit and restart (add update to restart)
