import pandas as pd
import re
import numpy as np
import itertools

###Part 1###

day1_list=pd.read_csv("advent_part_one_20241201.txt",
                      delimiter="/", header=None)[0].values.tolist()
list_one = [int(x.split(" ")[0]) for x in day1_list]
list_two = [int(x.split(" ")[3]) for x in day1_list]

p1 = sum(abs(np.sort(np.array(list_two))-np.sort(np.array(list_one))))

###Part 2###

unique, counts = np.unique(np.array(list_two), return_counts=True)
dictionary_count = dict(zip(unique, counts))
lst=[]
for x in list_one:
    try:
        lst.append(x*dictionary_count[x])
    except:
        lst.append(0)
p2 = sum(lst)

