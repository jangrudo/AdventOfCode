from aoc_shortcuts import *

f = open('input')

falls = [tuple(a) for a in lints(f)]

m = mcreate((71, 71), '.')

for fall in falls[: 1024]:
    m[fall[1]][fall[0]] = '#'

q = {(0, 0)}
visited = {(0, 0)}

for iteration in urange(1):

    nq = set()

    for i, j in q:
        for ni, nj in deltas(m, i, j):
            if m[ni][nj] != '#' and (ni, nj) not in visited:
                visited.add((ni, nj))
                nq.add((ni, nj))

    if (70, 70) in nq:
        break
    q = nq

mprint(m)

print(iteration)
