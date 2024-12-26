from aoc_shortcuts import *

f = open('input')

m = mread(f)

height, width = msize(m)

i0, j0 = mfind(m, '^')

i, j = i0, j0
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

# Moving along the straight lines consumes most of the running time.
jump = {}
for direction in STEP:
    jump[direction] = mcreate(msize(m), None)

# Having a few thin loops for updating the lookups in every possible direction is
# significantly faster than using a single generic function (it's the bottleneck).

def update_obstacle_lookup_i(m, i):

    target = (i, -1)
    for j in range(width):
        if m[i][j] != '#':
            jump['<'][i][j] = target
        else:
            target = (i, j + 1)

    target = (i, width)
    for j in range(width - 1, -1, -1):
        if m[i][j] != '#':
            jump['>'][i][j] = target
        else:
            target = (i, j - 1)

def update_obstacle_lookup_j(m, j):

    target = (-1, j)
    for i in range(height):
        if m[i][j] != '#':
            jump['^'][i][j] = target
        else:
            target = (i + 1, j)

    target = (height, j)
    for i in range(height - 1, -1, -1):
        if m[i][j] != '#':
            jump['v'][i][j] = target
        else:
            target = (i - 1, j)

def update_obstacle_lookup_i_local(m, i, jstart):

    target = (i, jstart + 1) if m[i][jstart] == '#' else jump['<'][i][jstart]

    for j in range(jstart + 1, width):
        if m[i][j] == '#':
            break
        jump['<'][i][j] = target

    target = (i, jstart - 1) if m[i][jstart] == '#' else jump['>'][i][jstart]

    for j in range(jstart - 1, -1, -1):
        if m[i][j] == '#':
            break
        jump['>'][i][j] = target

def update_obstacle_lookup_j_local(m, istart, j):

    target = (istart + 1, j) if m[istart][j] == '#' else jump['^'][istart][j]

    for i in range(istart + 1, height):
        if m[i][j] == '#':
            break
        jump['^'][i][j] = target

    target = (istart - 1, j) if m[istart][j] == '#' else jump['v'][istart][j]

    for i in range(istart - 1, -1, -1):
        if m[i][j] == '#':
            break
        jump['v'][i][j] = target

# Pre-calculate the jumps for the entire grid, in all directions.
for i in range(height):
    update_obstacle_lookup_i(m, i)
for j in range(width):
    update_obstacle_lookup_j(m, j)

def has_loop(m):
    i, j = i0, j0

    direction = '^'

    visited = set()

    while True:
        i, j = jump[direction][i][j]

        # mfits() slows things down a little bit.
        if not (0 <= i < height and 0 <= j < width):
            return False

        direction = TURN_RIGHT[direction]

        # Only checking the corners is enough for loop detection.
        if (i, j, direction) in visited:
            return True
        visited.add((i, j, direction))

count = 0

m[i0][j0] = '.'

for i, j in tqdm(mrange(m)):
    # Only consider obstacles which could alter the original path.
    if m[i][j] == 'X':
        m[i][j] = '#'

        # Update the jumps for the distorted area of the grid.
        update_obstacle_lookup_i_local(m, i, j)
        update_obstacle_lookup_j_local(m, i, j)

        if has_loop(m):
            count += 1

        m[i][j] = 'X'

        update_obstacle_lookup_i_local(m, i, j)
        update_obstacle_lookup_j_local(m, i, j)

print(count)
