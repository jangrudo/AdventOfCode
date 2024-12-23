from aoc_shortcuts import *

f = open('input')

PAD_0 = [list('789'), list('456'), list('123'), [None, '0', 'A'] ]
PAD_1 = [[None, '^', 'A'], list('<v>')]

# "Path" here denotes a series of directional keypad presses which allows to travel
# between a pair of keys (it's also followed by an "A" key press).
#
# Any directional keypad sequence can be represented as a series of such paths. With the
# addition of every extra robot, such a series of paths is transformed into a new, longer
# series, and for every original path there may be up to 2 transformation options to
# choose from. Nevertheless, the new series would always consist of the same fundamental
# building blocks.
#
# This allows to use dynamic programming to look up the ultimate total key press count
# for each fundamental path at each recursion level. At the initial manual keypad entry
# level, the total key press count equals to path length (plus the extra "A" button). To
# calculate it at a deeper level, we only need to have a lookup table for all the totals
# from one step before.
#
# Now, for any path, we also don't really need to care about its exact step counts in
# every direction, only about the total step count and the directions themselves (and
# their order). That's because adding more steps amounts to hitting the same button a few
# times more, which after the transformation becomes hitting the "A" button a few times
# more, and ultimately doesn't result in complicating the final total key press count.
#
# So, we store a path as a pair of "core" (one or two principal directions) and "extra"
# (total number of steps, minus the ones already covered in "core", and also minus the
# obligatory final "A" key press). For the lookup table, we only really need the "core".
#
# Also, this allows to simplify things a bit when we finally calculate the ultimate key
# press count for the numeric keypad (which has longer paths).
Path = xtuple('core extra')

path_cores = []  # The list of possible path cores actually isn't that long.
for d1 in STEP:
    path_cores.append(d1)
    for d2 in STEP:
        if d2 != d1 and d2 != TURN_BACK[d1]:
            path_cores.append(d1 + d2)

# Check if a path is valid for the given keypad (doesn't hit the empty slot).
def is_valid_path(pad, path, start, finish):
    if pad == PAD_0:
        if start in '0A' and finish in '147' and path[0] == '<':
            return False
        if start in '147' and finish in '0A' and path[0] == 'v':
            return False

    elif pad == PAD_1:
        if start in '<' and finish in '^A' and path[0] == '^':
            return False
        if start in '^A' and finish in '<' and path[0] == '<':
            return False

    return True

# Find all the paths between every key pair, which are both reasonable (don't change
# direction more than once) and possible (don't fall outside the keypad).
def calculate_paths(pad):
    paths = {}

    for i0, j0 in mrange(pad):
        for fi, fj in mrange(pad):

            # "Empty" paths (repeated key presses) have to be handled separately.
            if (i0, j0) == (fi, fj):
                continue

            start = pad[i0][j0]
            finish = pad[fi][fj]

            if start is None or finish is None:
                continue

            di, dj = fi - i0, fj - j0

            dir_i = 'v' if di >= 0 else '^'
            dir_j = '>' if dj >= 0 else '<'

            path1 = dir_i * abs(di) + dir_j * abs(dj)
            path2 = dir_j * abs(dj) + dir_i * abs(di)

            if path1 == path2:
                # Straight paths are always valid.
                paths[(start, finish)] = [Path(path1[0], len(path1) - 1)]

            else:
                assert len(path1) == len(path2)
                paths[(start, finish)] = []

                if is_valid_path(pad, path1, start, finish):
                    paths[(start, finish)].append(Path(dir_i + dir_j, len(path1) - 2))

                if is_valid_path(pad, path2, start, finish):
                    paths[(start, finish)].append(Path(dir_j + dir_i, len(path2) - 2))

    return paths

cached_paths_0 = calculate_paths(PAD_0)
cached_paths_1 = calculate_paths(PAD_1)

# Given the lookup table for total path lengths at previous recursion level, calculate
# the total key press count for the given key sequence at the current recursion level.
# The sequence is called "bare" because it doesn't contain the obligatory trailing "A"
# (so that this could also be used to update total key press counts for path cores).
def calculate_length(length_lookup, bare_sequence, cached_paths):

    current_key = 'A'

    sequence = bare_sequence + 'A'
    length = 0

    for c in sequence:
        # Optional, as repeating keys don't really seem to appear in the input file.
        if c == current_key:
            length += 1
            continue

        length += min(
            length_lookup[path.core] + path.extra
            for path in cached_paths[(current_key, c)]
        )
        current_key = c

    return length

length_lookup = {}

# At the manual entry level, total key press calculation is simple.
for core in path_cores:
    length_lookup[core] = len(core) + 1

for depth in range(25):
    next_length_lookup = {}

    for core in path_cores:
        next_length_lookup[core] = calculate_length(length_lookup, core, cached_paths_1)

    length_lookup = next_length_lookup

def optimize(sequence):

    return calculate_length(length_lookup, sequence[: -1], cached_paths_0)

total = 0

for s in lines(f):
    code = int(s.rstrip('A'))

    length = optimize(s)
    print(s, length)
    total += length * code

print(total)
