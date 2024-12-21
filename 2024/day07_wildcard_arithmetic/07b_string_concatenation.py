from aoc_shortcuts import *

open_input('input')

def check(target, a):

    for mask in range(3 ** (len(a) - 1)):
        result = a[0]

        for i in range(1, len(a)):
            flag = mask % 3
            if flag == 0:
                result += a[i]
            elif flag == 1:
                result *= a[i]
            else:
                result = int(str(result) + str(a[i]))
            mask //= 3

            # Doesn't really help much.
            if result > target:
                break

        if result == target:
            return True

    return False

total = 0

for s in tqdm(lines()):
    a = ints(s)
    target = popfront(a)

    if check(target, a):
        total += target

print(total)
