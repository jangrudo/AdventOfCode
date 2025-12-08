from aoc_shortcuts import *

f = open('input')

class Pair:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.distance = sum((p1[i] - p2[i]) ** 2 for i in range(3))

    def __lt__(self, other):
        return self.distance < other.distance

points = []

for a in lints(f):
    points.append(tuple(a))

pairs = []

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        pairs.append(Pair(points[i], points[j]))

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
