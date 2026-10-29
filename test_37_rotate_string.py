
import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string_two_positions():
    assert module.rotate_string("hello", 2) == "lohel"


def test_rotate_string_one_position():
    assert module.rotate_string("python", 1) == "npytho"


def test_rotate_string_full_rotation():
    assert module.rotate_string("abc", 3) == "abc"


def test_rotate_string_zero_positions():
    assert module.rotate_string("abc", 0) == "abc"


def test_rotate_string_empty_string():
    assert module.rotate_string("", 2) == ""
