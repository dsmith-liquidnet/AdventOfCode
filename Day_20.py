import numpy as np
from collections import deque, defaultdict
import pandas as pd


with open("inputs/day_20_input") as file:
    data = file.read().splitlines()

grid = []
for x in data:
    grid.append([y for y in x])

grid = np.array(grid)

rows, cols = grid.shape

for x in range(rows):
    for y in range(cols):
        if grid[x,y]=="S":
            start_x, start_y = x, y
        if grid[x,y]=="E":
            end_x, end_y = x, y

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def maze_search(grid, start_x, start_y, end_x, end_y):

    queue=deque([(start_x, start_y, 0)])
    route = []
    seen = set()
    seen.add((start_x, start_y))

    while queue:
        x, y, moves = queue.popleft()
        route.append((x, y))

        if (x, y) == (end_x, end_y):
            return route, moves

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if grid[nx, ny] != '#' and (nx, ny) not in seen:
                queue.append((nx, ny, moves+1))
                seen.add((nx, ny))

    return None



indices = np.where(grid[1:-1, 1:-1]=='#')
indices_p = list(zip(indices[0]+1, indices[1]+1))
#indices_p = [(7, 10)]
#indices_p = [(1, 8)]
cheats = {}

standard = maze_search(grid, start_x, start_y, end_x, end_y)[1]

for x in indices_p:
    grid_copy = grid.copy()
    grid_copy[x[0], x[1]] = '.'
    path = maze_search(grid_copy, start_x, start_y, end_x, end_y)
    if (x[0], x[1]) in path[0]:
        cheats[x] = path[1]
    else:
        cheats[x] = path[1]

improvements = [standard - x for x in cheats.values()]

beat=defaultdict(int)
for x in improvements:
      beat[x] = beat[x] + 1

print (beat)
print (sum([x>=100 for x in improvements]))








