from aoc_shortcuts import *

f = open('input')

pos = 50
count = 0

for step in lines(f):
    if step[0] == 'L':
        pos -= int(step[1:])
    else:
        pos += int(step[1:])
    while pos < 0:
        pos += 100
    while pos >= 100:
        pos -= 100

    if pos == 0:
        count += 1

print(count)
