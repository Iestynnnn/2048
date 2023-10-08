import random
import grid

def newGame():
    for row in grid.grid:
        for cell in row:
            y = 0
    addTile()

def addTile():

    empty_cells = []

    for row_num, row in enumerate(grid.grid):
        for cell_num, cell in enumerate(row):
            if cell == 0:
                empty_cells.append([row_num, cell_num])

    new_tile_value, = random.choices([2, 4], [9, 1])
    selected_tile = random.choice(empty_cells)
