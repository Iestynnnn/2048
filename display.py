# this is some code from another file testing out displaying with pygame
import pygame

CREAM = (255, 255, 220)
BLACK = (0, 0, 0)

pygame.init()


# Run until the user asks to quit
def draw(screen):

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(CREAM)

        pygame.draw.rect(screen, BLACK, (250, 250), 75)

        # Flip the display

        pygame.display.flip()


    # Done! Time to quit.

    pygame.quit()