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

largest = []

for i in range(len(nodes) - 2):
    for j in range(i + 1, len(nodes) - 1):
        if (nodes[i], nodes[j]) in connected:
            for k in range(j + 1, len(nodes)):
                if (
                    (nodes[i], nodes[k]) in connected and
                    (nodes[j], nodes[k]) in connected
                ):
                    largest.append((i, j, k))

def enlarge(largest):
    nlargest = []

    for big in tqdm(largest, desc=f'Subgraphs {len(largest[0])} found '):

        for i in range(big[-1] + 1, len(nodes)):
            node_connected = True
            for k in big:
                if (nodes[k], nodes[i]) not in connected:
                    node_connected = False
                    break

            if node_connected:
                nlargest.append(big + (i,))

    return nlargest

while True:
    nlargest = enlarge(largest)
    if len(nlargest) == 0:
        break
    largest = nlargest

print(','.join(nodes[k] for k in largest[0]))
