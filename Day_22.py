import numpy as np
from collections import defaultdict
import pandas as pd

with open('inputs/day_22_input.txt') as file:
    sequence = [int(x) for x in [line for line in file.read().splitlines()]]

def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num

sums = 0
for num in sequence:
    count = 1
    while count <=2000:
        num = step(num)
        count += 1
    sums += num

part_1 = sums

#print (part_1)

codes = []
for num in sequence:
    buyer_code = [num % 10]
    for _ in range(2000):
        num = step(num)
        end = num % 10
        buyer_code.append(end)
    codes.append(buyer_code)

banana_sequences = defaultdict(int)

for x in codes:
    seen = set()
    diffs = [int(y) for y in np.diff(x)]
    for c in range(len(x)-4):
        a, b, c, d, e = x[c:c+5]
        diffs = (b-a, c-b, d-c, e-d)
        if diffs in seen:
            continue
        seen.add(diffs)
        banana_sequences[diffs] += e




max_key = max(banana_sequences, key=banana_sequences.get)
print(banana_sequences[(-2,1,-1,3)])
print(max_key)
print(banana_sequences[max_key])


# df = pd.DataFrame(banana_sequences.values(), banana_sequences.keys())
#
# df.columns=["Count"]
# df.sort_values(by="Count", inplace=True)
# print(df.index)


# banana_sequences = defaultdict(int)
# x=codes[0]
# banana_sequences_local = defaultdict(int)
# diffs = [int(y) for y in np.diff(codes[0])]
# for c in range(0, len(diffs)-4):
#     diffs_key = tuple(diffs[c:c+4])
#     banana_sequences[diffs_key] += x[c+5]
#
#
# print(banana_sequences[(-2,1,-1,3)])
# df = pd.DataFrame(banana_sequences.values(), banana_sequences.keys())
#
# df.columns=["Count"]
# df.sort_values(by="Count", inplace=True)
# print(df)

