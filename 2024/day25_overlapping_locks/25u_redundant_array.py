from aoc_shortcuts import *

f = open('input')

locks = []
keys = []

while block := lines(f):
    heights = []
    for i in range(5):
        heights.append(sum(1 for s in block if s[i] == '#'))

    if all(c == '#' for c in block[0]):
        locks.append(heights)
    elif all(c == '#' for c in block[-1]):
        keys.append(heights)
    else:
        assert False

count = 0

for l in locks:
    for k in keys:

        sums = [l[i] + k[i] for i in range(5)]

        if all(sums[i] <= 7 for i in range(5)):
            count += 1

print(count)
