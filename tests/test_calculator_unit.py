import pytest
from src.calculator import Calculator

def test_add_positive_numbers():
    c = Calculator()
    assert c.add(5, 3) == 8

def test_subtract_positive_numbers():
    c = Calculator()
    assert c.subtract(10, 4) == 6

def test_multiply_positive_numbers():
    c = Calculator()
    assert c.multiply(6, 7) == 42

def test_divide_positive_numbers():
    c = Calculator()
    assert c.divide(8, 2) == 4

def test_divide_by_zero_raises():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)

def test_add_negative_numbers():
    c = Calculator()
    assert c.add(-5, -3) == -8

def test_divide_decimal_result():
    c = Calculator()
    assert c.divide(5, 2) == 2.5

def test_multiply_large_numbers():
    c = Calculator()
    assert c.multiply(10**6, 10**6) == 10**12