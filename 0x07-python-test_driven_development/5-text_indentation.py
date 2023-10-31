#!/usr/bin/python3
"""
This module defines a function for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after:
    each of the characters '.', '?' and ':'.

    :param text: str, The input text.

    :raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ".?:":
            print("\n\n", end="")
