#!/usr/bin/python3
"""Define a class Square to represent a square."""


class Square:
    """A class to represent a square."""

    def __init__(self, size: int = 0) -> None:
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """Return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
