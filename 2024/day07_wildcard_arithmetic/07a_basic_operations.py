from aoc_shortcuts import *

f = open('input')

def check(target, a):

    for mask in range(2 ** (len(a) - 1)):
        result = a[0]

        bit = 1
        for i in range(1, len(a)):
            flag = (mask & bit) != 0
            if flag:
                result += a[i]
            else:
                result *= a[i]
            bit *= 2

        if result == target:
            return True

    return False

total = 0

for s in tqdm(lines(f)):
    a = ints(s)
    target = popfront(a)

    if check(target, a):
        total += target

print(total)
