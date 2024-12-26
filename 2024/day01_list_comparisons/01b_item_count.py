from aoc_shortcuts import *

f = open('input')

left, right = zip(*lints(f))

print(sum(x * right.count(x) for x in left))
