from aoc_shortcuts import *

f = open('input')

left = []
right = []

for line in f:
    l, r = ints(line)
    left.append(l)
    right.append(r)

print(sum(x * right.count(x) for x in left))
