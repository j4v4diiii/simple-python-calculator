# test_calculator.py

# Import the functions you want to test from your calculator.py file
from calculator import add, subtract, multiply, divide

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 2) == 3
    assert subtract(10, 20) == -10
    assert subtract(0, 0) == 0

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 4) == 8
    assert multiply(-3, 2) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(-6, 3) == -2
    # Test division by zero
    assert divide(5, 0) == "Error: Division by zero is not allowed!"
    assert divide(0, 5) == 0 # 0 divided by any non-zero number is 0