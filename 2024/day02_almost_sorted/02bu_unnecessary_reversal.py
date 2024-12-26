from aoc_shortcuts import *

count = 0

def is_safe(a):
    if not (a == sorted(a) or a == list(reversed(sorted(a)))):
        return False
    for i in range(len(a) - 1):
        if not (1 <= abs(a[i] - a[i + 1]) <= 3):
            return False
    return True

def is_safe_x(a):
    for i in range(len(a)):
        ax = a.copy()
        del ax[i]
        if is_safe(ax):
            return True
    return False

with open('input') as f:
    for line in f:
        a = ints(line)

        if is_safe_x(a):
            count += 1

print(count)
