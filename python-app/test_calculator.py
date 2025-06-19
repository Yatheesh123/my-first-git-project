# test_calculator.py

from calculator import add, subtract, multiply, divide

def test():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Cannot divide by zero!"
    print("✅ All tests passed!")

test()
