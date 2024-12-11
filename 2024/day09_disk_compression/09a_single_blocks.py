from aoc_library import *

with open('input') as f:
    dense = [int(x) for x in f.readline().strip()]

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

i = 0
while True:
    while a[-1] == '.':
        a.pop()

    while i < len(a) and a[i] != '.':
        i += 1

    if i == len(a):
        break

    a[i] = a.pop()

total = 0

for i in range(len(a)):
    total += i * a[i]

print(total)
