from aoc_shortcuts import *

open_input('input')

m = mread()

start = mfind(m, 'S')[0]
finish = mfind(m, 'E')[0]

q = {start}

step = mcreate(msize(m), None)
step[start[0]][start[1]] = 0

for iteration in urange(1):
    nq = set()

    for i, j in q:
        for ni, nj in deltas(m, i, j):
            if m[ni][nj] != '#' and step[ni][nj] is None:
                step[ni][nj] = iteration
                nq.add((ni, nj))

    q = nq

    if finish in nq:
        break

LEAP = 2

count = 0

for i, j in mrange(step):
    if step[i][j] is not None:
        for ni in range(i - LEAP, i + LEAP + 1):
            for nj in range(j - LEAP, j + LEAP + 1):
                if mfits(step, ni, nj) and step[ni][nj] is not None:
                    shortcut = abs(ni - i) + abs(nj - j)

                    if shortcut <= LEAP and step[ni][nj] - step[i][j] - shortcut >= 100:
                        count += 1

print(count)
