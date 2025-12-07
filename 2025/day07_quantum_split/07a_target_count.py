from aoc_shortcuts import *

f = open('input')

m = mread(f)

i0, j0 = mfind(m, 'S')
j = {j0}

count = 0

for i in range(1, len(m)):
    nj = set()

    for pj in j:
        if m[i][pj] == '^':
            nj.add(pj - 1)
            nj.add(pj + 1)
            count += 1
        else:
            nj.add(pj)

    j = nj

print(count)
