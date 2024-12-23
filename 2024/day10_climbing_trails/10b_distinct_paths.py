from aoc_shortcuts import *

f = open('input')

m = mread(f)

for i, j in mrange(m):
    m[i][j] = int(m[i][j])

def iterate(path):
    i, j = path[-1]
    current = m[i][j]

    if len(path) == 10:
        return 1

    count = 0

    for ni, nj in deltas(m, i, j):
        if m[ni][nj] == current + 1:
            path.append((ni, nj))
            count += iterate(path)
            path.pop()

    return count

count = 0

for i, j in mrange(m):
    if m[i][j] == 0:
        path = [(i, j)]
        count += iterate(path)

print(count)
