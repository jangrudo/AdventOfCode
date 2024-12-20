# Idea stolen from here: https://github.com/KajaBraz/AdventOfCode2024

from aoc_library import *

with open('input') as f:
    initial_reg = [ints(s)[0] for s in lines(f)]

    program = ints(f.readline())

# The program in the input files seems to consist of a single loop, which converts the
# value in register `a` to some output value (without using any extra data, and without
# modifying the register `a` itself), then divides the value in register `a` by 8, and
# exits when `a` becomes zero.
#
# Therefore, at any iteration, future output of the program only depends on the value in
# register `a`, and its previous values are obtained by adding extra bits to the current
# one (3 bits at a time). We can thus match the output backwards, and by always trying
# smaller 3-bit extensions first, the'd make sure that the first value matching the
# entire output would also be the smallest possible.

def get_combo(reg, arg):
    if arg <= 3:
        return arg
    assert arg != 7
    return reg[arg - 4]

# Only need one character, provided that what follows has already been matched.
def get_first_output(program, reg):

    ip = 0

    while ip + 1 < len(program):

        opcode = program[ip]
        arg = program[ip + 1]

        if opcode == 0:
            reg[0] //= 2 ** get_combo(reg, arg)

        elif opcode == 1:
            reg[1] ^= arg

        elif opcode == 2:
            reg[1] = get_combo(reg, arg) % 8

        elif opcode == 3:
            assert False  # Expect some output in every iteration (before the jump).

        elif opcode == 4:
            reg[1] ^= reg[2]

        elif opcode == 5:
            return get_combo(reg, arg) % 8

        elif opcode == 6:
            reg[1] = reg[0] // 2 ** get_combo(reg, arg)

        elif opcode == 7:
            reg[2] = reg[0] // 2 ** get_combo(reg, arg)

        ip += 2

def iterate(reg_a, matched_count):
    if matched_count == len(program):
        return reg_a

    for extra in range(8):
        prev_reg_a = reg_a * 8 + extra

        reg = initial_reg.copy()
        reg[0] = prev_reg_a

        output = get_first_output(program, reg)
        if output == program[len(program) - matched_count - 1]:

            result = iterate(prev_reg_a, matched_count + 1)
            if result is not None:
                return result

    return None

print(iterate(0, 0))
