from aoc_shortcuts import *

f = open('input')

m = mread(f)

initial_count = mcount(m, '@')

while True:
    removed = False

    for i, j in mrange(m):
        if m[i][j] == '@':
            occupied = 0
            for ni, nj in alldeltas(m, i, j):
                if m[ni][nj] == '@':
                    occupied += 1
            if occupied < 4:
                m[i][j] = '.'
                removed = True

    if not removed:
        break

print(initial_count - mcount(m, '@'))
