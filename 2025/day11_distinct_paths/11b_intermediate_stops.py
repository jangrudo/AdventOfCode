from aoc_shortcuts import *

f = open('input')

Node = xtuple('name children')

nodes = {}

for line in f:
    items = line.split()
    name = items[0].rstrip(':')
    nodes[name] = Node(name, items[1:])

def paths(start, finish):
    path_count = {name : 0 for name in nodes}
    path_count[start] = 1
    finish_paths = 0

    q = {start}

    while len(q) > 0:
        nq = set()
        for name in q:
            for child in nodes[name].children:
                if child == finish:
                    finish_paths += path_count[name]
                elif child != 'out':
                    path_count[child] += path_count[name]
                    nq.add(child)
            # This is needed to prevent counting these paths more times in the future.
            path_count[name] = 0
        q = nq

    return finish_paths

print(paths('svr', 'dac'), paths('dac', 'fft'), paths('fft', 'out'))
print(paths('svr', 'fft'), paths('fft', 'dac'), paths('dac', 'out'))

total = paths('svr', 'dac') * paths('dac', 'fft') * paths('fft', 'out')
total += paths('svr', 'fft') * paths('fft', 'dac') * paths('dac', 'out')

print(total)
