from aoc_shortcuts import *

f = open('input')

m = mread(f)

i, j = mfind(m, '^')

direction = '^'

while True:
    m[i][j] = 'X'

    ni, nj = mmove(i, j, direction)

    if not mfits(m, ni, nj):
        break

    if m[ni][nj] == '#':
        direction = TURN_RIGHT[direction]
    else:
        i, j = ni, nj

print(mcount(m, 'X'))
