from aoc_shortcuts import *

f = open('input')

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

total = 0

for s in tqdm(lines(f)):
    a = ints(s)
    target = popfront(a)

    if iterate(a[0], 1):
        total += target

print(total)
