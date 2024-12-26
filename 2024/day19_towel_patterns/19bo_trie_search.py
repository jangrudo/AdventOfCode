from aoc_shortcuts import *

f = open('input')

TrieNode = xclass('', leaf=False, children={})

root = TrieNode()

def trie_add(node, pattern):
    for c in reversed(pattern):
        if c not in node.children:
            node.children[c] = TrieNode()
        node = node.children[c]

    node.leaf = True

def trie_search(node, s, i_final):
    for i in range(i_final, -1, -1):
        c = s[i]

        if c not in node.children:
            return

        node = node.children[c]
        if node.leaf:
            yield i

def solvable_count(s):
    found = [False] * (len(s) + 1)
    found[0] = True

    for i in range(1, len(s) + 1):
        for prev_i in trie_search(root, s, i - 1):
            found[i] += found[prev_i]

    return found[len(s)]

for pattern in lines(f)[0].split(', '):
    trie_add(root, pattern)

print(sum(solvable_count(s) for s in lines(f)))
