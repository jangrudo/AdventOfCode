from aoc_library import *

with open('input') as f:
    dense = [int(x) for x in f.readline().strip()]

class Block:
    def __init__(self, i, size):
        # i denotes left boundary of the memory block.
        self.i = i
        self.size = size

    def __lt__(self, other):
        if self.size != other.size:
            return self.size < other.size
        return self.i < other.i

# This essentially functions as 10 adjacent arrays (one per block size), each sorted by i.
free = SortedList()
used = []

i = 0
for ident in urange():
    size = dense[ident * 2]
    used.append(Block(i, size))
    i += size

    if ident * 2 + 1 == len(dense):
        break

    size = dense[ident * 2 + 1]
    free.add(Block(i, size))
    i += size

for ident in reversed(range(len(used))):

    # For each block size, find the leftmost free block. Among these, once again pick the
    # leftmost one.

    imin = None
    kbest = None
    for size in range(used[ident].size, 10):

        # Index of the leftmost block among free blocks of the given size.
        k = free.bisect_left(Block(0, size))

        # If such a block exists and is available for relocation, include if in the final
        # calculation for the minimal i. Also record its index k within the free array.
        if k < len(free) and free[k].i < used[ident].i:
            imin, kbest = argmin(imin, kbest, free[k].i, k)

    # Remove the found free block, and replace it with a smaller one.
    if kbest is not None:
        block = free.pop(kbest)

        used[ident].i = block.i

        block.i += used[ident].size
        block.size -= used[ident].size

        free.add(block)

total = 0

for ident, block in enumerate(used):
    for i in range(block.i, block.i + block.size):
        total += i * ident

print(total)

print_finish_time()
