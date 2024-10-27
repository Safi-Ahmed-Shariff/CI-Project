# test_main.py
import pytest
from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def test_add_numbers():
    assert add_numbers(5, 3) == 8
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(3, 5) == -2
    assert subtract_numbers(0, 0) == 0

def test_multiply_numbers():
    assert multiply_numbers(5, 3) == 15
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-1, -1) == 1

def test_divide_numbers():
    assert divide_numbers(6, 3) == 2
    assert divide_numbers(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide_numbers(5, 0)

if __name__ == "__main__":
    pytest.main()
