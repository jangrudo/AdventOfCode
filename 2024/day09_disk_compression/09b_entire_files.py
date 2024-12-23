from aoc_shortcuts import *

f = open('input')

dense = [int(c) for c in f.readline().strip()]

a = []

ident = 0

free = False
for length in dense:
    if free:
        a += ['.'] * length
    else:
        a += [ident] * length
        ident += 1
    free = not free

def move(i0, size):
    j = 0
    while True:
        while j < i0 and a[j] != '.':
            j += 1

        if j == i0:
            return

        nj = j
        while nj < i0 and a[nj] == '.':
            nj += 1

        if nj - j >= size:
            for k in range(size):
                a[j + k] = a[i0 + k]
                a[i0 + k] = '.'
            return

        j = nj

last_ident = a[-1]

i = len(a) - 1

for ident in tqdm(range(last_ident, -1, -1)):
    while a[i] != ident:
        i -= 1

    ni = i
    while ni >= 0 and a[ni] == ident:
        ni -= 1

    move(ni + 1, i - ni)
    i = ni

total = 0

for i in range(len(a)):
    if a[i] != '.':
        total += i * a[i]

print(total)
