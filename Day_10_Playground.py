import numpy as np
from queue import Queue
from collections import deque

class Grids:
    def __init__(self, grid, start, target):
        self.grid = np.array(grid)
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.starts = list(zip(np.where(self.grid == start)[0], np.where(self.grid == start)[1]))
        self.target = target

    def is_valid_move(self, x, y, prev_value, prev_x, prev_y):
        rows, cols = self.grid.shape
        if 0 <= x < rows and 0 <= y < cols:
            return self.grid[x, y] == prev_value + 1 and (x != prev_x or y != prev_y)
        return False

    def bfs(self, start_x, start_y):
        rows, col = self.grid.shape
        queue = deque([(start_x, start_y, None, None, [(start_x, start_y)])])
        result = []
        ends = []
        count = 0
        routes = []

        while queue:
            x, y, prev_x, prev_y, path = queue.popleft()
            result.append((x, y))

            if self.grid[x, y] == self.target:
                routes.append(path)
                if (x, y) not in ends:
                    count += 1
                    ends.append((x, y))
                continue

            valid_move_found = False
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_valid_move(nx, ny, self.grid[x, y], prev_x, prev_y):
                    queue.append((nx, ny, x, y, path + [(nx, ny)]))
                    valid_move_found = True

            if not valid_move_found:
                continue

        return len(ends)

    def dfs(self, start_x, start_y):
        stack = [(start_x, start_y, None, None, [(start_x, start_y)])]
        routes = []
        ends = []

        while stack:
            x, y, prev_x, prev_y, path = stack.pop()

            valid_move_found = False
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_valid_move(nx, ny, self.grid[x,y], prev_x, prev_y):
                    stack.append((nx, ny, x, y, path+[(nx, ny)]))
                    valid_move_found = True

            if self.grid[x, y] == self.target:
                routes.append(path)
                if (x, y) not in ends:
                    ends.append((x, y))
                continue

        return len(ends)




test_input = ['89010123',
'78121874',
'87430965',
'96549874',
'45678903',
'32019012',
'01329801',
'10456732']

test = []
for x in test_input:
    test.append([int(y) for y in x])

Grid1=Grids(test, 0, 9)

check = 0
for (x, y) in Grid1.starts:
    check += Grid1.bfs(x, y)

print (check)

check = 0
for (x, y) in Grid1.starts:
     check += Grid1.dfs(x, y)

print (check)
