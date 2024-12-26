from aoc_shortcuts import *

f = open('input')

left, right = map(sorted, zip(*lints(f)))

print(sum(abs(left[i] - right[i]) for i in range(len(left))))
