from aoc_shortcuts import *

f = open('input')

points = []
for a in lints(f):
    points.append(tuple(a))

surface = None

for i in tqdm(range(len(points) - 1)):
    for j in range(i + 1, len(points)):
        surface = gmax(surface,
            (abs(points[i][0] - points[j][0]) + 1) *
            (abs(points[i][1] - points[j][1]) + 1)
        )

print(surface)
