from aoc_library import *

with open('input') as f:
    m = mread(f)

i0, j0 = mfind(m, '^')[0]

TURN = {'^' : '>', '>': 'v', 'v': '<', '<': '^'}
STEP = {'^' : (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def mark_reachable(m):
    i, j = i0, j0

    direction = '^'

    while True:
        m[i][j] = 'X'

        di, dj = STEP[direction]
        ni = i + di
        nj = j + dj

        if not mfits(m, ni, nj):
            return

        if m[ni][nj] == '#':
            direction = TURN[direction]
        else:
            i = ni
            j = nj

def has_loop(m):
    i, j = i0, j0

    direction = '^'

    visited = set()

    while True:

        # Aggressive optimization of the inner loop.
        if direction == '^':
            while m[i][j] != '#':
                i -= 1
                if i < 0:
                    return False
            i += 1
        elif direction == 'v':
            while m[i][j] != '#':
                i += 1
                if i >= height:
                    return False
            i -= 1
        elif direction == '<':
            while m[i][j] != '#':
                j -= 1
                if j < 0:
                    return False
            j += 1
        elif direction == '>':
            while m[i][j] != '#':
                j += 1
                if j >= width:
                    return False
            j -= 1

        direction = TURN[direction]

        # Only checking the corners is enough for loop detection.
        if (i, j, direction) in visited:
            return True
        visited.add((i, j, direction))

count = 0

mark_reachable(m)

m[i0][j0] = '^'

height, width = msize(m)
pbar = tqdm(total = height * width)

for i, j in mrange(m):
    # Only consider obstacles which could alter the original path.
    if m[i][j] == 'X':
        m[i][j] = '#'

        if has_loop(m):
            count += 1

        m[i][j] = 'X'

    pbar.update(1)
pbar.close()

print(count)

print_finish_time()
