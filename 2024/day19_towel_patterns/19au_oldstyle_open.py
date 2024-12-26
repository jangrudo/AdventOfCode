from aoc_shortcuts import *

def solvable(s):
    found = [False] * (len(s) + 1)
    found[0] = True

    for i in range(1, len(s) + 1):
        for p in patterns:
            if len(p) <= i and s[: i].endswith(p) and found[i - len(p)]:
                found[i] = True
                break

    return found[len(s)]

with open('input') as f:
    patterns = lines(f)[0].split(', ')

    count = 0

    for s in tqdm(lines(f)):
        if solvable(s):
            count += 1

print(count)
