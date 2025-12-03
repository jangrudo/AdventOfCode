from aoc_shortcuts import *

f = open('input')

total = 0

for s in lines(f):
    joltage = None

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            joltage = gmax(joltage, int(s[i]) * 10 + int(s[j]))

    print(joltage)
    total += joltage

print(total)
