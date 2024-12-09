from aoc_library import *

with open('input') as f:
    m = mread(f)

count = 0

for i, j in mrange(m):
    for di, dj in ALLDELTAS:
        matches = True
        for k in range(len('XMAS')):
            ni = i + di * k
            nj = j + dj * k
            if not (mfits(m, ni, nj) and m[ni][nj] == 'XMAS'[k]):
                matches = False
                break
        if matches:
            count += 1

print(count)
