from aoc_shortcuts import *

f = open('input')

m = mread(f)

Node = xtuple('i j d')

i0, j0 = mfind(m, 'S')
fi, fj = mfind(m, 'E')

def next_nodes(node, length):
    yield (Node(node.i, node.j, TURN_LEFT[node.d]), length + 1000)
    yield (Node(node.i, node.j, TURN_RIGHT[node.d]), length + 1000)

    ni, nj = mmove(node.i, node.j, node.d)
    if m[ni][nj] != '#':
        yield (Node(ni, nj, node.d), length + 1)

reached = {Node(i0, j0, '>') : 0}
q = SortedList((length, node) for node, length in reached.items())
solved = set()

targets = [Node(fi, fj, d) for d in STEP]

while any(target not in solved for target in targets):

    minlength, bestnode = q.pop(0)
    solved.add(bestnode)

    for node, length in next_nodes(bestnode, minlength):
        if node not in solved:

            if node not in reached:
                q.add((length, node))
                reached[node] = length

            elif length < reached[node]:
                q.remove((reached[node], node))
                q.add((length, node))
                reached[node] = length

min_score = min(reached[node] for node in targets)

print(min_score)
