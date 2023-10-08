# this is some code from another file testing out displaying with pygame
import pygame

pygame.init()


# Run until the user asks to quit

running = True
while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill((0, 0, 0))


    # Draw a solid blue circle in the center

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()