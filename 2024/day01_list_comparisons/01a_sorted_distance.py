from aoc_library import *

left = []
right = []

with open('input') as f:
    for line in f:
        l, r = ints(line)
        left.append(l)
        right.append(r)

left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)
