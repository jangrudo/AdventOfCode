from aoc_shortcuts import *

f = open('input')

def count(s):
    total = 0
    enabled = True

    i = 0
    while i < len(s):
        i1 = s.find("do()", i)
        i2 = s.find("don't()", i)
        i3 = s.find("mul(", i)

        if i1 == -1:
            i1 = len(s)
        if i2 == -1:
            i2 = len(s)
        if i3 == -1:
            i3 = len(s)

        imin = min(i1, i2, i3)

        if imin == len(s):
            break

        if i1 == imin:
            enabled = True
            i = i1 + 4
            continue
        elif i2 == imin:
            enabled = False
            i = i2 + 7
            continue

        i = i3 + 4

        if i >= len(s) or s[i] not in string.digits:
            continue

        start1 = i
        while i < len(s) and s[i] in string.digits and i < start1 + 3:
            i += 1
        if i >= len(s) or s[i] != ',':
            continue

        op1 = int(s[start1 : i])

        i += 1
        if i >= len(s) or s[i] not in string.digits:
            continue

        start2 = i
        while i < len(s) and s[i] in string.digits and i < start2 + 3:
            i += 1
        if i >= len(s) or s[i] != ')':
            continue

        op2 = int(s[start2 : i])

        i += 1

        if enabled:
            total += op1 * op2

    return total

print(count(f.read()))
