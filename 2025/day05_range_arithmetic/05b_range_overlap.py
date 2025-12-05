from aoc_shortcuts import *

f = open('input')

ranges = []
for s in lines(f):
    r0, r1 = map(int, s.split('-'))

    for i in range(len(ranges)):
        r = ranges[i]

        if r[1] < r0 or r[0] > r1:
            continue
        if r[0] <= r0 and r1 <= r[1]:
            r0, r1 = (0, -1)
            break
        if r0 <= r[0] and r[1] <= r1:
            ranges[i] = (0, -1)
        elif r[0] < r0 and r0 <= r[1] < r1:
            r0 = r[1] + 1
        elif r[1] > r1 and r0 < r[0] <= r1:
            r1 = r[0] - 1
        else:
            assert False

    ranges.append((r0, r1))

print(sum(r[1] - r[0] + 1 for r in ranges))
