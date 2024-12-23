from aoc_shortcuts import *

f = open('input')

m = mread(f)

count = 0

height, width = msize(m)

for i, j in mrange(m):
    if 0 < i < height - 1 and 0 < j < width - 1 and m[i][j] == 'A':

        matches1 = (m[i - 1][j - 1] == 'M' and m[i + 1][j + 1] == 'S' or
                    m[i - 1][j - 1] == 'S' and m[i + 1][j + 1] == 'M')
        matches2 = (m[i - 1][j + 1] == 'M' and m[i + 1][j - 1] == 'S' or
                    m[i - 1][j + 1] == 'S' and m[i + 1][j - 1] == 'M')

        if matches1 and matches2:
            count += 1

print(count)
