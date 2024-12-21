from aoc_shortcuts import *

open_input('input')

def solvable_count(s):
    found = [0] * (len(s) + 1)
    found[0] = 1

    for i in range(1, len(s) + 1):
        for p in patterns:
            if len(p) <= i and s[: i].endswith(p) and found[i - len(p)] > 0:
                found[i] += found[i - len(p)]

    return found[len(s)]

patterns = lines()[0].split(', ')

count = 0

for line in tqdm(lines()):
    count += solvable_count(line)

print(count)
