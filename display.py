# this is some code from another file testing out displaying with pygame
import pygame

pygame.init()


# Run until the user asks to quit
def draw(screen):

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 220))

        pygame.draw.rect(screen, (0, 0, 0), (250, 250), 75)

        # Flip the display

        pygame.display.flip()


    # Done! Time to quit.

    pygame.quit()