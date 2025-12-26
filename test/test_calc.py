# tests/test_calculator.py
import pytest
from app.calculator import add, divide, sub

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_sub():
    assert sub(100, 1) == 99
