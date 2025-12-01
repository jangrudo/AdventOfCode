from aoc_shortcuts import *

f = open('input')

pos = 50
count = 0

for step in lines(f):
    if step[0] == 'L':
        steps = int(step[1:])
        for i in range(steps):
            pos -= 1
            if pos < 0:
                pos = 99
            if pos == 0:
                count += 1
    else:
        steps = int(step[1:])
        for i in range(steps):
            pos += 1
            if pos >= 100:
                pos = 0
            if pos == 0:
                count += 1

print(count)
