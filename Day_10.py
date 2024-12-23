import numpy as np
from queue import Queue
from collections import deque



test_input = ['89010123',
'78121874',
'87430965',
'96549874',
'45678903',
'32019012',
'01329801',
'10456732']

with open("advent_part_one_20241210.txt") as file:
    data = [i for i in file.read().split("\n")][:-1]


test = []
for x in data:
    test.append([int(y) for y in x])

grid = np.array(test)

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_valid_move(grid, x, y, prev_value, prev_x, prev_y):
    rows, cols = grid.shape
    if 0 <= x < rows and 0 <= y < cols:
        return grid[x, y] == prev_value + 1 and (x != prev_x or y != prev_y)
    return False

def bfs(grid, start_x, start_y):
    rows, col = grid.shape
    queue = deque([(start_x, start_y, None, None, [(start_x, start_y)])])
    result = []
    ends = []
    count=0
    routes=[]

    while queue:
        x, y, prev_x, prev_y, path = queue.popleft()
        result.append((x,y))

        if grid[x, y] == 9:
            routes.append(path)
            if (x,y) not in ends:
                count +=1
                ends.append((x,y))
            continue

        valid_move_found = False
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if is_valid_move(grid, nx, ny, grid[x,y], prev_x, prev_y):
                queue.append((nx, ny, x, y, path+[(nx, ny)]))
                valid_move_found = True

        if not valid_move_found:
            continue

    return count

x,y = np.where(grid==0)
pairs = list(zip(x, y))

check=0

for x in pairs:
      check += bfs(grid, x[0], x[1])







