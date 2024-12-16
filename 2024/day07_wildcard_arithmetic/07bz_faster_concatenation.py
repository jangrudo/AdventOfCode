from aoc_library import *

total = 0

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

with open('input') as f:
    for line in tqdm(f.readlines()):
        a = ints(line)
        target = a[0]
        a = a[1:]

        scaler = [10 ** len(str(x)) for x in a]

        if iterate(a[0], 1):
            total += target

print(total)
