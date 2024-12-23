from aoc_shortcuts import *

f = open('input')

left = []
right = []

for line in f:
    l, r = ints(line)
    left.append(l)
    right.append(r)

total = 0
for x in left:
    total += x * right.count(x)

print(total)
