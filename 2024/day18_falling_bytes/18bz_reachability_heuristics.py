from aoc_shortcuts import *

open_input('input')

falls = [tuple(ints(s)) for s in lines()]

m = mcreate((71, 71), '.')

for fall in falls[: 1024]:
    m[fall[1]][fall[0]] = '#'

def can_move(ifall, jfall):
    fall_neighbors = set((i, j) for i, j in deltas(m, ifall, jfall) if m[i][j] != '#')

    q = [(0, 0)]
    visited = {(0, 0)}

    for tail in urange():
        if tail == len(q):
            return False

        i, j = q[tail]

        for ni, nj in deltas(m, i, j):
            if m[ni][nj] != '#' and (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append((ni, nj))

                # Stop after having reached all the cells adjacent to the fallen block.
                if (ni, nj) in fall_neighbors:
                    fall_neighbors.remove((ni, nj))
                    if len(fall_neighbors) == 0:
                        return True

                if (ni, nj) == (70, 70):
                    return True

progress = tqdm(total = len(falls) - 1024)

for fallen in range(1024, len(falls)):

    ifall, jfall = reversed(falls[fallen])

    m[ifall][jfall] = '#'

    progress.update(1)

    # Ignore blocks with an easy walk-around (at most one obstacle nearby).
    if sum(1 for ni, nj in alldeltas(m, ifall, jfall) if m[ni][nj] == '#') <= 1:
        continue

    if not can_move(ifall, jfall):
        progress.update(len(falls) - fallen - 1)
        progress.close()
        break

m[falls[fallen][1]][falls[fallen][0]] = 'O'
mprint(m)

print(','.join(str(x) for x in falls[fallen]))
