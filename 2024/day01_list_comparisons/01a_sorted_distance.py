from aoc_shortcuts import *

f = open('input')

left = []
right = []

for line in f:
    l, r = ints(line)
    left.append(l)
    right.append(r)

left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += max(left[i], right[i]) - min(left[i], right[i])

print(total)
