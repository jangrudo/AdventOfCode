from aoc_shortcuts import *

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

def is_compact():

    # Center of mass. The actual hidden picture turns out to be quite dense.
    mx = sum(x[i] for i in range(size)) / size
    my = sum(y[i] for i in range(size)) / size

    far_count = 0  # The number of points away from the center of mass.

    # Cutoff values slightly tuned post factum for reliable identification, with random
    # picture locations and random background noise.
    #
    # Actual picture is 31 tiles wide, 33 tiles tall, and contains 353 out of 500 robots.

    for i in range(size):
        if abs(x[i] - mx) > 25 or abs(y[i] - my) > 25:
            far_count += 1

    return far_count < 250

for iteration in tqdm(urange()):
    for i in range(size):
        x[i] = (x[i] + vx[i]) % width
        y[i] = (y[i] + vy[i]) % height

    if is_compact():
        break

for cy in range(height):
    for cx in range(width):
        count = len([i for i in range(size) if x[i] == cx and y[i] == cy])
        print(count if count else '.', end='')
    print()

print(iteration + 1)
