from aoc_shortcuts import *

f = open('input')

lines(f)  # Ignore input values.

Rule = xclass('l r op target')

rules = []
nodes = set()

for s in lines(f):
    l, op, r, _, target = s.split()
    rules.append(Rule(l, r, op, target))

    nodes.update([l, r, target])

BITS = 45

# Manual inspection of the input reveals a highly regular design, which processes lower
# bits first, and only uses data from one previous step to compute the next output bit.
#
# For each pair of input nodes ("x" and "y"), a pair of "and" and "xor" nodes is computed
# first. Then, we also have a "carry" flag which is set to 1 if the result computed so
# far doesn't fit into the current bit space, and an overflow occurs. It's computed as
#
#   `carry[i] = and[i] | (xor[i] & carry[i-1])`
#
# where `(xor[i] & carry[i-1])` is another ("extra") intermediate node used per bit.
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
# We'll try to unwind this design (starting from the least significant bits), see where
# it's broken, and try to correct the errors on the fly.

def fix_circuit():
    swapped_nodes = []  # List of rule targets swapped so far.

    mapping = {}  # A dictionary mapping logical node names to real names.

    # The names of the input nodes are already quite logical.
    for node in nodes:
        if node[0] in 'xy':
            mapping[node] = node

    # On the first tier, we have "and" and "xor" nodes, directly connected to the inputs.
    for rule in rules:
        if rule.l[0] in 'xy' or rule.r[0] in 'xy':
            # Inputs from both numbers should appear in the same rule (in any order).
            assert set([rule.l[0], rule.r[0]]) == {'x', 'y'}
            assert rule.l[1:] == rule.r[1:]

            if rule.op == 'AND':
                mapping['and' + rule.l[1:]] = rule.target
            elif rule.op == 'XOR':
                mapping['xor' + rule.l[1:]] = rule.target
            else:
                assert False

    # For bit 0, some nodes shall also have a second logical name.
    mapping['carry00'] = mapping['and00']
    mapping['z00'] = mapping['xor00']

    for bit in range(1, BITS):
        prev = bit - 1

        xor_cur = f'xor{bit:02}'  # Names of the "xor" and "and" nodes (already mapped).
        and_cur = f'and{bit:02}'
        carry_prev = f'carry{prev:02}'  # Previous "carry" node (already mapped).
        carry_cur = f'carry{bit:02}'    # "carry" node for the current bit.
        extra_cur = f'extra{bit:02}'    # "extra" node for the current bit.
        z_cur = f'z{bit:02}'            # Output node for the current bit.

        # First, we need to map the "extra" node for the current bit ("carry" needs it).
        for rule in rules:
            if (
                rule.op == 'AND' and
                set([rule.l, rule.r]) == set([mapping[xor_cur], mapping[carry_prev]])
            ):
                mapping[extra_cur] = rule.target
                break  # Only one such node can exist if the design is correct.
        else:
            # If the rule is not found, it means that one (or both) of its operand nodes
            # is incorrectly mapped. Assuming that only one of the operand nodes can be
            # swapped in any given rule (which seems to hold across available input
            # files), try to find out which of the operand nodes could be replaced with
            # something else. To do this, search for the "AND" rule which has exactly one
            # of its arguments matching either of the two nodes that we have here.
            #
            # If the search succeeds, swap the two nodes (and update the mapping).
            node1, node2, target = find_swap(
                'AND', mapping[xor_cur], mapping[carry_prev]
            )
            mapping[extra_cur] = target
            swap_rules(mapping, node1, node2)
            swapped_nodes.extend([node1, node2])

        # Similarly, search for the "carry" node (and correct the circuit if needed).
        for rule in rules:
            if (
                rule.op == 'OR' and
                set([rule.l, rule.r]) == set([mapping[and_cur], mapping[extra_cur]])
            ):
                mapping[carry_cur] = rule.target
                break
        else:
            node1, node2, target = find_swap(
                'OR', mapping[and_cur], mapping[extra_cur]
            )
            mapping[carry_cur] = target
            swap_rules(mapping, node1, node2)
            swapped_nodes.extend([node1, node2])

        # Finally, do the same for the output ("z") node.
        for rule in rules:
            if (
                rule.op == 'XOR' and
                set([rule.l, rule.r]) == set([mapping[xor_cur], mapping[carry_prev]])
            ):
                mapping[z_cur] = rule.target
                break
        else:
            node1, node2, target = find_swap(
                'XOR', mapping[xor_cur], mapping[carry_prev]
            )
            mapping[z_cur] = target
            swap_rules(mapping, node1, node2)
            swapped_nodes.extend([node1, node2])

    # If we've got here, it means the entire design has been untangled, and all the nodes
    # mapped. However, we haven't checked yet if output mappings are actually correct.
    # Luckily, it looks like in available input files output nodes are never swapped.
    for bit in range(BITS):
        z_cur = f'z{bit:02}'
        assert mapping[z_cur] == z_cur

    # The most significant bit of the output should be mapped to the last "carry" flag.
    assert mapping['carry44'] == 'z45'

    return swapped_nodes

Swap = xtuple('node1 node2 target')

# Search for a rule which contains exactly one of the required operands.
def find_swap(op, required1, required2):

    candidates = []

    for rule in rules:
        if rule.op == op:
            if rule.l == required1:
                candidates.append(Swap(rule.r, required2, rule.target))
            elif rule.r == required1:
                candidates.append(Swap(rule.l, required2, rule.target))
            elif rule.l == required2:
                candidates.append(Swap(rule.r, required1, rule.target))
            elif rule.r == required2:
                candidates.append(Swap(rule.l, required1, rule.target))

    assert len(candidates) == 1

    swap = candidates[0]
    print((swap.node1, swap.node2))
    return swap

# Update the mapping dictionary after having swapped two given nodes.
def swap_mappings(mapping, node1, node2):

    # Find logical names pointing to node1 and node2, if any.
    for source in mapping:
        if mapping[source] == node1:
            mapping[source] = node2
        elif mapping[source] == node2:
            mapping[source] = node1

def swap_rules(mapping, target1, target2):
    rule1 = [r for r in rules if r.target == target1][0]
    rule2 = [r for r in rules if r.target == target2][0]

    rule1.target, rule2.target = rule2.target, rule1.target

    swap_mappings(mapping, target1, target2)

swapped_nodes = fix_circuit()

print(','.join(sorted(swapped_nodes)))
