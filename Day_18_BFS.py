import numpy as np
from collections import deque

with open("day_18_input.txt") as file:
    data = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in [i for i in file.read().split("\n")]]

map = np.zeros((71, 71))

for x in data[:1024]:
    map[x[1], x[0]] = 1

start_x = 0
start_y = 0
rows, cols = map.shape[0], map.shape[1]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for d in data[1024:]:
    queue = deque([(start_x, start_y)])
    result = []
    routes = []
    seen = set()
    length = None

    found = False

    map[d[1], d[0]] = 1
    while queue:
        x, y = queue.popleft()
        if (x, y) == (70,70):
            found = True
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if map[nx, ny] == 1:
                    continue
                elif map[nx, ny] == 0 and (nx, ny) not in seen:
                    queue.append((nx, ny))
                    seen.add((nx, ny))

    if not found:
        print (d)
        break

