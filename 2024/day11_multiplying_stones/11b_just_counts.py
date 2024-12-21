from aoc_shortcuts import *

open_input('input')

a = Counter(ints(lines()[0]))

for iteration in range(75):

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
