import pytest

def add(x, y):
    return x + y

def test_addition():
    assert add(1, 2) == 3

def test_subtraction():
    assert add(5, 3) == 2

if __name__ == "__main__":
    pytest.main()
