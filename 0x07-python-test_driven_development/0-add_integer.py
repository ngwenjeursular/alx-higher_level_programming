#!/usr/bin/python3
"""
This module defines a function that gets the sum of two integers
Usage:
- To use this function, call it with two integer or float values.
- The function will perform the addition and return an integer result.

"""


def add_integer(a, b=98):
    """Adds two integers or float

    Args:
        :param a: int or float
        :param b: int or float

    Returns:
        int

    Raises:
        TypeError: if a or b is not an integer or float
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return int(a) + int(b)
