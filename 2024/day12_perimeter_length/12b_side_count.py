from aoc_shortcuts import *

f = open('input')

m = mread(f)

total = 0

painted = mcreate(msize(m), False)

def get_area(i0, j0):
    if painted[i0][j0]:
        return None

    area = [(i0, j0)]
    painted[i0][j0] = True

    for tail in urange():
        if tail == len(area):
            break

        i, j = area[tail]

        for ni, nj in deltas(m, i, j):
            if m[ni][nj] == m[i][j] and not painted[ni][nj]:
                painted[ni][nj] = True
                area.append((ni, nj))

    return area

Edge = xtuple('i1 i2 j1 j2')

def calculate_perimeter(area):
    perimeter = set()

    for i, j in area:
        for di, dj in DELTAS:
            ni, nj = i + di, j + dj
            if not mfits(m, ni, nj) or m[ni][nj] != m[i][j]:
                perimeter.add(Edge(i, ni, j, nj))  # Inner side always comes first.

    visited = set()

    side_count = 0

    for edge in perimeter:
        if edge in visited:
            continue

        side_count += 1
        visited.add(edge)

        # Vertical edge.
        if edge.i1 == edge.i2:
            assert abs(edge.j1 - edge.j2) == 1

            for d in [-1, 1]:
                for k in urange(1):
                    nedge = Edge(edge.i1 + d * k, edge.i2 + d * k, edge.j1, edge.j2)
                    if nedge not in perimeter:
                        break
                    assert nedge not in visited
                    visited.add(nedge)

        # Horizontal edge.
        elif edge.j1 == edge.j2:
            assert abs(edge.i1 - edge.i2) == 1

            for d in [-1, 1]:
                for k in urange(1):
                    nedge = Edge(edge.i1, edge.i2, edge.j1 + d * k, edge.j2 + d * k)
                    if nedge not in perimeter:
                        break
                    assert nedge not in visited
                    visited.add(nedge)

        else:
            assert False

    return side_count

for i0, j0 in mrange(m):

    area = get_area(i0, j0)

    if area is None:
        continue

    perimeter = calculate_perimeter(area)

    total += perimeter * len(area)

print(total)
