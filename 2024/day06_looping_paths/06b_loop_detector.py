from aoc_shortcuts import *

open_input('input')

m = mread()

height, width = msize(m)

i0, j0 = mfind(m, '^')[0]

def has_loop(m):
    i, j = i0, j0

    direction = '^'

    visited = set()

    while True:
        ni, nj = mmove(i, j, direction)

        # mfits() slows things down considerably.
        if not (0 <= ni < height and 0 <= nj < width):
            return False

        if m[ni][nj] == '#':
            direction = TURN_RIGHT[direction]

            # Only checking the corners speeds up the processing a bit.
            if (i, j, direction) in visited:
                return True
            visited.add((i, j, direction))

        else:
            i, j = ni, nj

count = 0

for i, j in tqdm(mrange(m)):
    if m[i][j] == '.':
        m[i][j] = '#'

        if has_loop(m):
            count += 1

        m[i][j] = '.'

print(count)
