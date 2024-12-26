from aoc_shortcuts import *

m = []

with open('input') as f:
    for line in f:
        m.append([c for c in line.strip()])

count = 0

height = len(m)
width = len(m[0])

for i, j in mrange(m):
    for di, dj in ALLDELTAS:
        matches = True
        for k in range(len('XMAS')):
            ni = i + di * k
            nj = j + dj * k
            if not (0 <= ni < height and 0 <= nj < width and m[ni][nj] == 'XMAS'[k]):
                matches = False
                break
        if matches:
            count += 1

print(count)
