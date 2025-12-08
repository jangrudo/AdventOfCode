from aoc_shortcuts import *

f = open('input')

points = []

for a in lints(f):
    points.append(tuple(a))

pairs = []

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distance = sum((points[i][d] - points[j][d]) ** 2 for d in range(3))
        pairs.append((distance, points[i], points[j]))

pairs.sort()

sets = {p : frozenset([p]) for p in points}

for i in range(1000):
    pair = pairs[i]
    p1 = pair[1]
    p2 = pair[2]

    if sets[p1] != sets[p2]:
        aggregate = sets[p1] | sets[p2]
        for p in aggregate:
            sets[p] = aggregate

final_sets = set(sets.values())

sizes = sorted([len(s) for s in final_sets], reverse=True)
print(sizes)
print(sizes[0] * sizes[1] * sizes[2])
