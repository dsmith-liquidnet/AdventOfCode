import pandas as pd
import re
import numpy as np
import itertools
from functools import cmp_to_key

###Test###

input_rules = ["47|53","97|13","97|61","97|47","75|29","61|13","75|53","29|13","97|29","53|29","61|53","97|53","61|29",
"47|13","75|47","97|75","47|61","75|61","47|29","75|13","53|13"]

input_rules = [[int(x.split("|")[0]), int(x.split("|")[1])] for x in input_rules]

input_update = [[75,47,61,53,29],[97,61,53,29,13],[75,29,13],[75,97,47,61,53],[61,13,29],[97,13,75,29,47]]

###Real Deal###

with open("advent_part_one_20241205.txt") as file:
    data = [i for i in file.read().split("\n")]

input_rules = [x for x in data if "|" in x]

input_rules = [[int(x.split("|")[0]), int(x.split("|")[1])] for x in input_rules]

input_update_x = [x for x in data if "," in x]

input_update = []
for x in [x.split(",") for x in input_update_x]:
    input_update.append([int(y) for y in x])


def tester(rules, update_order):
    review = []
    for x in rules:
        try:
            review.append(update_order.index(x[0]) < update_order.index(x[1]))
        except:
            review.append(True)
        try:
            review.append(update_order.index(x[1]) > update_order.index(x[0]))
        except:
            review.append(True)

    return all(review)

list_filter=[]
for x in input_update:
    list_filter.append(tester(input_rules, x))

filtered = [x[1] for x in zip(list_filter, input_update) if x[0]]

p1 = sum([x[int((len(x)-1)/2)] for x in filtered])

###Part 2###

false_filtered = [x[1] for x in zip(list_filter, input_update) if not x[0]]

pairwise_order = {}
for x in input_rules:
    pairwise_order[(x[0], x[1])] = -1
    pairwise_order[(x[1], x[0])] = 1


def compare(x, y):
    if (x, y) in pairwise_order:
        return pairwise_order[(x, y)]
    if (y, x) in pairwise_order:
        return -pairwise_order[(y, x)]
    return 0

sorted_data=[]
for x in false_filtered:
    sorted_data.append(sorted(x, key=cmp_to_key(compare)))

p2 = sum([x[int((len(x)-1)/2)] for x in sorted_data])

print (p1, p2)
