from aoc_shortcuts import *

f = open('input')

def calc(s1, s2):
    print(s1, s2)

    assert len(s1) == len(s2)
    if len(s1) % 2 != 0:
        return 0

    n1 = int(s1[: len(s1) // 2])
    n2 = int(s2[: len(s2) // 2])

    count = 0

    a = []

    for n in range(n1, n2 + 1):
        s = str(n) * 2
        if s1 <= s <= s2:
            a.append(s)
            count += int(s)

    print(' ', a[0], a[-1])

    return count

total = 0

for pair in oneline(f).split(','):
    s1, s2 = pair.split('-')

    while len(s1) < len(s2):
        total += calc(s1, '9' * len(s1))
        s1 = '1' + '0' * len(s1)

    total += calc(s1, s2)

print(total)
