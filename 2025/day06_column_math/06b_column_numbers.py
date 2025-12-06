from aoc_shortcuts import *

f = open('input')

m = mread(f)

width = max(len(row) for row in m)
height = len(m) - 1

total = 0

nj = 0
while m[-1][nj] == ' ':
    nj += 1
op = m[-1][nj]
result = 0 if op == '+' else 1

for j in range(width):
    if all(m[i][j] == ' ' for i in range(height)):
        total += result

        nj = j
        while m[-1][nj] == ' ':
            nj += 1
        op = m[-1][nj]
        result = 0 if op == '+' else 1

    else:
        value = int(''.join(m[i][j] for i in range(height)))

        if op == '+':
            result += value
        else:
            result *= value

total += result

print(total)
