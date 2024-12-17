from aoc_library import *

with open('input') as f:
    m = mread(fblock(f))

    directions = ''.join(fblock(f))

i, j = mfind(m, '@')[0]

for direction in directions:
    di, dj = STEP[direction]

    ni = i + di  # Next position of the robot.
    nj = j + dj

    if m[ni][nj] == '#':
        continue

    if m[ni][nj] == 'O':
        nni = ni  # Nearest free block behind the boxes.
        nnj = nj
        while m[nni][nnj] == 'O':
            nni += di
            nnj += dj

        if m[nni][nnj] == '#':
            continue  # Cannot move the boxes.

        m[nni][nnj] = 'O'
        m[ni][nj] = '.'

    i = ni
    j = nj

mprint(m)

total = sum(100 * i + j for i, j in mfind(m, 'O'))

print(total)
