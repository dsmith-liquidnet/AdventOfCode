import pandas as pd
import re
import numpy as np
import itertools

with open("advent_part_one_20241204.txt") as file:
    data = [i for i in file.read().split("\n")][:-1]

pre_array = []
for y in data:
    pre_array.append([x for x in y])

data = np.array(pre_array)

data = np.pad(data, 4)


def horizontal_right(data, x, y):
    if data[x][y] + data[x][y + 1] + data[x][y + 2] + data[x][y + 3] == "XMAS":
        return 1
    else:
        return 0


def vertical_down(data, x, y):
    if data[x][y] + data[x + 1][y] + data[x + 2][y] + data[x + 3][y] == "XMAS":
        return 1
    else:
        return 0


def horizontal_left(data, x, y):
    if data[x][y] + data[x][y - 1] + data[x][y - 2] + data[x][y - 3] == "XMAS":
        return 1
    else:
        return 0


def vertical_up(data, x, y):
    if data[x][y] + data[x - 1][y] + data[x - 2][y] + data[x - 3][y] == "XMAS":
        return 1
    else:
        return 0


def south_east(data, x, y):
    if data[x][y] + data[x + 1][y + 1] + data[x + 2][y + 2] + data[x + 3][y + 3] == "XMAS":
        return 1
    else:
        return 0


def north_east(data, x, y):
    if data[x][y] + data[x - 1][y + 1] + data[x - 2][y + 2] + data[x - 3][y + 3] == "XMAS":
        return 1
    else:
        return 0


def north_west(data, x, y):
    if data[x][y] + data[x - 1][y - 1] + data[x - 2][y - 2] + data[x - 3][y - 3] == "XMAS":
        return 1
    else:
        return 0


def south_west(data, x, y):
    if data[x][y] + data[x + 1][y - 1] + data[x + 2][y - 2] + data[x + 3][y - 3] == "XMAS":
        return 1
    else:
        return 0


count = 0
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        if data[x][y] == "X":
            try:
                count += horizontal_right(data, x, y)
            except:
                pass
            try:
                count += vertical_down(data, x, y)
            except:
                pass
            try:
                count += horizontal_left(data, x, y)
            except:
                pass
            try:
                count += vertical_up(data, x, y)
            except:
                pass
            try:
                count += north_east(data, x, y)
            except:
                pass
            try:
                count += south_east(data, x, y)
            except:
                pass
            try:
                count += south_west(data, x, y)
            except:
                pass
            try:
                count += north_west(data, x, y)
            except:
                pass
p1 = count

###Part 2###

def xmas(data, x, y):
    diag_one = data[x - 1][y - 1] + data[x][y] + data[x + 1][y + 1]
    diag_two = data[x - 1][y + 1] + data[x][y] + data[x + 1][y - 1]
    if (diag_one == "MAS" or diag_one == "SAM") and (diag_two == "MAS" or diag_two == "SAM"):
        return 1
    else:
        return 0


count = 0

for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        if data[x][y] == "A":
            try:
                count += xmas(data, x, y)
            except:
                pass

p2 = count
