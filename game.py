import random
def newGame(grid):
    for row in grid:
        for cell in row:
            y = 0
    addTile()

def addTile(grid):
    randomIndex = random.randint(0, numberOfEmptyTiles())
    for row in grid:
        for cell in row:
            if cell == 0:
                if randomIndex == 0:
                    if random.randint(0,9) == 0:
                        cell == 4
                    else:
                        cell == 2
                else:
                    randomIndex -= 1


def numberOfEmptyTiles(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell == 0:
                count += 1
    return count




