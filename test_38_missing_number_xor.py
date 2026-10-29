
import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_number_middle():
    assert module.missing_number([3, 0, 1]) == 2


def test_missing_number_last():
    assert module.missing_number([0, 1]) == 2


def test_missing_number_large_list():
    assert module.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_missing_number_zero():
    assert module.missing_number([1, 2, 3]) == 0


def test_missing_number_empty_list():
    assert module.missing_number([]) == 0
