from aoc_library import *

m = []

with open('input') as f:
    for line in f:
        m.append([c for c in line.strip()])

height = len(m)
width = len(m[0])

for i, j in mrange(m):
    if m[i][j] == '^':
        i0, j0 = i, j
        break

def has_loop(m):
    ci, cj = i0, j0

    direction = '^'

    visited = set()

    while True:
        di, dj = STEP[direction]
        ni = ci + di
        nj = cj + dj

        if not (0 <= ni < height and 0 <= nj < width):
            return False

        if m[ni][nj] == '#':
            direction = TURN_RIGHT[direction]

            # Only checking the corners speeds up the processing a bit.
            if (ci, cj, direction) in visited:
                return True
            visited.add((ci, cj, direction))

        else:
            ci = ni
            cj = nj

count = 0

for i, j in tqdm(mrange(m)):
    if m[i][j] == '.':
        m[i][j] = '#'

        if has_loop(m):
            count += 1

        m[i][j] = '.'

print(count)
