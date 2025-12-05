from aoc_shortcuts import *

f = open('input')

pairs = []
for s in lines(f):
    s0, s1 = s.split('-')
    p0, p1 = int(s0), int(s1)

    for i in range(len(pairs)):
        p = pairs[i]
        if p[0] > p[1]:
            continue

        if p[1] < p0 or p[0] > p1:
            continue
        if p[0] <= p0 and p1 <= p[1]:
            p0, p1 = (0, -1)
            break
        if p0 <= p[0] and p[1] <= p1:
            pairs[i] = (0, -1)
            continue
        if p[0] < p0 and p0 <= p[1] < p1:
            p0 = p[1] + 1
            continue
        if p[1] > p1 and p0 < p[0] <= p1:
            p1 = p[0] - 1
            continue
        assert False

    pairs.append((p0, p1))

count = 0

for p in pairs:
    count += p[1] - p[0] + 1

print(count)
