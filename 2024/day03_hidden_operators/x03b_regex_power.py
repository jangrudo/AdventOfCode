from aoc_library import *

with open('input') as f:
    s = f.read()

ops = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', s)

total = 0
enabled = True

for op in ops:
    if op == "do()":
        enabled = True
    elif op == "don't()":
        enabled = False
    else:
        if enabled:
            op1, op2 = ints(op)
            total += op1 * op2

print(total)
