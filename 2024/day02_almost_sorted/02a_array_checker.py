from aoc_shortcuts import *

open_input('input')

count = 0

def is_safe(a):
    if not (a == sorted(a) or a == sorted(a, reverse=True)):
        return False
    for i in range(len(a) - 1):
        if not (1 <= abs(a[i] - a[i + 1]) <= 3):
            return False
    return True

for s in lines():
    a = ints(s)

    if is_safe(a):
        count += 1

print(count)
