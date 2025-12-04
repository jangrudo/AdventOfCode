from aoc_shortcuts import *

f = open('input')

total = 0

for s in lines(f):
    c1 = max(s[: -1])
    c2 = max(s[s.find(c1) + 1 :])
    total += int(c1) * 10 + int(c2)

print(total)
