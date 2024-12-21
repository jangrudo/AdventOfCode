from aoc_shortcuts import *

open_input('input')

left = []
right = []

for s in lines():
    l, r = ints(s)
    left.append(l)
    right.append(r)

left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)
