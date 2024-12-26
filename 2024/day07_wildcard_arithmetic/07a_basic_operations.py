from aoc_shortcuts import *

f = open('input')

def iterate(result, size):
    if result > target:
        return False
    if size == len(a):
        return result == target

    return (
        iterate(result + a[size], size + 1) or
        iterate(result * a[size], size + 1)
    )

total = 0

for a in lints(f):
    target = a.pop(0)

    if iterate(a[0], 1):
        total += target

print(total)
