from aoc_shortcuts import *

f = open('input')

locks = []
keys = []

while block := lines(f):
    heights = []
    for i in range(5):
        heights.append(sum(1 for s in block if s[i] == '#'))

    if block[0] == '#####':
        locks.append(heights)
    elif block[-1] == '#####':
        keys.append(heights)
    else:
        assert False

count = 0

for l in locks:
    for k in keys:

        if all(l[i] + k[i] <= 7 for i in range(5)):
            count += 1

print(count)
