from aoc_shortcuts import *

left = []
right = []

with open('input') as f:
    for line in f:
        l, r = ints(line)
        left.append(l)
        right.append(r)

total = 0
for x in left:
    total += x * right.count(x)

print(total)