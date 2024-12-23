from aoc_shortcuts import *

f = open('input')

m = mread(f)

def shortest_path(m):
    start = mfind(m, 'S')[0]
    finish = mfind(m, 'E')[0]

    q = {start}
    visited = {start}

    for iteration in urange(1):
        nq = set()

        for i, j in q:
            for ni, nj in deltas(m, i, j):
                if m[ni][nj] != '#' and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    nq.add((ni, nj))

        q = nq

        if finish in nq:
            break

    return iteration

original_path = shortest_path(m)

count = 0

for i, j in tqdm(mrange(m)):
    if m[i][j] == '#':

        # Added post factum to speed this up at least a little bit.
        if sum(1 for ni, nj in deltas(m, i, j) if m[ni][nj] != '#') < 2:
            continue

        m[i][j] = '.'
        path = shortest_path(m)

        if original_path - path >= 100:
            count += 1

        m[i][j] = '#'

print(count)
