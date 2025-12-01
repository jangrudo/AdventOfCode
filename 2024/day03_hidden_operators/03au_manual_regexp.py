from aoc_shortcuts import *

DIGITS = '0123456789'

def count(s):
    total = 0

    i = 0
    while i < len(s):
        i = s.find('mul(', i)
        if i == -1:
            break

        i += 4
        if i >= len(s) or s[i] not in DIGITS:
            continue

        start1 = i
        while i < len(s) and s[i] in DIGITS and i < start1 + 3:
            i += 1
        if i >= len(s) or s[i] != ',':
            continue

        op1 = int(s[start1 : i])

        i += 1
        if i >= len(s) or s[i] not in DIGITS:
            continue

        start2 = i
        while i < len(s) and s[i] in DIGITS and i < start2 + 3:
            i += 1
        if i >= len(s) or s[i] != ')':
            continue

        op2 = int(s[start2 : i])

        i += 1

        total += op1 * op2

    return total

with open('input') as f:
    print(count(f.read()))
