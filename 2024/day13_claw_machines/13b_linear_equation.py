from aoc_library import *

total = 0

def solve(xa, ya, xb, yb, xprize, yprize):

    iup =  yb * xprize - xb * yprize
    jup = -ya * xprize + xa * yprize
    down = xa * yb - xb * ya

    # The funniest part would have been to optimize the degenerate case, but it seems to
    # never appear in the input file.
    #
    # In the degenerate case, both vectors point in the same direction. Depending on the
    # ratio of their lengths, one of them would be cheaper than the other in the long
    # run. So we'd want to maximize the use of the "cheaper" vector, while making sure we
    # can still hit the target.
    #
    # By dividing both x and y components of any of the two vectors by their greatest
    # common divisor, we can get an "atomic" vector, of which any of the two vectors is a
    # multiple. If the target vector is not as well a multiple of this "atomic" vector,
    # then we can never hit it (an integer solutions doesn't exist). Otherwise, the
    # problem boils down to a single equation of the form
    #
    #   `a * i + b * j = prize`
    #
    # where `a`, `b` and `prize` are integers, and `i` and `j` are the unknowns. If `a`
    # and `b` have a common divisor, and `prize` is not divisible by it as well, then
    # this equation is not solvable with integer `i` and `j`. Otherwise, we can reduce it
    # even further, to a form which is identical to the one above, but where `a` and `b`
    # are coprime.
    #
    # If our goal would be to maximize the use of vector A, we'd need to find the minimal
    # non-negative `j` such that `prize - b * j` is divisible by `a`. We could then start
    # with `prize`, and keep subtracting `b` from it until the resulting number would
    # become zero modulo `a`. Since `a` and `b` are coprime, this search is guaranteed to
    # succeed in at most `a` iterations.
    #
    # If the goal would be to maximize the use of vector B, we'd keep subtracting `a`
    # from prize, and check if the resulting number is zero modulo `b`. If neither of the
    # two original vectors is cheaper than the other (i.e. if vector A is exactly 3 times
    # longer than vector B), then the two searches would lead to identical final score.
    assert down != 0

    if iup % down != 0 or jup % down != 0:
        return 0  # No integer solution.

    i = iup // down
    j = jup // down

    assert xa * i + xb * j == xprize
    assert ya * i + yb * j == yprize

    return 3 * i + j

with open('input') as f:
    while lines := list(fsection(f)):

        xa, ya = ints(lines[0])
        xb, yb = ints(lines[1])
        xprize, yprize = ints(lines[2])

        xprize += 10000000000000
        yprize += 10000000000000

        total += solve(xa, ya, xb, yb, xprize, yprize)

print(total)
