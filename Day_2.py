import pandas as pd
import re
import numpy as np
import itertools

day2_list=pd.read_csv("advent_part_one_20241202.txt", delimiter="/", header=None)[0].values.tolist()
input_data=[x.split(" ") for x in day2_list]

###Part 1###
def increasing_decreasing(x):
    return np.all(x>0) or np.all(x<0)

def one_or_more(x):
    return np.all(abs(x)>=1)

def three_or_less(x):
    return np.all(abs(x)<=3)

count = 0
for x in input_data:
    test = np.diff(np.array([int(y) for y in x]))
    if all([increasing_decreasing(test), one_or_more(test), three_or_less(test)]):
        count+=1

p1 = count

###Part 2###

count = 0

for x in input_data:
    int_list = [int(z) for z in x]

    for y in range(len(int_list)):
        list_copy = int_list[:]
        list_copy.pop(y)
        new_diff_array = np.diff(np.array(list_copy))
        if all([increasing_decreasing(new_diff_array), one_or_more(new_diff_array), three_or_less(new_diff_array)]):
            count += 1
            break

p2 = count