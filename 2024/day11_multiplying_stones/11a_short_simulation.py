from aoc_shortcuts import *

f = open('input')

a = Counter(ints(f))

for iteration in range(25):

    na = Counter()

    for x, count in a.items():
        s = str(x)

        if x == 0:
            na[1] += count

        elif len(s) % 2 == 0:
            na[int(s[: len(s) // 2])] += count
            na[int(s[len(s) // 2 :])] += count

        else:
            na[x * 2024] += count

    a = na

print(a.total())
