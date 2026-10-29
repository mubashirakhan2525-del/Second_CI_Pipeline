
import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating_normal():
    assert module.first_non_repeating("aabbcde") == "c"


def test_first_non_repeating_first_character():
    assert module.first_non_repeating("abc") == "a"


def test_first_non_repeating_single_character():
    assert module.first_non_repeating("x") == "x"


def test_first_non_repeating_none_found():
    assert module.first_non_repeating("aabbcc") is None


def test_first_non_repeating_empty_string():
    assert module.first_non_repeating("") is None
