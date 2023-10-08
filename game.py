import random
def newGame():
    for row in main.grid:
        for cell in row:
            y = 0
    addTile()

def addTile():
    randomIndex = random.randint(0, numberOfEmptyTiles())
    for row in main.grid:
        for cell in row:
            if cell == 0:
                if randomIndex == 0:
                    if random.randint(0,9) == 0:
                        cell == 4
                    else:
                        cell == 2
                else:
                    randomIndex -= 1


def numberOfEmptyTiles():
    count = 0
    for row in main.grid:
        for cell in row:
            if y == 0:
                count += 1
    return count




