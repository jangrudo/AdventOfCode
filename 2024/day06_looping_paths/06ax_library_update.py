from aoc_library import *

with open('input') as f:
    m = mread(f)

TURN = {'^' : '>', '>': 'v', 'v': '<', '<': '^'}

i, j = mfind(m, '^')[0]

direction = '^'

while True:
    m[i][j] = 'X'

    di, dj = STEP[direction]
    ni = i + di
    nj = j + dj

    if not mfits(m, ni, nj):
        break

    if m[ni][nj] == '#':
        direction = TURN[direction]
    else:
        i = ni
        j = nj

print(mcount(m, 'X'))
