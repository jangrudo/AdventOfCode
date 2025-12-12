from aoc_shortcuts import *

f = open('input')

shape_sizes = []
count = 0

while block := lines(f):
    if block[0].endswith(':'):
        shape = tuple(block[1:])
        shape_sizes.append(mcount(shape, '#'))

    else:
        for line in block:
            items = line.split()
            width, height = ints(items[0])
            target = tuple(int(item) for item in items[1:])
            area = width * height
            total_size = sum(shape_sizes[i] * target[i] for i in range(len(target)))
            if area >= total_size:
                print(area, total_size, area - total_size, target)
                count += 1

print(count)
