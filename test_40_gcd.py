
import importlib

module = importlib.import_module("40_gcd")


def test_gcd_common_divisor():
    assert module.gcd(12, 18) == 6


def test_gcd_coprime_numbers():
    assert module.gcd(7, 3) == 1


def test_gcd_with_zero():
    assert module.gcd(20, 0) == 20


def test_gcd_both_zero():
    assert module.gcd(0, 0) == 0


def test_gcd_negative_number():
    assert module.gcd(-8, 12) == 4
