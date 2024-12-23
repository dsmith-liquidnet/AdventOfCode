from functools import cache

with open("Day_19_input") as file:
    data = file.read().split("\n")

patterns = [x.strip() for x in data[0].split(",")]
designs = data[2:]
maxlen = max(map(len, patterns))


@cache
def can_obtain(design):
    if design == "":
        return True
    for i in range(min(len(design), maxlen)+1):
        if design[:i] in patterns and can_obtain(design[i:]):
            return True
    return False

print(sum(1 if can_obtain(design) else 0 for design in designs))
