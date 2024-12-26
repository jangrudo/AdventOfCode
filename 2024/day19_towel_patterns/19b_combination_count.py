from aoc_shortcuts import *

f = open('input')

patterns = oneline(f).split(', ')

def solvable_count(s):
    found = [0] * (len(s) + 1)
    found[0] = 1

    for i in range(1, len(s) + 1):
        for p in patterns:
            if len(p) <= i and s[: i].endswith(p):
                found[i] += found[i - len(p)]

    return found[len(s)]

print(sum(solvable_count(s) for s in tqdm(lines(f))))
