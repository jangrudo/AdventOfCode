from aoc_shortcuts import *

f = open('input')

total = 0

def iterate(result, size):
    if result > target:
        return False
    if size == len(a):
        return result == target

    return (
        iterate(result + a[size], size + 1) or
        iterate(result * a[size], size + 1)
    )

for s in lines(f):
    a = ints(s)
    target = popfront(a)

    if iterate(a[0], 1):
        total += target

print(total)
