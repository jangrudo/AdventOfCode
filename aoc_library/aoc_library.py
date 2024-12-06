from collections import namedtuple
from copy import deepcopy
from sys import exit
from tqdm import tqdm

import re

import atexit
import datetime
import os
import os.path
import sys

DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ALLDELTAS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

DIGITS = '0123456789'
HEXDIGITS = '0123456789abcdef'

def mrange(m):
    height = len(m)
    width = len(m[0])

    for i in range(height):
        for j in range(width):
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

def xmin(min_value, value):
    if min_value is None:
        return value
    else:
        return min(min_value, value)

def xmax(max_value, value):
    if max_value is None:
        return value
    else:
        return max(max_value, value)

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

def ints(s):
    a = []

    i = 0
    while i < len(s):
        if (
            s[i] in DIGITS or
            s[i] in '+-' and i + 1 < len(s) and s[i + 1] in DIGITS
        ):
            j = i + 1
            while j < len(s) and s[j] in DIGITS:
                j += 1
            a.append(int(s[i : j]))
            i = j
            continue
        i += 1

    return a

aoc_library_now = datetime.datetime.now()

def print_finish_time():
    atexit.register(
        lambda: print('Finished in', datetime.datetime.now() - aoc_library_now)
    )

# Override IDE's habit of running Python scripts from project's root directory.
os.chdir(os.path.dirname(sys.argv[0]))
