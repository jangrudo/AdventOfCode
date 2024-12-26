from aoc_shortcuts import *

f = open('input')

patterns = oneline(f).split(', ')

def solvable(s):
    found = [False] * (len(s) + 1)
    found[0] = True

    for i in range(1, len(s) + 1):
        for p in patterns:
            if len(p) <= i and s[: i].endswith(p) and found[i - len(p)]:
                found[i] = True
                break

    return found[len(s)]

print(sum(solvable(s) for s in tqdm(lines(f))))
