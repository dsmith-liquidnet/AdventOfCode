import numpy as np

with open("day_15_input_map.txt") as file:
    data = [i for i in file.read().split("\n")]

map=[]
for row in data:
    map.append([x for x in row])

map = np.array(map)

with open("day_15_input_sequence.txt") as file:
    sequence = [i for i in file.read()]

def movement(move):
    if move=='>': return (0, 1)
    if move=='<': return (0, -1)
    if move=='^': return (-1, 0)
    if move=='v': return (1, 0)

count=0
start=None

for x in range(map.shape[0]):
    for y in range(map.shape[1]):
        if map[x, y]=='@':
            start = (x, y)

x, y = start[0], start[1]
while count<len(sequence):
    dx, dy = movement(sequence[count])
    nx, ny = x + dx, y + dy
    if map[nx, ny] == ".":
        x, y = nx, ny
        count += 1
    elif map[nx, ny] == '#':
        count += 1
    elif map[nx, ny] == "O":
        if sequence[count]=='<':
            subset = map[x, 0:ny]
            for x in range(-len(subset))




