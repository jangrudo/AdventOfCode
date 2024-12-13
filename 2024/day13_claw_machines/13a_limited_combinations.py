from aoc_library import *

total = 0

def solve(xa, ya, xb, yb, xprize, yprize):
    for i in range(100):
        for j in range(100):
            if xa * i + xb * j == xprize and ya * i + yb * j == yprize:
                return 3 * i + j
    return 0

with open('input') as f:
    while lines := list(fsection(f)):

        xa, ya = ints(lines[0])
        xb, yb = ints(lines[1])
        xprize, yprize = ints(lines[2])

        total += solve(xa, ya, xb, yb, xprize, yprize)

print(total)
