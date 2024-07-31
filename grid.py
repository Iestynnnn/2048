grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

score = 0

def numberOfEmptyTiles():
    count = 0
    for row in grid:
        for cell in row:
            if cell == 0:
                count += 1
    return count