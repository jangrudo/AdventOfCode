from aoc_shortcuts import *

open_input('input')

a = ints(lines()[0])

Node = xclass('value', nxt=None)

root = Node(a[0])
tail = root

for x in a[1:]:
    node = Node(x)
    tail.nxt = node
    tail = node

for iteration in tqdm(range(25)):

    node = root
    while node is not None:
        s = str(node.value)

        if node.value == 0:
            node.value = 1

        elif len(s) % 2 == 0:
            value1 = int(s[: len(s) // 2])
            value2 = int(s[len(s) // 2 :])
            node.value = value1
            new = Node(value2)
            new.nxt = node.nxt
            node.nxt = new
            node = new

        else:
            node.value *= 2024

        node = node.nxt

def count_nodes(node):
    count = 0
    while node is not None:
        count += 1
        node = node.nxt
    return count

print(count_nodes(root))
