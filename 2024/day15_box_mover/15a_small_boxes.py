from aoc_shortcuts import *

f = open('input')

m = mread(f)

directions = ''.join(lines(f))

i, j = mfind(m, '@')

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

total = sum(100 * i + j for i, j in mfindall(m, 'O'))

print(total)
