from aoc_library import *

with open('input') as f:
    s = f.read()

ops = re.findall(r'mul\(\d{1,3},\d{1,3}\)', s)

total = 0

for op in ops:
    op1, op2 = ints(op)
    total += op1 * op2

print(total)
