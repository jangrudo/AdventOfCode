from aoc_library import *

def solvable_count(s):
    found = [0] * (len(s) + 1)
    found[0] = 1

    for i in range(1, len(s) + 1):
        for p in patterns:
            if len(p) <= i and s[: i].endswith(p) and found[i - len(p)] > 0:
                found[i] += found[i - len(p)]

    return found[len(s)]

with open('input') as f:
    patterns = lines(f)[0].split(', ')

    count = 0

    for line in tqdm(lines(f)):
        count += solvable_count(line)

print(count)
