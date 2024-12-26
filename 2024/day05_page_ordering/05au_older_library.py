from aoc_shortcuts import *

rules = set()

total = 0

def compare(x, y):
    if (x, y) in rules:
        return -1
    if (y, x) in rules:
        return 1
    assert False

def check(a):
    for i in range(len(a) - 1):
        if not (compare(a[i], a[i + 1]) < 0):
            return False
    return True

with open('input') as f:
    for line in f:
        rule = tuple(ints(line))

        if len(rule) == 0:
            break
        assert len(rule) == 2

        rules.add(rule)

    for line in f:
        a = ints(line)

        if check(a):
            total += a[len(a) // 2]

print(total)
