
import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent_normal():
    assert module.most_frequent([1, 2, 2, 3]) == 2


def test_most_frequent_tie():
    assert module.most_frequent([4, 4, 5, 5]) == 4


def test_most_frequent_single_element():
    assert module.most_frequent([7]) == 7


def test_most_frequent_repeated_element():
    assert module.most_frequent([3, 3, 3, 2, 2]) == 3


def test_most_frequent_empty_list():
    assert module.most_frequent([]) is None
