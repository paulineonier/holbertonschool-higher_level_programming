#!/usr/bin/python3
"""A module to add two numbers

Do an addition between two numbers,
these numbers can be integers or floats.

"""


def add_integer(a, b=98):
    """Adds two numbers

    Returns:
        int: The result of the addition.

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    """Cast the data type of num parameter
    Convert a float number to a integer number
    Returns: int: The number casted to integer.

    """
    if type(num) is float:
        num = int(num)
        return num

    return num
