
import importlib

module = importlib.import_module("34_check_sorted")


def test_sorted_array():
    assert module.is_sorted([1, 2, 3, 4]) is True


def test_unsorted_array():
    assert module.is_sorted([1, 3, 2, 4]) is False


def test_equal_elements():
    assert module.is_sorted([5, 5, 6, 6]) is True


def test_single_element():
    assert module.is_sorted([7]) is True


def test_empty_array():
    assert module.is_sorted([]) is True
