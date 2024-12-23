from aoc_shortcuts import *

f = open('input')

falls = [tuple(ints(line)) for line in f]

m = mcreate((71, 71), '.')

for fall in falls[: 1024]:
    m[fall[1]][fall[0]] = '#'

def can_move():
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

                if (ni, nj) == (70, 70):
                    return True

progress = tqdm(total = len(falls) - 1024)

for fallen in range(1024, len(falls)):

    m[falls[fallen][1]][falls[fallen][0]] = '#'

    if not can_move():
        progress.update(len(falls) - fallen)
        progress.close()
        break

    progress.update(1)

m[falls[fallen][1]][falls[fallen][0]] = 'O'
mprint(m)

print(','.join(str(x) for x in falls[fallen]))
