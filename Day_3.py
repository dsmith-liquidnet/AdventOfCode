import pandas as pd
import re
import numpy as np
import itertools

###Part 1###

with open ("advent_part_one_20241203.txt") as file:
    data = file.read()

def match_and_sum(text):
    matches = re.findall(r"mul\(\d+,\d+\)", text)

    sums=0
    for x in matches:
        numbers=[int(y) for y in re.findall(r"\d+", x)]
        sums += numbers[0]*numbers[1]

    return sums

p1 = match_and_sum(data)

###Part 2###

first_sum = match_and_sum(data.split("don't()")[0])

second_sum = 0
count = 0
for x in data.split("don't()")[1:]:
    try:
        do_text = "".join(x.split("do()")[1:])
        second_sum += match_and_sum(do_text)
        count += 1
    except:
        count += 1

p2 = first_sum + second_sum

