from aoc_shortcuts import *

f = open('input')

table = []

total = 0

for s in lines(f):
    items = s.split()
    if items[0] not in '+*':
        table.append(ints(s))

    else:
        for j in range(len(items)):
            op = items[j]
            result = 0 if op == '+' else 1
            for i in range(len(table)):
                if op == '+':
                    result += table[i][j]
                else:
                    result *= table[i][j]
            total += result

print(total)
