from aoc_shortcuts import *

f = open('input')

m = mread(f)

height, width = msize(m)

i0, j0 = mfind(m, '^')[0]

def mark_reachable(m):
    i, j = i0, j0

    direction = '^'

    while True:
        ni, nj = mmove(i, j, direction)

        if not mfits(m, ni, nj):
            return

        if m[ni][nj] == '#':
            direction = TURN_RIGHT[direction]
        else:
            m[ni][nj] = 'X'
            i, j = ni, nj

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

            # Only checking the corners is enough for loop detection.
            if (i, j, direction) in visited:
                return True
            visited.add((i, j, direction))

        else:
            i, j = ni, nj

mark_reachable(m)

count = 0

for i, j in tqdm(mrange(m)):
    # Only consider obstacles which could alter the original path.
    if m[i][j] == 'X':
        m[i][j] = '#'

        if has_loop(m):
            count += 1

        m[i][j] = 'X'

print(count)
