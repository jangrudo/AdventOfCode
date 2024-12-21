from aoc_shortcuts import *

open_input('input')

import numpy

width = 101
height = 103

Robot = xtuple('x y vx vy')

robots = [Robot(*ints(s)) for s in lines()]

x = numpy.array([r.x for r in robots], numpy.int32)
y = numpy.array([r.y for r in robots], numpy.int32)
vx = numpy.array([r.vx for r in robots], numpy.int32)
vy = numpy.array([r.vy for r in robots], numpy.int32)

def is_compact():

    # Center of mass (two scalar numpy.float64 values).
    mx = x.mean()
    my = y.mean()

    # The number of points away from the center of mass.
    #
    # Subtracion of a float scalar from an array of integers results in an array of
    # floats. Comparing an array to a scalar results in an array of booleans. Logical
    # operations between boolean arrays are element-wise. Summing an array of booleans is
    # equivalent to counting its True members.
    far_count = ((numpy.abs(x - mx) > 25) | (numpy.abs(y - my) > 25)).sum()

    return far_count < 250

for iteration in tqdm(urange()):
    x = (x + vx) % width
    y = (y + vy) % height

    if is_compact():
        break

for cy in range(height):
    print(''.join(
        str(count) if (
            count := ((x == cx) & (y == cy)).sum()
        ) > 0
        else '.' for cx in range(width)
    ))

print(iteration + 1)
