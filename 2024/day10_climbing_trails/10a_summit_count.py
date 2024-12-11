from aoc_library import *

with open('input') as f:
    m = mread(f)

for i, j in mrange(m):
    m[i][j] = int(m[i][j])

# Return a set of reachable summits.
def iterate(path):
    i, j = path[-1]
    current = m[i][j]

    if len(path) == 10:
        return {(i, j)}

    tails = set()

    for ni, nj in deltas(m, i, j):
        if m[ni][nj] == current + 1:
            path.append((ni, nj))
            tails |= iterate(path)
            path.pop()

    return tails

count = 0

for i, j in mrange(m):
    if m[i][j] == 0:
        path = [(i, j)]
        count += len(iterate(path))

print(count)
