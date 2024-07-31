# this is some code from another file testing out displaying with pygame
import pygame
import grid
import math
import typing

EMPTYTILE = (250, 250, 190)
GRIDBORDERSCOLOUR = (235, 235, 250)
tile_colours: list[tuple[int, int, int]] = [(210,210,210),(220,210,210),(240,180,180)]

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
    pygame.display.set_caption('2048 - Score: ' + str(grid.score))


def drawTiles(screen):
    text_font = pygame.font.SysFont('Comic Sans MS', 30)
    for x in range(4):
        for y in range(4):
            if grid.grid[x][y] != 0:
                pygame.draw.rect(screen, get_tile_colour(grid.grid[x][y]), pygame.Rect((101*x, 101*y),(97,97)))
                text_surface = text_font.render(str(2**grid.grid[x][y]), False, (0, 0, 0))
                screen.blit(text_surface, (101*x + 30, 101*y + 35))

def get_tile_colour(tile_value):
    if tile_value < 4:
        return tile_colours[tile_value - 1]
    if tile_value < 10:
        return (240, (180 * (tile_value - 1)/9), (180 * (tile_value - 1)/9))
    return (240, 210, 50)