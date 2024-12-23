import numpy as np
import heapq

###Part 1 - Implementing Dijkstra's algo to find the lowest cost route through the maze###
with open("day_16_test_input.txt") as file:
    data = [i for i in file.read().split("\n")]

maze = []

for x in data:
    maze.append([y for y in x])

maze = np.array(maze)

start_x, start_y = np.where(maze=="S")[0][0], np.where(maze=="S")[1][0]
end_x, end_y = np.where(maze=="E")[0][0], np.where(maze=="E")[1][0]

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
directions = ["<", ">", "^", "v"]
directions_dict = dict(zip(moves, directions))

def dijkstra_maze(maze, start, end, turn_penalty, start_direction):

    pq = [(0, start[0], start[1], start_direction)]
    costs={(start[0], start[1], start_direction): 0}

    while pq:
        cost, x, y, current_dir = heapq.heappop(pq)

        if (x, y) == end:
            return cost

        for dx, dy in moves:
            new_dir = directions_dict[(dx, dy)]
            nx, ny = x + dx, y + dy

            if maze[(nx, ny)] != "#":
                new_cost = cost + 1
                if current_dir != new_dir:
                    new_cost += turn_penalty

                if (nx, ny, new_dir) not in costs or new_cost<costs[(nx, ny, new_dir)]:
                    costs[(nx, ny, new_dir)] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, new_dir))

    return float('inf')

print(dijkstra_maze(maze, (start_x, start_y), (end_x, end_y), 1000, '>'))

###Part 2 - Finding all the routes###

def dfs(maze, start, end, turn_penalty, start_direction):

    stack = [(start_x, start_y, [(start_x, start_y, start_direction)], start_direction, 0, 0)]
    routes = []


    while stack:
        x, y, path, direction, move_count, turns = stack.pop()

        if maze[(x, y)] == "E":
            routes.append(path)
            continue

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            new_dir = directions_dict[(nx, ny)]
            if (nx, ny, new_dir) in path or maze[(x, y)] == '#':
                continue
            if maze[(nx, ny)] != '#':
                new_move_count = move_count + 1
                new_turns = turns
                if direction != new_dir:
                    new_turns += 1
                stack.append((nx, ny, path+[(nx, ny, new_dir)], new_dir, new_move_count, new_turns))




    return routes

print(dfs(maze, (start_x, start_y), (end_x, end_y), 1000, ">"))
