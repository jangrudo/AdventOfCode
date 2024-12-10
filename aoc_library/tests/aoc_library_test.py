from aoc_library import *

class TestGminmax:
    def calculate_minmax(self, a):
        min_value = None
        max_value = None
        for x in a:
            min_value = gmin(min_value, x)
            max_value = gmax(max_value, x)
        return (min_value, max_value)

    def test_many(self):
        assert self.calculate_minmax([1, 2, -3, 5, 0, 2]) == (-3, 5)
    def test_sorted(self):
        assert self.calculate_minmax([1, 2, 3, 4, 5]) == (1, 5)
    def test_duplicate(self):
        assert self.calculate_minmax([0, 0, 0]) == (0, 0)
    def test_single(self):
        assert self.calculate_minmax([10]) == (10, 10)
    def test_none(self):
        assert self.calculate_minmax([]) == (None, None)

class TestArgminmax:
    def calculate_argminmax(self, a):
        min_value = None
        max_value = None
        argmin_i = None
        argmax_i = None

        for i in range(len(a)):
            min_value, argmin_i = argmin(min_value, argmin_i, a[i], i)
            max_value, argmax_i = argmax(max_value, argmax_i, a[i], i)

        return (min_value, max_value, argmin_i, argmax_i)

    def test_many(self):
        assert self.calculate_argminmax([0, 6, -2, -4, 2]) == (-4, 6, 3, 1)
    def test_sorted(self):
        assert self.calculate_argminmax([8, 7, 4, 2, 1]) == (1, 8, 4, 0)
    def test_duplicate(self):
        assert self.calculate_argminmax([1, 2, 2, 2, 1]) == (1, 2, 0, 1)
    def test_single(self):
        assert self.calculate_argminmax([0]) == (0, 0, 0, 0)
    def test_none(self):
        assert self.calculate_argminmax([]) == (None, None, None, None)

class TestInts():
    def test_list(self):
        assert ints('199, 0, -20, -0, +33') == [199, 0, -20, 0, 33]
    def test_mixed(self):
        assert ints('1: [0 0 10]; 8|9') == [1, 0, 0, 10, 8, 9]

    def test_text(self):
        assert ints('Player #1 starts with 100% health and experience 8') == [1, 100, 8]

    def test_no_whitespace(self):
        assert ints('2to3') == [2, 3]
    def test_hex(self):
        assert ints('0xff10') == [0, 10]

    def test_adjacent_minus(self):
        assert ints('-1-1-1-1') == [-1, -1, -1, -1]
    def test_adjacent_plus(self):
        assert ints('+1+1+1+1') == [1, 1, 1, 1]
    def test_plus_minus(self):
        assert ints('+-2 -+3') == [-2, 3]

    def test_long_integer(self):
        assert ints('12345678901234567890') == [12345678901234567890]
    def test_long_negative_integer(self):
        assert ints('-12345678901234567890') == [-12345678901234567890]

    def test_empty_text(self):
        assert ints('text') == []
    def test_empty_string(self):
        assert ints('') == []

class TestSubstr:
    def test_nested_list(self):
        assert ints(substr('rule 5: [1, 2, 3] -> action 8', '[', ']')) == [1, 2, 3]

    def test_at_boundaries(self):
        assert substr('<<test>>', '<<', '>>') == 'test'
    def test_same_substrings(self):
        assert substr('!!test!!', '!!', '!!') == 'test'
    def test_single_char_substrings(self):
        assert substr('!test!', '!', '!') == 'test'

    def test_open_start(self):
        assert ints(substr('10, 20 -> 88, 77', None, '->')) == [10, 20]
    def test_open_end(self):
        assert ints(substr('10, 20 -> 88, 77', '->', None)) == [88, 77]
    def test_open_both(self):
        assert substr('', None, None) == ''
