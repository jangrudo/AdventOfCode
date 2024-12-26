from aoc_shortcuts import *

f = open('input')

width = 101
height = 103

Robot = xclass('x y vx vy')

robots = [Robot(*a) for a in lints(f)]

size = len(robots)

def is_compact():

    # Center of mass. The actual hidden picture turns out to be quite dense.
    mx = sum(r.x for r in robots) / size
    my = sum(r.y for r in robots) / size

    # The number of points away from the center of mass.
    #
    # Cutoff values slightly tuned post factum for reliable identification, with random
    # picture locations and random background noise.
    #
    # Actual picture is 31 tiles wide, 33 tiles tall, and contains 353 out of 500 robots.
    far_count = sum(1 for r in robots if abs(r.x - mx) > 25 or abs(r.y - my) > 25)

    return far_count < 250

for iteration in tqdm(urange()):
    for r in robots:
        r.x = (r.x + r.vx) % width
        r.y = (r.y + r.vy) % height

    if is_compact():
        break

for y in range(height):
    for x in range(width):
        count = sum(1 for r in robots if r.x == x and r.y == y)
        print(count if count else '.', end='')
    print()

print(iteration + 1)
