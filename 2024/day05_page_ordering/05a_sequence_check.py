from aoc_shortcuts import *

f = open('input')

rules = set(tuple(a) for a in lints(f))

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

total = 0

for a in lints(f):
    if check(a):
        total += a[len(a) // 2]

print(total)
