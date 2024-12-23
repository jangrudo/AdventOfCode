from aoc_shortcuts import *

f = open('input')

nodes = set()
connected = set()

for s in lines(f):
    l, r = s.split('-')
    connected.add((l, r))
    connected.add((r, l))
    nodes.add(l)
    nodes.add(r)

nodes = sorted(list(nodes))

count = 0

for i in range(len(nodes) - 2):
    for j in range(i + 1, len(nodes) - 1):
        if (nodes[i], nodes[j]) in connected:
            for k in range(j + 1, len(nodes)):
                if (
                    (nodes[i], nodes[k]) in connected and
                    (nodes[j], nodes[k]) in connected
                ):
                    if any(nodes[a][0] == 't' for a in (i, j, k)):
                        count += 1

print(count)
