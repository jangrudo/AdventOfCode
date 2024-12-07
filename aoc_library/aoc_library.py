from collections import namedtuple
from copy import deepcopy
from functools import cmp_to_key
from sys import exit
from tqdm import tqdm

import re
import string

import datetime
import os
import pathlib
import sys

DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ALLDELTAS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

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

# "g" means "generic". Chosen to prevent collisions with common variable names.
def gmin(min_value, value):
    if min_value is None:
        return value
    else:
        return min(min_value, value)

def gmax(max_value, value):
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

# Idea stolen from here: https://blog.vero.site/post/advent-leaderboard
def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

aoc_library_now = datetime.datetime.now()

def print_finish_time():
    print('Finished in', datetime.datetime.now() - aoc_library_now)

# Override IDE's habit of running Python scripts from project's root directory.
os.chdir(pathlib.Path(sys.argv[0]).parent)
