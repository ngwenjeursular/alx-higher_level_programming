#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): An identifier for the square.

        Raises:
            TypeError: If size, x, or y is not an integer.
            ValueError: If size, x, or y is not within the expected range.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square.

        Args:
            *args: Non-keyworded arguments in the order: id, size, x, y.
            **kwargs: Keyworded arguments to update specific attributes.

        Note:
            If *args is present and not empty, **kwargs is skipped.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the attributes of the Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: A string in the format "[Square] (<id>) <x>/<y> - <size>".
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
