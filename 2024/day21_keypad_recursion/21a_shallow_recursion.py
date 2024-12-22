from aoc_shortcuts import *

open_input('input')

PAD_0 = [list('789'), list('456'), list('123'), [None, '0', 'A'] ]
PAD_1 = [[None, '^', 'A'], list('<v>')]

# It doesn't pay off to change direction more than once while travelling between two keys
# (steps along each of the axes have to be made anyway, and every turn is an overhead).
#
# This function only finds one such path for each key pair (the other path can be found
# by reversing the original one).
def calculate_paths(pad):
    paths = {}

    for i0, j0 in mrange(pad):
        for fi, fj in mrange(pad):

            start = pad[i0][j0]
            finish = pad[fi][fj]

            if start is None or finish is None:
                continue

            di, dj = fi - i0, fj - j0

            path = ''
            if di >= 0:
                path += 'v' * di
            else:
                path += '^' * (-di)

            if dj >= 0:
                path += '>' * dj
            else:
                path += '<' * (-dj)

            # In case start equals finish, connecting path would be an empty string.
            paths[(start, finish)] = path

    return paths

cached_paths_0 = calculate_paths(PAD_0)
cached_paths_1 = calculate_paths(PAD_1)

# It can be shown, that if we take a valid controlling sequence for a directional keypad,
# and transform it up to 2 times, then the length of the final sequence is always the
# same, regardless of however we decide to move between the keys during each of the
# transformations (assuming we only consider paths which change direction at most once).
#
# In the original sequence, we have a series of blocks, each pressing a direction button
# a few times, then optionally pressing another direction button a few times, and finally
# pressing the "A" button. (The order in which we press the direction buttons is fixed).
#
# After one transformation, each such block looks like follows. We travel from button "A"
# to the first direction button, press "A" a few times, then optionally travel to another
# direction button, press "A" a few times more, and finally travel back to button "A".
# Basically, we get a longer series of similar-looking blocks, but this time the order
# of the direction buttons within each block may be arbitrary.
#
# Consider what happens with such a block after the second transformation. We have to
# travel to both direction buttons from button "A" and return back. If we needed to
# switch the order in which the direction buttons are pressed, it's always doable by
# following the same path in the opposite direction. The length of the path would be the
# same, however this time we'd also have to press different buttons (the opposite ones).
# Which explains why this rule doesn't generalize to more than 2 transformations.
def transform_sequence_1(sequence):
    current_key = 'A'

    transformed = ''

    for c in sequence:
        transformed += cached_paths_1[(current_key, c)] + 'A'
        current_key = c

    return transformed

# Check if a path is valid for the numeric keypad (doesn't hit the empty slot).
def is_valid_path_0(path, start, finish):
    if start in '0A' and finish in '147' and path[0] == '<':
        return False
    if start in '147' and finish in '0A' and path[0] == 'v':
        return False
    return True

# Since the recursion depth is 3, direction order becomes important for the numeric
# keypad. Find all the possible combinations, excluding the paths which fall outside.
def transform_sequence_0(sequence):
    transformations = []

    def iterate(path_list, current_key, i):
        if i == len(sequence):
            transformations.append('A'.join(path_list) + 'A')
            return

        path1 = cached_paths_0[current_key, sequence[i]]

        if is_valid_path_0(path1, current_key, sequence[i]):
            path_list.append(path1)
            iterate(path_list, sequence[i], i + 1)
            path_list.pop()

        path2 = ''.join(reversed(path1))

        if path2 != path1 and is_valid_path_0(path2, current_key, sequence[i]):
            path_list.append(path2)
            iterate(path_list, sequence[i], i + 1)
            path_list.pop()

    iterate([], 'A', 0)

    return transformations

def optimize(sequence):
    min_length = None

    for trans1 in transform_sequence_0(sequence):

        trans2 = transform_sequence_1(trans1)
        trans3 = transform_sequence_1(trans2)

        min_length = gmin(min_length, len(trans3))

    return min_length

total = 0

for s in lines():
    code = int(s.rstrip('A'))

    length = optimize(s)
    print(s, length, code)
    total += length * code

print(total)
