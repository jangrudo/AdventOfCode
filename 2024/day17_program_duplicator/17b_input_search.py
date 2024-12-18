from aoc_library import *

with open('input') as f:
    list(fblock(f))  # Ignore. Registers b and c seem to be always set to zero.

    program = ints(f.readline())

# The program seems to be nearly identical across various inputs, with 2 key parameters.
assert program[0 : 2] == [2, 4]       # b = a % 8

assert program[2] == 1
assert program[3] <= 7
xorparam_1 = program[3]               # b ^= xorparam_1

# Some of the following instructions can be reordered without affecting the final result.
assert {program[4], program[6], program[8], program[10], program[12]} == {7, 4, 1, 5, 0}

for ip in [4, 6, 8, 10, 12]:
    if program[ip] == 7:
        assert program[ip + 1] == 5   # c = a // (2 ** b)

    elif program[ip] == 4:
        pass  # Argument ignored.     # b ^= c

    elif program[ip] == 1:
        assert program[ip + 1] <= 7
        xorparam_2 = program[ip + 1]  # b ^= xorparam_2

    elif program[ip] == 5:
        assert program[ip + 1] == 5   # output b % 8

    elif program[ip] == 0:
        assert program[ip + 1] == 3   # a //= 8

assert program[14 : 16] == [3, 0]     # repeat until a == 0

# Program summary (for non-zero a):
#
# while a != 0:
#     x = (a % 8) ^ xorparam_1         # x is up to 3 bits long (0 <= x <= 7).
#     y = a // (2 ** x)                # Remove up to 7 bits from a, and store this in y.
#     print((x ^ y ^ xorparam_2) % 8)  # Only need 3 bits of y (i.e. up to 10 bits of a).
#     a //= 8                          # Remove the last 3 bits from a.

candidates = []

# "nibbles" are a list of 3-bit pieces sliced off the original number. "head" is 7 more
# bits needed to generate the output matched so far (one output digit per "nibble").
def iterate(nibbles, head):

    depth = len(nibbles)  # "depth" is the number of digits matched so far.

    if depth == len(program):
        if head == 0:  # The program terminates when "head" is zero.
            value = 0
            for nibble in reversed(nibbles):
                value = value * 8 + nibble
            candidates.append(value)
        return

    x = (head % 8) ^ xorparam_1

    # "extra" are 3 more bits needed to generate the next output digit.
    for extra in range(8):

        chunk = extra * 128 + head  # "chunk" contains all the data for the next digit.

        y = chunk // (2 ** x)
        b = (y ^ x ^ xorparam_2) % 8

        if b == program[depth]:  # Stop the recursion on first non-matching digit.
            nibbles.append(chunk % 8)
            iterate(nibbles, chunk // 8)
            nibbles.pop()

for head in range(128):  # Start with any of the possible 7-bit combinations.
    iterate([], head)

print(f'{len(candidates)} candidates found.')

print(sorted(candidates)[0])
