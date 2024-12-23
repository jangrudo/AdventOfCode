from aoc_shortcuts import *

f = open('input')

count = 0

def is_safe(a):
    if not (a == sorted(a) or a == sorted(a, reverse=True)):
        return False
    for i in range(len(a) - 1):
        if not (1 <= abs(a[i] - a[i + 1]) <= 3):
            return False
    return True

for line in f:
    a = ints(line)

    if is_safe(a):
        count += 1

print(count)
