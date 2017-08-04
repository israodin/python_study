# coding=utf-8

from task1 import task


def _test_task(seq1, seq2, expected):
    assert task(seq1, seq2) == expected


def test_ok():
    _test_task([1, 2, 3], [2, 3, 4], [2, 3])


def test_list_tuple():
    _test_task(['foo', True, 42], (True, 42, 'baz'), [True, 42])


def test_tuple_set():
    _test_task((99, 22, 11, 44), {'test', 99, 22.0}, [22.0, 99])


def test_empty():
    _test_task({1, 2, 3}, {6, 5, 4}, [])
