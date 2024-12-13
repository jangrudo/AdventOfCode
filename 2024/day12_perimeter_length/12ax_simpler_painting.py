from aoc_library import *

with open('input') as f:
    m = mread(f)

total = 0

visited = deepcopy(m)
for i, j in mrange(visited):
    visited[i][j] = False

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
