# this is some code from another file testing out displaying with pygame
import pygame
import grid
import math
import typing

EMPTYTILE = (250, 250, 190)
GRIDBORDERSCOLOUR = (235, 235, 250)

pygame.init()


# Run until the user asks to quit
def draw(screen):
    screen.fill(EMPTYTILE)

    pygame.draw.rect(screen, GRIDBORDERSCOLOUR, pygame.Rect((97,0),(4,400)))
    pygame.draw.rect(screen, GRIDBORDERSCOLOUR, pygame.Rect((198,0),(4,400)))
    pygame.draw.rect(screen, GRIDBORDERSCOLOUR, pygame.Rect((299,0),(4,400)))
    pygame.draw.rect(screen, GRIDBORDERSCOLOUR, pygame.Rect((0,97),(400,4)))
    pygame.draw.rect(screen, GRIDBORDERSCOLOUR, pygame.Rect((0,198),(400,4)))
    pygame.draw.rect(screen, GRIDBORDERSCOLOUR, pygame.Rect((0,299),(400,4)))

    drawTiles(screen)
    # Flip the display

    pygame.display.flip()


def drawTiles(screen):
    tile_colours: list[tuple[int, int, int]] = [(210,210,210),(220,210,210),(240,110,110)]
    text_font = pygame.font.SysFont('Comic Sans MS', 30)
    for x in range(4):
        for y in range(4):
            if grid.grid[x][y] != 0:
                pygame.draw.rect(screen, tile_colours[grid.grid[x][y]-1], pygame.Rect((101*x, 101*y),(97,97)))
                text_surface = text_font.render(str(2**grid.grid[x][y]), False, (0, 0, 0))
                screen.blit(text_surface, (101*x + 30, 101*y + 35))

