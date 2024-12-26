from aoc_shortcuts import *

f = open('input')

total = 0

def solve(xa, ya, xb, yb, xprize, yprize):
    for i in range(100):
        for j in range(100):
            if xa * i + xb * j == xprize and ya * i + yb * j == yprize:
                return 3 * i + j
    return 0

while a := ints(f):

    xa, ya, xb, yb, xprize, yprize = a

    total += solve(xa, ya, xb, yb, xprize, yprize)

print(total)
