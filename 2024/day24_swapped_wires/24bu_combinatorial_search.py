from aoc_shortcuts import *

import random

f = open('input')

lines(f)  # Ignore input values.

Rule = xclass('l r op target')

rules = []
nodes = set()

for s in lines(f):
    l, op, r, _, target = s.split()
    rules.append(Rule(l, r, op, target))

    nodes.add(l)
    nodes.add(r)
    nodes.add(target)

BITS = 45

def set_values(values, prefix, number):
    bit = 0
    for bit in range(BITS):
        key = f'{prefix}{bit:02}'
        values[key] = 1 if (number & (2 ** bit) != 0) else 0

def simulate(x, y):

    values = {}

    set_values(values, 'x', x)
    set_values(values, 'y', y)

    while len(values) < len(nodes):
        updated = False
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

                updated = True

        # Exit upon reaching a dead end (might happen when tinkering with wires).
        if not updated:
            return None

    number = 0

    for bit in range(BITS + 1):
        key = f'z{bit:02}'
        number += (2 ** bit) * values[key]

    return number

def get_random(maxbits):
    return random.randint(0, 2 ** maxbits - 1)

def test_circuit():

    # A few random tries seems enough to detect the flaws we find in the input files.
    # (The most challenging to find would be errors near the most significant bit, but
    # even for these we'd get 99.9% success rate with 300 checks).
    for i in range(300):
        x = get_random(BITS)
        y = get_random(BITS)
        z = simulate(x, y)

        if x + y != z:
            return False

    return True

def swap_rules(target1, target2):
    r1 = [rule for rule in rules if rule.target == target1]
    r2 = [rule for rule in rules if rule.target == target2]

    assert len(r1) == 1
    assert len(r2) == 1

    rule1 = r1[0]
    rule2 = r2[0]

    target1 = rule1.target
    target2 = rule2.target

    rule1.target = target2
    rule2.target = target1

# Manual inspection of the input reveals a highly regular design, which processes lower
# bits first, and only uses data from one previous step to compute the next output bit.
#
# For each pair of input nodes ("x" and "y"), a pair of "and" and "xor" nodes is computed
# first. Then, we also have a "carry" flag, which indicates if the result computed so far
# fits into the current bit space, or an overflow occurs. It's computed as
#
#   `carry[i] = and[i] | (xor[i] & carry[i-1])`
#
# where `(xor[i] & carry[i-1])` is another intermediate node used per bit.
#
# The value of the output "z" node is computed as
#
#   `z[i] = xor[i] ^ carry[i-1]`
#
# which effectively adds the 3 bits together.
#
# The two exceptions to this are bit 0, which doesn't have a "carry" flag (the
# corresponding "and" node is used instead), and the last bit 45, for which the output is
# taken directly from the last "carry" flag, as there are no more inputs to xor it with.
#
# This means that "XOR" operators can either process a pair of input nodes ("x" and "y"),
# or generate an output "z" bit (except for the last one, "z45", which is generated with
# an "OR" operator), or both (for output "z00"). However, an "XOR" can never take an
# intermediate node as input, and produce another intermediate node as output.
#
# On the other hand, output bits (except for "z45") can never be produced by rules other
# than "XOR".
#
# Luckily, there are exactly 6 rules in the input which break one of the two above
# mentioned laws (3 rules per law). Each of the rules in these two groups only fits into
# the opposite group, and doesn't fit anywhere else (provided that each rule is only
# allowed to be swapped once). Therefore, these 6 "flawed" rules form 3 pairs, with each
# pair spanning both groups, so the total number of possible pair triplets is 6.
#
# Now, we only need to find one missing swap, which is doable by trying them all.

flawed_middles = []

for rule in rules:
    if (
        rule.op == 'XOR' and
        rule.l[0] not in 'xy' and rule.r[0] not in 'xy' and rule.target[0] != 'z'
    ):
        print(rule)
        flawed_middles.append(rule.target)

flawed_zets = []

for rule in rules:
    if rule.op != 'XOR' and rule.target[0] == 'z' and rule.target != 'z45':
        print(rule)
        flawed_zets.append(rule.target)

assert len(flawed_middles) == 3
assert len(flawed_zets) == 3

# Each rule can be uniquely identified by its target.
alltargets = sorted(list(set(rule.target for rule in rules)))

for i in range(3):
    for j in range(3):
        for k in range(3):
            if len(set([i, j, k])) != 3:
                continue

            swap_rules(flawed_middles[0], flawed_zets[i])
            swap_rules(flawed_middles[1], flawed_zets[j])
            swap_rules(flawed_middles[2], flawed_zets[k])

            progress = tqdm(  # Calculate the toal pair count for steady progress.
                total = len(alltargets) * (len(alltargets) - 1) // 2,
                desc = str((i, j, k))
            )

            for ii1 in range(len(alltargets) - 1):
                for ii2 in range(ii1 + 1, len(alltargets)):
                    node1 = alltargets[ii1]
                    node2 = alltargets[ii2]

                    if (
                        node1 not in flawed_middles and node1 not in flawed_zets and
                        node2 not in flawed_middles and node2 not in flawed_zets
                    ):
                        swap_rules(node1, node2)

                        if test_circuit():
                            progress.close()

                            print(
                                (flawed_middles[0], flawed_zets[i]),
                                (flawed_middles[1], flawed_zets[j]),
                                (flawed_middles[2], flawed_zets[k]),
                                (node1, node2)
                            )
                            print(','.join(sorted(
                                flawed_middles + flawed_zets + [node1, node2]
                            )))
                            exit()

                        swap_rules(node1, node2)  # Undo the swap made above.

                    progress.update(1)

            swap_rules(flawed_middles[0], flawed_zets[i])  # Undo the swaps made above.
            swap_rules(flawed_middles[1], flawed_zets[j])
            swap_rules(flawed_middles[2], flawed_zets[k])

            progress.close()
