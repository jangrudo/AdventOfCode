from aoc_shortcuts import *

f = open('input')

values = {}

for s in lines(f):
    key, value = s.split(': ')
    values[key] = int(value)

Rule = xtuple('l r op target')

rules = []
nodes = set()

for s in lines(f):
    l, op, r, _, target = s.split()
    rules.append(Rule(l, r, op, target))

    nodes.add(l)
    nodes.add(r)
    nodes.add(target)

while len(values) < len(nodes):
    for rule in rules:
        if rule.target not in values and rule.l in values and rule.r in values:

            if rule.op == 'AND':
                values[rule.target] = values[rule.l] & values[rule.r]
            elif rule.op == 'OR':
                values[rule.target] = values[rule.l] | values[rule.r]
            elif rule.op == 'XOR':
                values[rule.target] = values[rule.l] ^ values[rule.r]
            else:
                assert False

zets = sorted([node for node in values if node.startswith('z')])

maxbit = int(zets[-1].lstrip('z'))

number = 0
power = 1
for bit in range(maxbit + 1):
    key = f'z{bit:02d}'
    number += power * values[key]
    power *= 2

print(number)
