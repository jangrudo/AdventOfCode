from aoc_shortcuts import *

with open('input') as f:
    m = mread(f)

letters = string.ascii_letters + string.digits

marks = deepcopy(m)

for c in letters:
    points = mfind(m, c)

    for a in range(len(points) - 1):
        for b in range(a + 1, len(points)):
            di = points[b][0] - points[a][0]
            dj = points[b][1] - points[a][1]

            k = 0
            while True:
                ni1 = points[a][0] - di * k
                nj1 = points[a][1] - dj * k

                ni2 = points[b][0] + di * k
                nj2 = points[b][1] + dj * k

                fits = False
                if mfits(m, ni1, nj1):
                    fits = True
                    marks[ni1][nj1] = '#'
                if mfits(m, ni2, nj2):
                    fits = True
                    marks[ni2][nj2] = '#'

                if not fits:
                    break
                k += 1

mprint(marks)

print(mcount(marks, '#'))
