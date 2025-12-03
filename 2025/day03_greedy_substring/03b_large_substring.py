from aoc_shortcuts import *

f = open('input')

total = 0

for s in lines(f):
    joltage = ''

    start = 0
    for i in range(12):
        nxt = max(s[start : len(s) - 12 + i + 1])
        start = s.find(nxt, start) + 1
        joltage += nxt

    print(joltage)
    total += int(joltage)

print(total)
