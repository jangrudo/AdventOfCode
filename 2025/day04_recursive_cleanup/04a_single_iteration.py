from aoc_shortcuts import *

f = open('input')

m = mread(f)

count = 0

for i, j in mrange(m):
    if m[i][j] == '@':
        occupied = 0
        for ni, nj in alldeltas(m, i, j):
            if m[ni][nj] == '@':
                occupied += 1
        if occupied < 4:
            count += 1

print(count)