from aoc_library import *

width = 101
height = 103

x = []
y = []
vx = []
vy = []

with open('input') as f:
    for line in f:
        items = ints(line)
        x.append(items[0])
        y.append(items[1])
        vx.append(items[2])
        vy.append(items[3])

size = len(x)

for iteration in range(100):
    for i in range(size):
        x[i] = (x[i] + vx[i]) % width
        y[i] = (y[i] + vy[i]) % height

def get_count(x1, x2, y1, y2):
    print(x2 - x1 + 1, y2 - y1 + 1, x1, x2, y1, y2)

    count = 0
    for i in range(size):
        if x1 <= x[i] <= x2 and y1 <= y[i] <= y2:
            count += 1
    return count

count1 = get_count(0, width // 2 - 1, 0, height // 2 - 1)
count2 = get_count(0, width // 2 - 1, height // 2 + 1, height - 1)
count3 = get_count(width // 2 + 1, width - 1, 0, height // 2 - 1)
count4 = get_count(width // 2 + 1, width - 1, height // 2 + 1, height - 1)

print(count1 * count2 * count3 * count4)
