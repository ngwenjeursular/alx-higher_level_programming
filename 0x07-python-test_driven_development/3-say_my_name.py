#!/usr/bin/python3
"""
This module defines a function for printing the name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name><last name>."

    :param first_name: str, first name
    :param last_name: str, optional, last name. Default: empty string

    :raises:
    - TypeError: if first_name or last_name is not a string
    """
    err = "first_name must be a string"

    if not first_name and not last_name:
        raise TypeError(err)

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
