from aoc_shortcuts import *

f = open('input')

Pair = xtuple('distance p1 p2')

points = []

for a in lints(f):
    points.append(tuple(a))

pairs = []

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distance = sum((points[i][d] - points[j][d]) ** 2 for d in range(3))
        pairs.append(Pair(distance, points[i], points[j]))

pairs.sort()

sets = {p : frozenset([p]) for p in points}

for pair in pairs:
    if sets[pair.p1] != sets[pair.p2]:
        aggregate = sets[pair.p1] | sets[pair.p2]

        if len(aggregate) == len(points):
            print(pair.p1, pair.p2)
            print(pair.p1[0] * pair.p2[0])
            exit()

        for p in aggregate:
            sets[p] = aggregate
