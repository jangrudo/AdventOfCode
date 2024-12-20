from aoc_library import *

with open('input') as f:
    m = mread(f)

    directions = ''.join(lines(f))

for i in range(len(m)):
    row = ''.join(m[i])
    row = row.replace('.', '..').replace('#', '##').replace('O', '[]').replace('@', '@.')

    m[i] = list(c for c in row)

i, j = mfind(m, '@')[0]

# Move a box in the given direction. Return False if it's not possible.
def move_box(i, j, di, dj):

    # Move left.
    if di == 0 and dj == -1:
        nj = j - 1  # Nearest free block to the left, behind the boxes.
        while m[i][nj] == ']':
            nj -= 2

        if m[i][nj] == '#':
            return False

        for jj in range(nj, j + 1):
            m[i][jj] = m[i][jj + 1]
        m[i][j + 1] = '.'
        return True

    # Move right.
    elif di == 0 and dj == 1:
        nj = j + 2  # Nearest free block to the right, behind the boxes.
        while m[i][nj] == '[':
            nj += 2

        if m[i][nj] == '#':
            return False

        for jj in range(nj, j, -1):
            m[i][jj] = m[i][jj - 1]
        m[i][j] = '.'
        return True

    # Move up or down.
    movable = [{j}]  # List of movable boxes within each row.

    for k in urange(1):  # Index of the next row being processed.
        nmovable = set()

        ni = i + k * di  # Next row's coordinate within the map.

        for bj in movable[-1]:
            if m[ni][bj] == '#' or m[ni][bj + 1] == '#':
                return False  # If one box is blocked, none can be moved.

            # Add up to two boxes for each one from the previous row.
            if m[ni][bj] == '[':
                nmovable.add(bj)
            if m[ni][bj - 1] == '[':
                nmovable.add(bj - 1)
            if m[ni][bj + 1] == '[':
                nmovable.add(bj + 1)

        if len(nmovable) == 0:
            break
        movable.append(nmovable)

    # Move all the boxes, starting from those which are farther away.
    for k in reversed(range(len(movable))):
        bi = i + k * di

        for bj in movable[k]:
            assert m[bi + di][bj] in '.@'
            assert m[bi + di][bj + 1] in '.@'

            m[bi + di][bj] = '['
            m[bi + di][bj + 1] = ']'
            m[bi][bj] = '.'
            m[bi][bj + 1] = '.'

    return True

for direction in directions:
    di, dj = STEP[direction]

    ni = i + di  # Next position of the robot.
    nj = j + dj

    if m[ni][nj] == '#':
        continue

    if m[ni][nj] in '[]':

        bj = nj if m[ni][nj] == '[' else nj - 1  # Left side of the box to be moved.

        if not move_box(ni, bj, di, dj):
            continue

    m[i][j] = '.'  # Update current location (to simplify debugging).
    m[ni][nj] = '@'

    i = ni
    j = nj

mprint(m)

total = sum(100 * i + j for i, j in mfind(m, '['))

print(total)
