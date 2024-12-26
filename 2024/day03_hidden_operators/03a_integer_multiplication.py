from aoc_shortcuts import *

f = open('input')

ops = re.findall(r'mul\(\d{1,3},\d{1,3}\)', f.read())

total = 0

for op in ops:
    op1, op2 = ints(op)
    total += op1 * op2

print(total)
