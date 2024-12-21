from aoc_shortcuts import *

open_input('input')

m = mread()

total = 0

visited = mcreate(msize(m), False)

def get_area(i0, j0):
    if visited[i0][j0]:
        return None

    area = [(i0, j0)]
    visited[i0][j0] = True

    for tail in urange():
        if tail == len(area):
            break

        i, j = area[tail]

        for ni, nj in deltas(m, i, j):
            if m[ni][nj] == m[i][j] and not visited[ni][nj]:
                visited[ni][nj] = True
                area.append((ni, nj))

    return area

for i0, j0 in mrange(m):

    area = get_area(i0, j0)

    if area is None:
        continue

    perimeter = 0

    for i, j in area:
        for di, dj in DELTAS:
            ni, nj = i + di, j + dj
            if not mfits(m, ni, nj) or m[ni][nj] != m[i][j]:
                perimeter += 1

    total += perimeter * len(area)

print(total)
