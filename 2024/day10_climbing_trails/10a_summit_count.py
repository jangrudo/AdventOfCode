from aoc_shortcuts import *

f = open('input')

m = mread(f)

for i, j in mrange(m):
    m[i][j] = int(m[i][j])

# Return a set of reachable summits.
def iterate(i, j):
    if m[i][j] == 9:
        return {(i, j)}

    tails = set()

    for ni, nj in deltas(m, i, j):
        if m[ni][nj] == m[i][j] + 1:
            tails |= iterate(ni, nj)

    return tails

count = 0

for i, j in mfindall(m, 0):
    count += len(iterate(i, j))

print(count)
