from aoc_shortcuts import *

f = open('input')

def simulate(n):
    for iteration in range(2000):
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216

    return n

total = 0

for s in tqdm(lines(f)):
    total += simulate(int(s))

print(total)
