from aoc_shortcuts import *

f = open('input')

m = mread(f)

i0, j0 = mfind(m, 'S')
splits = [0] * len(m[0])
splits[j0] = 1

count = 0

for i in range(1, len(m)):
    nsplits = [0] * len(m[0])

    for j in range(len(splits)):
        if m[i][j] == '^':
            nsplits[j - 1] += splits[j]
            nsplits[j + 1] += splits[j]
        else:
            nsplits[j] += splits[j]
    splits = nsplits

print(sum(splits))
