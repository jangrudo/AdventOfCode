from aoc_shortcuts import *

f = open('input')

dense = [int(c) for c in f.readline().strip()]

# i denotes left boundary of the memory block.
Block = xtuple('size i')

# This essentially functions as 10 adjacent arrays (one per block size), each sorted by i.
free = SortedList()
used = []

i = 0
is_free = False

for size in dense:
    if is_free:
        free.add(Block(size, i))
    else:
        used.append(Block(size, i))

    i += size
    is_free = not is_free

for ident in tqdm(range(len(used) - 1, -1, -1)):

    # For each block size, find the leftmost free block. Among these, once again pick the
    # leftmost one.

    imin = None
    kbest = None
    for size in range(used[ident].size, 10):

        # Index of the leftmost block among free blocks of the given size.
        k = free.bisect_left(Block(size, 0))

        # If such a block exists and is available for relocation, include if in the final
        # calculation for the minimal i. Also record its index k within the free array.
        if k < len(free) and free[k].i < used[ident].i:
            imin, kbest = argmin(imin, kbest, free[k].i, k)

    # Remove the found free block, and replace it with a smaller one.
    if kbest is not None:
        free_block = free.pop(kbest)

        used[ident] = Block(used[ident].size, free_block.i)

        nsize = free_block.size - used[ident].size
        ni = free_block.i + used[ident].size

        free.add(Block(nsize, ni))

total = 0

for ident, block in enumerate(used):
    for i in range(block.i, block.i + block.size):
        total += i * ident

print(total)
