from aoc_library import *

total = 0

def iterate(result, size):
    if result > target:
        return False
    if size == len(a):
        return result == target

    return (
        iterate(result + a[size], size + 1) or
        iterate(result * a[size], size + 1) or
        iterate(int(str(result) + str(a[size])), size + 1)
    )

with open('input') as f:
    for line in tqdm(f.readlines()):
        a = ints(line)
        target = a[0]
        a = a[1:]

        if iterate(a[0], 1):
            total += target

print(total)
