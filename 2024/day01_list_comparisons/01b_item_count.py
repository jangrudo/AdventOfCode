from aoc_shortcuts import *

open_input('input')

left = []
right = []

for s in lines():
    l, r = ints(s)
    left.append(l)
    right.append(r)

total = 0
for x in left:
    total += x * right.count(x)

print(total)
