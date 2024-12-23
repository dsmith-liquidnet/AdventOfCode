from collections import defaultdict

input = [125, 17]
#input = [814,1183689,0,1,766231,4091,93836,46]

stone_counts = defaultdict(int)

for x in input:
    stone_counts[x] +=1



def stone_transformer(stone_counts):
    new_counts = defaultdict(int)
    for stones, counts in stone_counts.items():
        if stones==0:
            new_counts[1] += counts
        elif len(str(stones))%2==0:
            left_int = int(str(stones)[:int(len(str(stones))/2)])
            right_int = int(str(stones)[len(str(stones))//2:])
            new_counts[left_int] += counts
            new_counts[right_int] += counts
        else:
            new_counts[stones*2024] += counts

    return new_counts

for _ in range(25):
    stone_counts = stone_transformer(stone_counts)

print(sum(stone_counts.values()))

dict = defaultdict(int)

for x in input:
    dict[x] +=1

for _ in range(75):

    new_dict = defaultdict(int)
    for stones, counts in dict.items():
        if stones == 0:
            new_dict[1] += counts
        elif len(str(stones)) % 2 == 0:
            left_int = int(str(stones)[:int(len(str(stones)) / 2)])
            right_int = int(str(stones)[len(str(stones)) // 2:])
            new_dict[left_int] += counts
            new_dict[right_int] += counts
        else:
            new_dict[stones * 2024] += counts
    dict = new_dict.copy()

print(sum(dict.values()))