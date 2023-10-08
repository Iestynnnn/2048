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

        pygame.draw.rect(screen, BLACK, pygame.Rect((100,0),(3,400)))
        pygame.draw.rect(screen, BLACK, pygame.Rect((200,0),(3,400)))
        pygame.draw.rect(screen, BLACK, pygame.Rect((300,0),(3,400)))
        pygame.draw.rect(screen, BLACK, pygame.Rect((0,100),(400,3)))
        pygame.draw.rect(screen, BLACK, pygame.Rect((0,200),(400,3)))
        pygame.draw.rect(screen, BLACK, pygame.Rect((0,300),(400,3)))


        # Flip the display

        pygame.display.flip()


    # Done! Time to quit.

    pygame.quit()