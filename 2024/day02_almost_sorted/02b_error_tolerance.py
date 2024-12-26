from aoc_shortcuts import *

f = open('input')

def is_safe(a):
    if not (a == sorted(a) or a == sorted(a, reverse=True)):
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

print(sum(is_safe_x(a) for a in lints(f)))
