from aoc_shortcuts import *

f = open('input')

total = Counter()

def simulate(n):
    last = n % 10
    deltas = []

    price = {}

    for iteration in range(2000):
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216

        prev = last
        last = n % 10
        deltas.append(last - prev)

        if len(deltas) >= 4:
            seq = tuple(deltas[-4 :])

            if seq not in price:
                price[seq] = last

    for seq in price:
        total[seq] += price[seq]

for n in tqdm(ints(f)):
    simulate(n)

print(max(total.values()))
