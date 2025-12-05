from aoc_shortcuts import *

f = open('input')

pairs = []
for s in lines(f):
    p1, p2 = s.split('-')
    pairs.append((int(p1), int(p2)))

count = 0

for s in lines(f):
    n = int(s)
    if any(p[0] <= n <= p[1] for p in pairs):
        count += 1

print(count)
