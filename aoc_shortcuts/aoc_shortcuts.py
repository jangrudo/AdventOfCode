from collections import *
from sortedcontainers import *
from tqdm import tqdm

from copy import deepcopy
from functools import cmp_to_key
from sys import exit

import math
import re
import string

import atexit
import datetime
import operator
import os
import pathlib
import sys

# ---- Parsing --------------------------------------------------------------------------
aoc_library_file = None

def open_input(input_file_path):
    global aoc_library_file

    if aoc_library_file is not None:
        aoc_library_file.close()

    aoc_library_file = open(input_file_path)

# Read lines from the input file, newlines stripped, until the nearest blank line or EOF.
def lines():
    assert aoc_library_file is not None

    line_strings_list = []

    for line in aoc_library_file:
        s = line.rstrip('\n')
        if s == '':
            break

        line_strings_list.append(s)

    return line_strings_list

def popfront(a):
    x = a[0]
    del a[0]
    return x

# Idea stolen from here: https://blog.vero.site/post/advent-leaderboard
def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

# This one has never been used so far.
def substr(s, substring_left, substring_right):
    if substring_left is None:
        start = 0
    else:
        start = s.find(substring_left)
        assert start != -1
        start += len(substring_left)

    if substring_right is None:
        end = len(s)
    else:
        end = s.find(substring_right, start)
        assert end != -1

    return s[start : end]

# ---- Maps -----------------------------------------------------------------------------
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ALLDELTAS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

STEP = {'^' : (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

TURN_LEFT  = {'^' : '<', 'v': '>', '<': 'v', '>': '^'}
TURN_RIGHT = {'^' : '>', 'v': '<', '<': '^', '>': 'v'}
TURN_BACK  = {'^' : 'v', 'v': '^', '<': '>', '>': '<'}

# "m" means "map": a two-dimensional rectangular array of chars.
def mread():
    m = []
    for s in lines():
        m.append(list(s))
    return m

def mprint(m):
    for row in m:
        print(''.join(row))

def msize(m):
    height = len(m)
    width = len(m[0])
    return (height, width)

def mcreate(size, item_value):
    height, width = size

    # Allow to fill the maps with empty lists and similar structures. For primitive data
    # types, shave the overhead off by not running the deepcopy().

    if _is_immutable_type(item_value):
        return [[item_value for j in range(width)] for i in range(height)]
    else:
        return [[deepcopy(item_value) for j in range(width)] for i in range(height)]

def mrange(m):
    return _MrangeIterator(m)

# This wrapper allows to iterate over maps with tqdm (luckily, it only needs __len__).
class _MrangeIterator:
    def __init__(self, m):
        self.m = m
        self.height = len(m)
        self.width = len(m[0])

    def __len__(self):
        return self.height * self.width

    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield (i, j)

def deltas(m, i, j):
    height = len(m)
    width = len(m[0])

    for di, dj in DELTAS:
        ni = i + di
        nj = j + dj
        if 0 <= ni < height and 0 <= nj < width:
            yield (ni, nj)

def alldeltas(m, i, j):
    height = len(m)
    width = len(m[0])

    for di, dj in ALLDELTAS:
        ni = i + di
        nj = j + dj
        if 0 <= ni < height and 0 <= nj < width:
            yield (ni, nj)

def mmove(i, j, direction):
    di, dj = STEP[direction]
    return i + di, j + dj

def mfits(m, i, j):
    height = len(m)
    width = len(m[0])

    return 0 <= i < height and 0 <= j < width

def mfind(m, c_sequence):
    return [(i, j) for i, j in mrange(m) if m[i][j] in c_sequence]

def mcount(m, c_sequence):
    return sum(1 for i, j in mrange(m) if m[i][j] in c_sequence)

# ---- Structures -----------------------------------------------------------------------
# Similar to collections.namedtuple, but doesn't require to type the class name twice.
#
# The sole argument should be a space-separated list of field names.
def xtuple(field_names_str):
    if not isinstance(field_names_str, str):
        raise TypeError(f'{field_names_str!r} identifier list must be a string')

    field_names = tuple(field_names_str.split())

    for name in field_names:
        if not name.isidentifier():
            raise ValueError(f'{name!r} is not an identifier')

    # Duplicate class names are OK. Field list is only added to simplify debugging.
    xtuple_name = 'xtuple__' + '__'.join(field_names)

    xtuple_dict = {
        '_field_names': field_names,
        '__slots__': (),  # This forbids setting custom attributes on xtuple instances.
    }

    for i, name in enumerate(field_names):
        xtuple_dict[name] = property(operator.itemgetter(i))  # Read-only accessors.

    return type(xtuple_name, (_XtupleBase,), xtuple_dict)

# Similar to xtuple, but creates a mutable class. The constructor of the returned class
# takes a few mandatory positional-only arguments (similar to xtuple), and optionally
# default-initializes a few extra members. This is equivalent to defining the class
# manually, but saves time on typing in the boilerplate (with a bit of overhead).
#
# The returned class can be used as is, or subclassed to add missing functionality.
#
# First argument should be a space-separated list of member names, corresponding to the
# constructor's argument list. Default values for the rest are passed as key=value pairs.
def xclass(primary_member_names_str, **secondary_member_defaults):
    if not isinstance(primary_member_names_str, str):
        raise TypeError(
            f'{primary_member_names_str!r} identifier list must be a string'
        )

    primary_member_names = tuple(primary_member_names_str.split())

    all_member_names = primary_member_names + tuple(secondary_member_defaults.keys())

    for name in all_member_names:
        if not name.isidentifier():
            raise ValueError(f'{name!r} is not an identifier')

    # Allow to initialize members with empty lists and similar structures. This requires
    # deepcopy() to properly copy the values, which adds a bit of overhead even for
    # primitive data types which don't need it. Solve this by pre-computing in advance
    # which members are guaranteed to be fine without the deepcopy().

    secondary_immutable_defaults = {}
    secondary_deepcopy_defaults = {}

    for key, value in secondary_member_defaults.items():
        if _is_immutable_type(value):
            secondary_immutable_defaults[key] = value
        else:
            secondary_deepcopy_defaults[key] = deepcopy(value)

    # Duplicate class names are OK. Member list is only added to simplify debugging.
    xclass_name = 'xclass__' + '__'.join(all_member_names)

    xclass_dict = {
        '_primary_member_names': primary_member_names,
        '_secondary_immutable_defaults' : secondary_immutable_defaults,
        '_secondary_deepcopy_defaults' : secondary_deepcopy_defaults,

        # This forbids adding more attributes to the class (unless it's subclassed), and
        # also improves performance a little bit.
        '__slots__': all_member_names,
    }

    return type(xclass_name, (_XclassBase,), xclass_dict)

class _XtupleBase(tuple):
    __slots__ = ()  # To properly clear the slots, we also need to update base classes.

    def __new__(cls, *arguments):
        # Argument checking adds an overhead, but is crucial for early error detection.
        if len(arguments) != len(cls._field_names):
            raise ValueError(
                f'{len(cls._field_names)} tuple arguments expected '
                f'({len(arguments)} given)'
            )

        return tuple.__new__(cls, tuple(arguments))

    # str() falls back to repr(), and repr() is still needed for printing lists etc.
    def __repr__(self):
        # The format is the same as in namedtuple, but without the class name.
        return ('({})'.format(', '.join(
            _get_member_string(self, name) for name in self._field_names
        )))

class _XclassBase():
    __slots__ = ()  # To properly set the slots, we also need to update base classes.

    def __init__(self, *arguments):
        if len(arguments) != len(self._primary_member_names):
            raise ValueError(
                f'{len(self._primary_member_names)} constructor arguments expected '
                f'({len(arguments)} given)'
            )

        for i, value in enumerate(arguments):
            setattr(self, self._primary_member_names[i], value)

        for key, value in self._secondary_immutable_defaults.items():
            setattr(self, key, value)

        for key, value in self._secondary_deepcopy_defaults.items():
            setattr(self, key, deepcopy(value))

    def __repr__(self):
        return ('({})'.format(', '.join(
            _get_member_string(self, name) for name in self.__slots__
        )))

    # Comparison is added for rapid prototyping, but it may be twice slower than a manual
    # implementation without getattr(), and 10 times slower than xtuple.
    def __lt__(self, other):
        for name in self._primary_member_names:
            self_value = getattr(self, name)
            other_value = getattr(other, name)

            if self_value != other_value:
                return self_value < other_value

        return False

    def __eq__(self, other):
        for name in self._primary_member_names:
            self_value = getattr(self, name)
            other_value = getattr(other, name)

            if self_value != other_value:
                return False

        return True

def _get_member_string(obj, name):
    value = getattr(obj, name)

    # This is needed to prevent recursion in linked structures.
    if isinstance(value, _XclassBase):
        value_string = '<ref>'
    elif isinstance(value, _XtupleBase):
        value_string = '<tuple>'
    else:
        value_string = str(value)

    return f'{name}={value_string}'

# Return False if the type of obj might be an immutable one.
def _is_immutable_type(obj):
    if obj is None or any(isinstance(obj, t) for t in (bool, int, float, str, bytes)):
        return True

    if any(isinstance(obj, t) for t in (tuple, frozenset)):
        # This may recurse, but it won't get into class instances, and it's not easy (if
        # possible at all) to make a loop with immutable containers. Also, this function
        # isn't expected to be called in tight loops, so this extra work should be fine.
        return all(_is_immutable_type(item) for item in obj)

    return False

# ---- Iterators ------------------------------------------------------------------------
# "u" means "unlimited".
def urange(start=None, step=1):
    k = 0 if start is None else start
    while True:
        yield k
        k += step

# ---- Minimum and maximum --------------------------------------------------------------
# "g" means "generic". Chosen to prevent collisions with common variable names.
def gmin(min_value, value):
    if min_value is None or value < min_value:
        return value
    else:
        return min_value

def gmax(max_value, value):
    if max_value is None or value > max_value:
        return value
    else:
        return max_value

def argmin(min_value, best_parameter, value, parameter):
    if min_value is None or value < min_value:
        return value, parameter
    else:
        return min_value, best_parameter

def argmax(max_value, best_parameter, value, parameter):
    if max_value is None or value > max_value:
        return value, parameter
    else:
        return max_value, best_parameter

# ---- Timing ---------------------------------------------------------------------------
aoc_library_now = datetime.datetime.now()

def print_finish_time():
    print('Finished in', datetime.datetime.now() - aoc_library_now)

# Always print finish time statistics, unless the script terminates with exception.
atexit.register(print_finish_time)

_default_excepthook = sys.excepthook

def _aoc_library_excepthook(*args):
    atexit.unregister(print_finish_time)  # Unregister the print handler upon exception.
    _default_excepthook(*args)            # Print the traceback as usual.

sys.excepthook = _aoc_library_excepthook

# ---- Startup --------------------------------------------------------------------------
# Override IDE's habit of running Python scripts from project's root directory.
os.chdir(pathlib.Path(sys.argv[0]).parent)
