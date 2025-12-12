from aoc_shortcuts import *

f = open('input')

Point = xclass('x y', dx=None, dy=None, i=None, j=None)

points = []
for a in lints(f):
    points.append(Point(*a))

# Calculate directions towards neighboring points.
for p1 in points:
    for p2 in points:
        if p1 != p2:
            if p1.x == p2.x:
                assert p1.dy is None
                p1.dy = 1 if p2.y > p1.y else -1
            elif p1.y == p2.y:
                assert p1.dx is None
                p1.dx = 1 if p2.x > p1.x else -1

# Compress points into a smaller grid.
xs = sorted(set(p.x for p in points))
ys = sorted(set(p.y for p in points))

m = mcreate((len(xs), len(ys)), '.')

# Map point coordinates to grid indices.
for p in points:
    p.i = xs.index(p.x)
    p.j = ys.index(p.y)

for p in points:
    m[p.i][p.j] = '#'

# Draw lines between neighboring points.
for p in points:
    for ni in urange(p.i + p.dx, p.dx):
        if m[ni][p.j] == '#':
            break
        m[ni][p.j] = '#'
    for nj in urange(p.j + p.dy, p.dy):
        if m[p.i][nj] == '#':
            break
        m[p.i][nj] = '#'

# Paint outside space with '@'.
def paint(m, i0, j0):
    assert m[i0][j0] == '.'

    q = {(i0, j0)}
    while len(q) > 0:
        nq = set()
        for i, j in q:
            m[i][j] = '@'
            for ni, nj in deltas(m, i, j):
                if m[ni][nj] == '.':
                    nq.add((ni, nj))
        q = nq

# It looks like image corners always lie outside the boundary.
height, width = msize(m)

paint(m, 0, 0)
paint(m, 0, width - 1)
paint(m, height - 1, 0)
paint(m, height - 1, width - 1)

# Check if a rectangle lies entirely within the boundary.
def fits(m, p1, p2):
    imin, imax = sorted((p1.i, p2.i))
    jmin, jmax = sorted((p1.j, p2.j))

    for i in range(imin, imax + 1):
        for j in range(jmin, jmax + 1):
            if m[i][j] == '@':
                return False
    return True

surface = None

for p1 in tqdm(points):
    for p2 in points:
        if p1 < p2:
            if fits(m, p1, p2):
                surface = gmax(surface, (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1))

print(surface)
