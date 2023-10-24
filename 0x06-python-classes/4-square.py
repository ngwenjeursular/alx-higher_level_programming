#!/usr/bin/python3
"""Define a class Square to represent a square."""


class Square:
    """A class to represent a square."""

    def __init__(self, size: int = 0) -> None:
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self) -> int:
        """Get/set the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """Set the current size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """Return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
