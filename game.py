import random
import grid
from enum import Enum

dead = False

def newGame():
    for row in grid.grid:
        for cell in row:
            y = 0
    addTile()

class direction(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'

def update(input_direction):
    # merge tiles in direction specified
    if input_direction == direction.UP:
        True
    elif input_direction == direction.DOWN:
        True
    elif input_direction == direction.LEFT:
        True
    elif input_direction == direction.RIGHT:
        True


    # check if dead
    if grid.numberOfEmptyTiles() == 0:
        dead = True
    # adds tile if not dead
    else:
        addTile()

def addTile():

    empty_cells = []

    for row_num, row in enumerate(grid.grid):
        for cell_num, cell in enumerate(row):
            if cell == 0:
                empty_cells.append([row_num, cell_num])

    new_tile_value, = random.choices([1, 2], [9, 1])
    selected_tile = random.choice(empty_cells)
    grid.grid[selected_tile[0]][selected_tile[1]] = new_tile_value
