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

print(sum(abs(left[i] - right[i]) for i in range(len(left))))
