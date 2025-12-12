from aoc_shortcuts import *

f = open('input')

shapes = []
shape_index = []
shape_sizes = []

def rotate(shape):
    m = mcreate((3, 3), '.')
    for i, j in mrange(shape):
        m[j][len(m) - 1 - i] = shape[i][j]
    return tuple(''.join(m[i]) for i in range(len(m)))

def flip(shape):
    m = mcreate((3, 3), '.')
    for i, j in mrange(shape):
        m[len(m) - 1 - i][j] = shape[i][j]
    return tuple(''.join(m[i]) for i in range(len(m)))

index = 0
count = 0

while block := lines(f):
    if block[0].endswith(':'):
        shape = tuple(block[1:])
        shape_sizes.append(mcount(shape, '#'))

        flipped = flip(shape)
        assert shape not in shapes
        shapes.append(shape)
        shape_index.append(index)
        if flipped not in shapes:
            shapes.append(flipped)
            shape_index.append(index)

        for k in range(3):
            shape = rotate(shape)
            flipped = flip(shape)
            if shape not in shapes:
                shapes.append(shape)
                shape_index.append(index)
            if flipped not in shapes:
                shapes.append(flipped)
                shape_index.append(index)

        index += 1

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
