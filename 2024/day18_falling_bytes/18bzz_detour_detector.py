from aoc_shortcuts import *

f = open('input')

falls = [tuple(ints(line)) for line in f]

size = (71, 71)

m = mcreate(size, '.')

start = (0, 0)
finish = (size[0] - 1, size[1] - 1)

for fall in falls[: 1024]:
    m[fall[1]][fall[0]] = '#'

Partition = xclass('q visited', nq=None)

def can_move(ifall, jfall):

    # The fallen block may partition the labyrinth into up to 4 different areas. Start
    # discovering them, beginning with the cells adjacent to the fallen block. At any
    # moment in time, partitions discovered so far shall consist of cells which are
    # reachable from the starting points within a given number of steps. Whenever some
    # cell turns out to be reachable from more than one starting point, merge all the
    # partitions containing it into a single one. This essentially allows to discover all
    # the shortest detours around the newly blocked cell.
    #
    # If any of the partitions becomes completely discovered, and it contains neither the
    # starting nor the final points, then it's a dead end, and can be safely ignored. If
    # it contains both these points, then obviously they are connected. If it only
    # contains one point, but not the other, the connection is not possible any more.
    #
    # If at some moment only one partitions remains, it means that all the cells around
    # the fallen block are either interconnected or lead to dead ends, and so the
    # labyrinth is still traversable. If no partitions remain, it means the fallen block
    # is completely surrounded by dead ends, and can be ignored as well.
    partitions = []
    for i, j in deltas(m, ifall, jfall):
        if m[i][j] != '#':
            partitions.append(Partition({(i, j)}, {(i, j)}))

    while True:
        if len(partitions) <= 1:
            return True

        for part in partitions:  # Process each partition independently.

            part.nq = set()

            for i, j in part.q:
                for ni, nj in deltas(m, i, j):
                    if m[ni][nj] != '#' and (ni, nj) not in part.visited:
                        part.visited.add((ni, nj))
                        part.nq.add((ni, nj))

                part.q = part.nq

        dead_partitions = []  # Indices to be removed.

        for k, part in enumerate(partitions):

            if start in part.visited and finish in part.visited:
                return True  # Both points are reachable within the same partition.

            if len(part.nq) == 0:  # Partition completely discovered.
                if start in part.visited or finish in part.visited:
                    return False  # One of the points is rechable, but not the other.

                dead_partitions.append(k)
                continue

            # For any pair of partitions, check if they can be merged.
            for n, npart in enumerate(partitions[k + 1 :]):

                # When growing partitions meet each other, the meeting points are always
                # among the recently added ones, and can be found in any such partition.
                if any(point in npart.visited for point in part.nq):

                    # Keep the partition with the greater index, so that we don't have to
                    # skip dead partitions later on.
                    npart.nq |= part.nq
                    npart.visited |= part.visited

                    dead_partitions.append(k)
                    break

        # Reversed order is needed to prevent modifications of the indices being removed.
        for k in reversed(dead_partitions):
            del partitions[k]

for fallen in range(1024, len(falls)):

    ifall, jfall = reversed(falls[fallen])

    m[ifall][jfall] = '#'

    if not can_move(ifall, jfall):
        break

m[falls[fallen][1]][falls[fallen][0]] = 'O'
mprint(m)

print(','.join(str(x) for x in falls[fallen]))
