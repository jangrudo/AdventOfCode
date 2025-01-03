from aoc_shortcuts import *

f = open('input')

nodes = set()
edges = set()

for s in lines(f):
    l, r = s.split('-')
    edges.add((l, r))
    edges.add((r, l))
    nodes.add(l)
    nodes.add(r)

nodes = sorted(nodes)

count = 0

for i in range(len(nodes) - 2):
    for j in range(i + 1, len(nodes) - 1):
        if (nodes[i], nodes[j]) in edges:
            for k in range(j + 1, len(nodes)):
                if (nodes[i], nodes[k]) in edges and (nodes[j], nodes[k]) in edges:
                    if any(nodes[a][0] == 't' for a in (i, j, k)):
                        count += 1

print(count)
