from calculator_tool import Calculator

def test_addition():
    calc = Calculator()
    result = calc.add(2, 4)
    assert result == 6

def test_subtraction():
    calc = Calculator()
    result = calc.subtract(10, 4)
    assert result == 6

def test_division():
    calc = Calculator()
    result = calc.divide(8, 2)
    assert result == 4

def test_multiplication():
    calc = Calculator()
    result = calc.multiply(2, 4)
    assert result == 8
