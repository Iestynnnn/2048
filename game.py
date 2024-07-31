import random
import grid
from enum import Enum

dead = False

def newGame():
    for row in grid.grid:
        for cell in row:
            y = 0
    addTile()
    addTile()

class direction(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'

def update(input_direction):
    # merge tiles in direction specified
    updated_grid = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    if input_direction == direction.UP:
        for x in range(len(updated_grid)):
            updated_grid[x] = merge_column(grid.grid[x])
    elif input_direction == direction.DOWN:
        for x in range(len(updated_grid)):
            updated_grid[x] = merge_column(grid.grid[x][::-1])[::-1]
    elif input_direction == direction.LEFT:
        for x in range(len(updated_grid[0])):
            column = []
            for y in range(len(updated_grid)):
                column.append(grid.grid[y][x])
            column = merge_column(column)
            for y in range(len(updated_grid)):
                new_value = column[y]
                updated_grid[y][x] = new_value     #<---here
    elif input_direction == direction.RIGHT:
        for x in range(len(updated_grid[0])):
            column = []
            for y in range(len(updated_grid)):
                column.append(grid.grid[y][x])
            column = merge_column(column[::-1])[::-1]
            for y in range(len(updated_grid)):
                new_value = column[y]
                updated_grid[y][x] = new_value

    if updated_grid == grid.grid:
        return
    else:
        grid.grid = updated_grid

    # check if dead
    if grid.numberOfEmptyTiles() == 0:
        dead = True
    # adds tile if not dead
    else:
        addTile()

# for each column e.g [a,b,c,d] merging towards a
def merge_column(tiles):
    value_pointer = 0
    completed_stack = []

    # while there is a variable after the current variable
    while value_pointer < len(tiles) - 1:
        # if it is a non zero variable
        if tiles[value_pointer] != 0:
            # create holder for original variable
            tile_1_value = tiles[value_pointer]
            value_pointer += 1
            # while there are more variables check for a non zero variable,
            # if there is a non zero variable compare with the original variable
            while value_pointer < len(tiles):
                if tiles[value_pointer] == 0:
                    value_pointer += 1
                else:
                    # if the original variable and the current variable match,
                    # increase the value of the variable and add to the completed stack
                    if tile_1_value == tiles[value_pointer]:
                        completed_stack.append(tile_1_value+1)
                        grid.score += 2**(tile_1_value+1)
                        tile_1_value = 0
                        value_pointer += 1
                    # otherwise add the original variable repeat the loop
                    else:
                        completed_stack.append(tile_1_value)
                        tile_1_value = 0
                    break
            if tile_1_value != 0:
                completed_stack.append(tile_1_value)
        else:
            value_pointer += 1
    if value_pointer == len(tiles) - 1:
        completed_stack.append(tiles[value_pointer])

    while len(completed_stack) < len(tiles):
        completed_stack.append(0)

    return completed_stack

def addTile():

    empty_cells = []

    for row_num, row in enumerate(grid.grid):
        for cell_num, cell in enumerate(row):
            if cell == 0:
                empty_cells.append([row_num, cell_num])

    new_tile_value, = random.choices([1, 2], [9, 1])
    selected_tile = random.choice(empty_cells)
    grid.grid[selected_tile[0]][selected_tile[1]] = new_tile_value
    print()