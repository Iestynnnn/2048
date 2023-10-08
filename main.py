import pygame
import game
import display

pygame.init()

grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

#create screen

screen = pygame.display.set_mode([500,500])


game.newGame()

# define a variable to control the main loop
running = True

while running:
    
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
#  draw
    display.draw(screen)

#  await movement

#  update (check dead, if dead give options end and restart (add update to restart))

#quit game