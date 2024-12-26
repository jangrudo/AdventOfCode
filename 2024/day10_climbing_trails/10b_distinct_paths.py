from aoc_shortcuts import *

f = open('input')

m = mread(f)

for i, j in mrange(m):
    m[i][j] = int(m[i][j])

def iterate(i, j):
    if m[i][j] == 9:
        return 1

    count = 0

    for ni, nj in deltas(m, i, j):
        if m[ni][nj] == m[i][j] + 1:
            count += iterate(ni, nj)

    return count

count = 0

for i, j in mfindall(m, 0):
    count += iterate(i, j)

print(count)
