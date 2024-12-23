from aoc_shortcuts import *

f = open('input')

total = {}

def simulate(n):
    a = [n % 10]

    price = {}

    for iteration in range(2000):
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216

        a.append(n % 10)

        if len(a) >= 5:
            tail = a[-5 : ]
            seq = tuple(tail[i + 1] - tail[i] for i in range(4))

            if seq not in price:
                price[seq] = a[-1]

    for seq in price:
        if seq not in total:
            total[seq] = price[seq]
        else:
            total[seq] += price[seq]

for s in tqdm(lines(f)):
    simulate(int(s))

print(max(total[seq] for seq in total))
