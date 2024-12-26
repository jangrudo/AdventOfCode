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

largest = set()

for i in range(len(nodes) - 2):
    for j in range(i + 1, len(nodes) - 1):
        if (nodes[i], nodes[j]) in connected:
            for k in range(j + 1, len(nodes)):
                if (
                    (nodes[i], nodes[k]) in connected and
                    (nodes[j], nodes[k]) in connected
                ):
                    largest.add(tuple(sorted([nodes[i], nodes[j], nodes[k]])))

def enlarge(largest):
    nlargest = set()

    for big in tqdm(largest, desc=f'Subgraphs {len(list(largest)[0])} found '):

        for node in nodes:
            if node not in big:
                node_connected = True
                for i in range(len(big)):
                    if (big[i], node) not in connected:
                        node_connected = False
                        break

                if node_connected:
                    nlargest.add(tuple(sorted(list(big) + [node])))

    return nlargest

while True:
    nlargest = enlarge(largest)
    if len(nlargest) == 0:
        break
    largest = nlargest

print(','.join(s for s in list(largest)[0]))
