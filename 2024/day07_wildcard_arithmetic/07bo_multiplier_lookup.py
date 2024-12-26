from aoc_shortcuts import *

f = open('input')

def iterate(result, size):
    if result > target:
        return False
    if size == len(a):
        return result == target

    # Also don't calculate the same values thrice.
    x = a[size]
    nsize = size + 1

    return (
        iterate(result + x, nsize) or
        iterate(result * x, nsize) or
        iterate(result * scaler[size] + x, nsize)
    )

total = 0

for s in tqdm(lines(f)):
    a = ints(s)
    target = popfront(a)

    scaler = [10 ** len(str(x)) for x in a]

    if iterate(a[0], 1):
        total += target

print(total)
