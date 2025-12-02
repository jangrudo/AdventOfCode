from aoc_shortcuts import *

f = open('input')

def calc(s1, s2):
    print(s1, s2)

    assert len(s1) == len(s2)

    found = set()

    for count in range(2, len(s1) + 1):
        if len(s1) % count != 0:
            continue

        n1 = int(s1[: len(s1) // count])
        n2 = int(s2[: len(s2) // count])

        a = []

        for n in range(n1, n2 + 1):
            s = str(n) * count
            if s1 <= s <= s2:
                a.append(s)
                found.add(int(s))

        if len(a) > 0:
            print(' ', count, a[0], a[-1])

    return sum(found)

total = 0

for pair in oneline(f).split(','):
    s1, s2 = pair.split('-')

    while len(s1) < len(s2):
        total += calc(s1, '9' * len(s1))
        s1 = '1' + '0' * len(s1)

    total += calc(s1, s2)

print(total)
