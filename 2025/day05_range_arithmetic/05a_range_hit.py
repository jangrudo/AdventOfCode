from aoc_shortcuts import *

f = open('input')

ranges = []
for s in lines(f):
    ranges.append(tuple(map(int, s.split('-'))))

count = 0

for n in ints(f):
    if any(r[0] <= n <= r[1] for r in ranges):
        count += 1

print(count)
