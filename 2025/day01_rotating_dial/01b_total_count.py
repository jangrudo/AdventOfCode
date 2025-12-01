from aoc_shortcuts import *

f = open('input')

pos = 50
count = 0

for step in lines(f):
    delta = -1 if step[0] == 'L' else 1
    distance = int(step[1:])

    for i in range(distance):
        pos += delta
        pos %= 100

        if pos == 0:
            count += 1

print(count)
