from aoc_library import *

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

with open('input') as f:
    for line in tqdm(f.readlines()):
        a = ints(line)
        target = a[0]
        a = a[1:]

        if check(target, a):
            total += target

print(total)
