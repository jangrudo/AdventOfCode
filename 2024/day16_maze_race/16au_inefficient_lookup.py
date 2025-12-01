from aoc_shortcuts import *

with open('input') as f:
    m = mread(f)

Node = xtuple('i j direction')

i0, j0 = mfind(m, 'S')
fi, fj = mfind(m, 'E')

def next_nodes(node, length):
    nodes = [
        (Node(node.i, node.j, TURN_LEFT[node.direction]), length + 1000),
        (Node(node.i, node.j, TURN_RIGHT[node.direction]), length + 1000),
    ]
    di, dj = STEP[node.direction]
    ni, nj = node.i + di, node.j + dj
    if m[ni][nj] != '#':
        nodes.append((Node(ni, nj, node.direction), length + 1))

    return nodes

q = {Node(i0, j0, '>') : 0}
marked = {}

targets = [Node(fi, fj, d) for d in STEP]

total_node_count = mcount(m, '.SE') * 4
progress = tqdm(total = total_node_count)

while any(target not in marked for target in targets):

    minlength = None
    bestnode = None
    for node, length in q.items():
        minlength, bestnode = argmin(minlength, bestnode, length, node)

    del q[bestnode]

    marked[bestnode] = minlength
    progress.update(1)

    for nnode, nlength in next_nodes(bestnode, minlength):
        if nnode not in marked and (nnode not in q or q[nnode] > nlength):
            q[nnode] = nlength

progress.update(total_node_count - len(marked))
progress.close()

min_score = min(marked[node] for node in targets)

print(min_score)
