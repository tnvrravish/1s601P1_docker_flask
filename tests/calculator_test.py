"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def generate_tuple():
    """ generates tuple"""
    # This is Arrange part in AAA
    return 1, 2


def test_calculator_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    # This is Arrange part in AAA
    tuple_list = generate_tuple()
    # This is Action Part of AAA
    result = Calculator.add(tuple_list)
    # This is Assert part in AAA
    assert result == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = generate_tuple()
    result = Calculator.subtract(tuple_list)
    assert result == -3


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    tuple_list = generate_tuple()
    result = Calculator.multiply(tuple_list)
    assert result == 2


def test_calculater_division_method():
    """Testing the Calculator Division"""
    tuple_list = generate_tuple()
    result = Calculator.division(tuple_list)
    assert result == 0.5


def test_calculater_divison_by_zero_method():
    """Testing the Calculator Division by Zero"""
    tuple_list = (1, 0)
    result = Calculator.division(tuple_list)
    assert result is None


def test_calculater_divison_by_multiplevalues_method():
    """Testing the Calculator Division by Zero"""
    tuple_list = (1, 2, 3)
    result = Calculator.division(tuple_list)
    assert result is None
