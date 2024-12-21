from aoc_shortcuts import *

open_input('input')

m = mread()

letters = string.ascii_letters + string.digits

marks = deepcopy(m)

def mark(i, j):
    if mfits(m, i, j):
        marks[i][j] = '#'

for c in letters:
    points = mfind(m, c)

    for a in range(len(points) - 1):
        for b in range(a + 1, len(points)):
            di = points[b][0] - points[a][0]
            dj = points[b][1] - points[a][1]

            mark(points[a][0] - di, points[a][1] - dj)
            mark(points[b][0] + di, points[b][1] + dj)

mprint(marks)

print(mcount(marks, '#'))
