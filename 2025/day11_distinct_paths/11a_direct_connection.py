from aoc_shortcuts import *

f = open('input')

Node = xclass('name', children=[], paths=0)

nodes = {}

for line in f:
    items = line.split()
    name = items[0].rstrip(':')
    nodes[name] = Node(name)
    nodes[name].children = items[1:]

nodes['you'].paths = 1

out_paths = 0

q = {'you'}

while len(q) > 0:
    nq = set()
    for name in q:
        for child in nodes[name].children:
            if child == 'out':
                out_paths += nodes[name].paths
            else:
                nodes[child].paths += nodes[name].paths
                nq.add(child)
        # This line was missing from the original solution, which was a bug.
        nodes[name].paths = 0

    q = nq
    print(q)

print(out_paths)
