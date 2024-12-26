from aoc_shortcuts import *

m = []

with open('input') as f:
    for line in f:
        m.append([c for c in line.strip()])

count = 0

height = len(m)
width = len(m[0])

for i, j in mrange(m):
    if 0 < i < height - 1 and 0 < j < width - 1 and m[i][j] == 'A':

        matches1 = (m[i - 1][j - 1] == 'M' and m[i + 1][j + 1] == 'S' or
                    m[i - 1][j - 1] == 'S' and m[i + 1][j + 1] == 'M')
        matches2 = (m[i - 1][j + 1] == 'M' and m[i + 1][j - 1] == 'S' or
                    m[i - 1][j + 1] == 'S' and m[i + 1][j - 1] == 'M')

        if matches1 and matches2:
            count += 1

print(count)
