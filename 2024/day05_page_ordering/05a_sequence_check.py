from aoc_shortcuts import *

open_input('input')

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

for s in lines():
    rules.add(tuple(ints(s)))

for s in lines():
    a = ints(s)

    if check(a):
        total += a[len(a) // 2]

print(total)
