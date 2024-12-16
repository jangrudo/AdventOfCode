from aoc_library import *

m = []

with open('input') as f:
    for line in f:
        m.append([c for c in line.strip()])

height = len(m)
width = len(m[0])

for i, j in mrange(m):
    if m[i][j] == '^':
        ci, cj = i, j
        break

TURN = {'^' : '>', '>': 'v', 'v': '<', '<': '^'}

direction = '^'

while True:
    m[ci][cj] = 'X'

    di, dj = STEP[direction]
    ni = ci + di
    nj = cj + dj

    if not (0 <= ni < height and 0 <= nj < width):
        break

    if m[ni][nj] == '#':
        direction = TURN[direction]
    else:
        ci = ni
        cj = nj

count = 0

for i, j in mrange(m):
    if m[i][j] == 'X':
        count += 1

print(count)
