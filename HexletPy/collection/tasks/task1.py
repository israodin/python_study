# coding=utf-8


def task(seq1, seq2):
    """
    Функция принимает две последовательности (списки, словари, множества).
    Вернуть отсортированный список элементов, каждый из которых принадлежит обеим последовательностям.

    Пример:
    >>> task([1, 3, 2], (2, 3, 4))
    [2, 3]
    """
    # BEGIN (write your solution here)
    seq1,seq2 =  set(seq1),set(seq2)
    list_res = list(seq1 & seq2)
    res = sorted(list_res)
    return res
    # END