from aoc_shortcuts import *

f = open('input')

points = []
for a in lints(f):
    points.append(tuple(a))

surface = None

for i in tqdm(range(len(points) - 1)):
    for j in range(i + 1, len(points)):
        xmin = min(points[i][0], points[j][0])
        xmax = max(points[i][0], points[j][0])
        ymin = min(points[i][1], points[j][1])
        ymax = max(points[i][1], points[j][1])

        surface = gmax(surface, (xmax - xmin + 1) * (ymax - ymin + 1))

print(surface)
