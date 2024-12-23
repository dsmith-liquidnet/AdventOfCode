import numpy as np
###Part 1###
test_input=["....#.....",
".........#",
"..........",
"..#.......",
".......#..",
"..........",
".#..^.....",
"........#.",
"#.........",
"......#..."]


import numpy as np
with open("advent_part_one_20241206.txt") as file:
    data = [i for i in file.read().split("\n")][:-1]

matrix=[]
for x in data:
    matrix.append([y for y in x])
matrix=np.array(matrix)

turn_rules = {"^":">", ">":"v", "v":"<", "<":"^"}

direction_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def tracer(matrix, symbol="^"):

    start_pos = np.where(matrix == symbol)
    x, y = start_pos[0][0], start_pos[1][0]
    limit_x, limit_y = matrix.shape
    locs = []

    while 0 <= x < limit_x and 0 <= y < limit_y:
        dx, dy = direction_map[symbol]
        new_x, new_y = x+dx, y+dy
        if (0 <= new_x < limit_x) and 0 <= new_y < limit_y and (matrix[new_x, new_y]=="#"):
            symbol = turn_rules[symbol]
        else:
            x, y = new_x, new_y
            locs.append((x, y))

    for x in locs[:-1]:
        matrix[x]="X"

    return len(set(locs[:-1]))


###Part 2###

def tracer_two(matrix, symbol="^"):

    start_pos = np.where(matrix == symbol)
    x, y = start_pos[0][0], start_pos[1][0]
    limit_x, limit_y = matrix.shape
    turns=[]
    while 0 <= x < limit_x and 0 <= y < limit_y:
        dx, dy = direction_map[symbol]
        new_x, new_y = x+dx, y+dy
        if (0 <= new_x < limit_x) and 0 <= new_y < limit_y and (matrix[new_x, new_y]=="#"):
            if [x, y, symbol] in turns:
                return 1
            else:
                turns.append([x, y, symbol])
                symbol = turn_rules[symbol]
        else:
            x, y = new_x, new_y
    return 0

loops=0
combos=[]
for x in range(matrix.shape[0]):
    for y in range(matrix.shape[1]):
        combos.append((x, y))

start_pos = np.where(matrix == "^")
x, y = start_pos[0][0], start_pos[1][0]
combos.remove((x,y))
for x in combos:
    new_matrix = matrix.copy()
    new_matrix[x] = "#"
    loops += tracer_two(new_matrix)

print (loops)
