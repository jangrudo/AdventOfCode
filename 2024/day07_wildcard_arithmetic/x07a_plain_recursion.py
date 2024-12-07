from aoc_library import *

total = 0

def iterate(result, size):
    if result == target and size == len(a):
        return True
    if result > target or size == len(a):
        return False

    return (
        iterate(result + a[size], size + 1) or
        iterate(result * a[size], size + 1)
    )

with open('input') as f:
    for line in f:
        a = ints(line)
        target = a[0]
        a = a[1:]

        if iterate(a[0], 1):
            total += target

print(total)