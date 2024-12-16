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

# ---- Two-dimensinal arrays ------------------------------------------------------------
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ALLDELTAS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# "m" means "map": a two-dimensional rectangular array of chars.
def mread(f):
    m = []
    for line in f:
        m.append([c for c in line.strip()])
    return m

def mprint(m):
    for row in m:
        print(''.join(row))

def msize(m):
    height = len(m)
    width = len(m[0])
    return (height, width)

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

def mfits(m, i, j):
    height = len(m)
    width = len(m[0])

    return 0 <= i < height and 0 <= j < width

def mfind(m, c_sequence):
    points = []
    for i, j in mrange(m):
        if m[i][j] in c_sequence:
            points.append((i, j))
    return points

def mcount(m, c_sequence):
    count = 0
    for i, j in mrange(m):
        if m[i][j] in c_sequence:
            count += 1
    return count

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

# ---- Input file parsing ---------------------------------------------------------------
# Iterate over input file lines until the nearest blank one or EOF.
def fsection(f):
    for line in f:
        if line.strip() == '':
            return
        else:
            yield line

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

# Idea stolen from here: https://blog.vero.site/post/advent-leaderboard
def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

# ---- Classes --------------------------------------------------------------------------
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

    # Python seems to be OK with duplicate class names. Field list is only added to
    # potentially simplify debugging.
    xtuple_name = 'xtuple__' + '__'.join(field_names)

    xtuple_dict = {
        '_field_names': field_names,
        '__slots__': (),  # This forbids setting custom attributes on tuple instances.
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

    # Python seems to be OK with duplicate class names. Member list is only added to
    # potentially simplify debugging.
    xclass_name = 'xclass__' + '__'.join(all_member_names)

    xclass_dict = {
        '_primary_member_names': primary_member_names,
        '_secondary_member_defaults' : secondary_member_defaults,

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

        for key, value in self._secondary_member_defaults.items():
            setattr(self, key, value)

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

# ---- Finish time statistics -----------------------------------------------------------
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

# ---- Current working directory --------------------------------------------------------
# Override IDE's habit of running Python scripts from project's root directory.
os.chdir(pathlib.Path(sys.argv[0]).parent)
