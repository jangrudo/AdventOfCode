from aoc_shortcuts import *

open_input('input')

m = mread()

i, j = mfind(m, '^')[0]

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
