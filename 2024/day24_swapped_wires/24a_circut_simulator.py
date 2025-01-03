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

    nodes.update([l, r, target])

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

zets = sorted([n for n in nodes if n.startswith('z')])

# Reverse the string so that most significant bits come first.
bits = ''.join(str(values[n]) for n in zets)[::-1]

print(int(bits, base=2))
