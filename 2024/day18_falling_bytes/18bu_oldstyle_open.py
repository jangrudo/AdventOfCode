from aoc_shortcuts import *

with open('input') as f:
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

for fallen in tqdm(range(1024, len(falls))):

    m[falls[fallen][1]][falls[fallen][0]] = '#'

    if not can_move():
        break

m[falls[fallen][1]][falls[fallen][0]] = 'O'
mprint(m)

print(','.join(str(x) for x in falls[fallen]))
