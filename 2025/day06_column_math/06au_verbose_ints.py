from aoc_shortcuts import *

f = open('input')

table = []

total = 0

for s in lines(f):
    items = s.split()
    if items[0] not in ['+', '*']:
        table.append(list(map(int, items)))

    else:
        for i in range(len(items)):
            op = items[i]
            result = 0 if op == '+' else 1
            for j in range(len(table)):
                if op == '+':
                    result += table[j][i]
                else:
                    result *= table[j][i]
            total += result

print(total)
