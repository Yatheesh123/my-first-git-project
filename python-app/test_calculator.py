# test_calculator.py

from calculator import add, subtract, multiply, divide

def run_tests():
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 5) == 15
    assert divide(8, 2) == 4
    assert divide(10, 0) == "Cannot divide by zero!"
    print("✅ All tests passed!")

run_tests()
