from aoc_shortcuts import *

f = open('input')

m = mread(f)

width = max(len(m[i]) for i in range(len(m)))
height = len(m) - 1

total = 0

pos = 0
while m[-1][pos] == ' ':
    pos += 1

op = m[-1][pos]
result = 0 if op == '+' else 1

for j in range(width):
    if all(m[i][j] == ' ' for i in range(height)):
        pos = j
        while m[-1][pos] == ' ':
            pos += 1
        op = m[-1][pos]
        total += result
        result = 0 if op == '+' else 1

    else:
        value = 0
        for i in range(height):
            if m[i][j] != ' ':
                value = value * 10 + ord(m[i][j]) - ord('0')

        if op == '+':
            result += value
        else:
            result *= value

total += result

print(total)
