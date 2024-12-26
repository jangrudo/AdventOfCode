from aoc_shortcuts import *

f = open('input')

m = mread(f)

letters = string.ascii_letters + string.digits

marks = deepcopy(m)

for c in letters:
    points = mfindall(m, c)

    for p1 in points:
        for p2 in points:
            # Each point pair is processed twice, with alternating directions.
            if p1 != p2:
                ni = p2[0] + p2[0] - p1[0]
                nj = p2[1] + p2[1] - p1[1]

                if mfits(m, ni, nj):
                    marks[ni][nj] = '#'

mprint(marks)

print(mcount(marks, '#'))
