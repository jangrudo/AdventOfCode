from aoc_shortcuts import *

open_input('input')

dense = [int(c) for c in lines()[0]]

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
