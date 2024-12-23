from aoc_shortcuts import *

f = open('input')

width = 101
height = 103

Robot = xclass('x y vx vy')

robots = [Robot(*ints(line)) for line in f]

for iteration in range(100):
    for r in robots:
        r.x = (r.x + r.vx) % width
        r.y = (r.y + r.vy) % height

halfwidth = width // 2
halfheight = height // 2

def get_count(x0, y0):
    return sum(
        1 for r in robots if
        x0 <= r.x < x0 + halfwidth and
        y0 <= r.y < y0 + halfheight
    )

count1 = get_count(0, 0)
count2 = get_count(0, height // 2 + 1)
count3 = get_count(width // 2 + 1, 0)
count4 = get_count(width // 2 + 1, height // 2 + 1)

print(count1 * count2 * count3 * count4)
