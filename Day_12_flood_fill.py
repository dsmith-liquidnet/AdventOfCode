import numpy as np
from collections import deque

with open("inputs/day_12_input.txt") as file:
    data = [line for line in file.read().splitlines()]

grid  = []
for y in data:
    grid.append([x for x in y])

grid = np.array(grid)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
areas = []
rows, cols = grid.shape




def flood_fill(start_x, start_y, target):
    visited = {}
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        if grid[x,y] != target or (x,y) in visited:
            continue
        bounds = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx<0 or nx>=rows or ny<0 or ny>=cols:
                bounds += 1
            elif grid[x, y] != grid[nx, ny]:
                bounds += 1

        visited[(x,y)] = bounds

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                queue.append((nx, ny))

    return visited

for x in range(rows):
    for y in range(cols):
        if not any((x,y) in area for area in areas):
            area = flood_fill(x, y, grid[x,y])
            if area:
                areas.append(area)
total = 0
for a in areas:
    total += (sum(a.values())*len(a))

#print (min(areas[0]))
def boundary_path(nodes_dict):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    nodes = list(nodes_dict.keys())
    start = min(nodes)  # Start at the smallest node (lexicographically)
    x, y = start
    current_direction = None
    sides = 0
    boundary = []
    visited = set()

    while True:
        visited.add((x, y))
        boundary.append((x, y))

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if (nx, ny) in nodes and (nx, ny) not in visited:
                if current_direction is not None and current_direction != i:
                    sides += 1
                current_direction = i
                x, y = nx, ny
                break
        else:
            if boundary and current_direction is not None:
                sides += 1
            # No valid neighbor found
            break

    # Check if boundary is closed
    if len(boundary) > 1 and boundary[0] == boundary[-1]:
        sides += 1

    # Handle special cases for vertical or horizontal lines
    if all(z[0] == boundary[0][0] for z in boundary) or all(z[1] == boundary[0][1] for z in boundary):
        sides = 4

    return sides



for x in range(rows):
    for y in range(cols):
        if not any((x,y) in area for area in areas):
            area = flood_fill(x, y, grid[x,y])
            if area:
                areas.append(area)

region = 0
for a in areas:
    region += len(a) * boundary_path(a)

testing = 2

print(areas[testing])
print(boundary_path(areas[testing]))
