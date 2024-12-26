from aoc_shortcuts import *

f = open('input')

m = mread(f)

start = mfind(m, 'S')
finish = mfind(m, 'E')

q = {start}

# Cell's (zero-based) index on the (single) path through the labyrinth.
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

LEAP = 20

count = 0

height, width = msize(m)  # mfits() slows things down considerably.

for i, j in tqdm(mrange(step)):
    if step[i][j] is not None:

        for ni in range(max(i - LEAP, 0), min(i + LEAP + 1, height)):

            di = abs(ni - i)  # Pre-computing the abs value is a considerable speedup.

            # Only loop over cells which exactly fit the shortcut constraints.
            remainder = LEAP - di
            for nj in range(max(j - remainder, 0), min(j + remainder + 1, width)):

                if step[ni][nj] is not None:
                    shortcut = di + abs(nj - j)

                    if step[ni][nj] - step[i][j] - shortcut >= 100:
                        count += 1

print(count)
