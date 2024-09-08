"""This is tests for calculator"""
import pytest
from src.finance.calculator import is_even, is_prime

def test_is_even_simple():
    """test case for is_even function
    """
    assert is_even(4) is True
    assert is_even(7) is False

def test_is_prime():
    """simple test case for is_prime
    """
    assert is_prime(7) is True
    assert is_prime(8) is False
    with pytest.raises(ValueError, match = "Input should not be less than 2."):
        is_prime(0)

