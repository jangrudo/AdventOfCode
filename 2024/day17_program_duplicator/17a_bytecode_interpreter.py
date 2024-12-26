from aoc_shortcuts import *

f = open('input')

reg = [a[0] for a in lints(f)]

program = ints(f)

def get_combo(arg):
    if arg <= 3:
        return arg
    assert arg != 7
    return reg[arg - 4]

ip = 0

output = []

while ip + 1 < len(program):

    opcode = program[ip]
    arg = program[ip + 1]

    if opcode == 0:
        reg[0] //= 2 ** get_combo(arg)

    elif opcode == 1:
        reg[1] ^= arg

    elif opcode == 2:
        reg[1] = get_combo(arg) % 8

    elif opcode == 3:
        if reg[0] != 0:
            ip = arg
            continue

    elif opcode == 4:
        reg[1] ^= reg[2]

    elif opcode == 5:
        output.append(get_combo(arg) % 8)

    elif opcode == 6:
        reg[1] = reg[0] // 2 ** get_combo(arg)

    elif opcode == 7:
        reg[2] = reg[0] // 2 ** get_combo(arg)

    ip += 2

print(','.join(str(x) for x in output))
