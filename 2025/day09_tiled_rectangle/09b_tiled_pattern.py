from aoc_shortcuts import *

f = open('input')

Point = xclass('x y', dx=None, dy=None, mi=None, mj=None)

p = []
for a in lints(f):
    p.append(Point(*a))

for i in range(len(p) - 1):
    for j in range(i + 1, len(p)):
        if p[i].y == p[j].y:
            assert p[i].dx is None
            p[i].dx = 1 if p[j].x > p[i].x else -1
            p[j].dx = -p[i].dx
        if p[i].x == p[j].x:
            assert p[i].dy is None
            p[i].dy = 1 if p[j].y > p[i].y else -1
            p[j].dy = -p[i].dy

xs = sorted(set(pt.x for pt in p))
ys = sorted(set(pt.y for pt in p))

pset = set((pt.x, pt.y) for pt in p)

m = mcreate((len(xs), len(ys)), '.')

pref = mcreate((len(xs), len(ys)), None)

def findpt(p, x, y):
    for pt in p:
        if pt.x == x and pt.y == y:
            return pt
    assert False

for i, j in mrange(m):
    if (xs[i], ys[j]) in pset:
        m[i][j] = '#'
        pref[i][j] = findpt(p, xs[i], ys[j])

for i, j in mrange(m):
    if (xs[i], ys[j]) in pset:
        dx = pref[i][j].dx
        ni = i
        while m[ni + dx][j] != '#':
            m[ni + dx][j] = '#'
            ni += dx

        dy = pref[i][j].dy
        nj = j
        while m[i][nj + dy] != '#':
            m[i][nj + dy] = '#'
            nj += dy

def paint(m, i0, j0):
    assert m[i0][j0] == '.'

    q = {(i0, j0)}
    while len(q) > 0:
        nq = set()
        for i, j in q:
            m[i][j] = '@'
            for ni, nj in deltas(m, i, j):
                if m[ni][nj] not in '@#':
                    nq.add((ni, nj))
        q = nq

imax, jmax = msize(m)

paint(m, 0, 0)
paint(m, 0, jmax - 1)
paint(m, imax - 1, 0)
paint(m, imax - 1, jmax - 1)

for pt in p:
    pt.mi = xs.index(pt.x)
    pt.mj = ys.index(pt.y)
    assert pt.x == xs[pt.mi]
    assert pt.y == ys[pt.mj]

def isgood(m, mis, mif, mjs, mjf):
    assert mis <= mif
    assert mjs <= mjf

    for mi in range(mis, mif + 1):
        for mj in range(mjs, mjf + 1):
            if m[mi][mj] not in '.#':
                return False
    return True

surface = None

for k1 in tqdm(range(len(p) - 1)):
    for k2 in range(k1 + 1, len(p)):
        mi1 = p[k1].mi
        mj1 = p[k1].mj
        mi2 = p[k2].mi
        mj2 = p[k2].mj

        mis = min(mi1, mi2)
        mif = max(mi1, mi2)
        mjs = min(mj1, mj2)
        mjf = max(mj1, mj2)

        if isgood(m, mis, mif, mjs, mjf):
            surface = gmax(surface, (xs[mif] - xs[mis] + 1) * (ys[mjf] - ys[mjs] + 1))

print(surface)
