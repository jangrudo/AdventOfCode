from aoc_shortcuts import *

f = open('input')

rules = set(tuple(ints(s)) for s in lines(f))

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

for s in lines(f):
    a = ints(s)

    if not check(a):
        a.sort(key=cmp_to_key(compare))
        total += a[len(a) // 2]

print(total)
