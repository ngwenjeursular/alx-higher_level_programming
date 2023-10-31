#!/usr/bin/python3
"""
This module prints a square with the character "#".
"""


def print_square(size):
    """
    This module prints a square using the character "#".

    :param size: int, size of the square

    :raises:
    - TypeError: If size is not an integer or if size is a float less than 0
    - ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")

    if size > 0:
        for i in range(size):
            [print("#", end="") for x in range(size)]
            print("")
