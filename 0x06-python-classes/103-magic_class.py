#!/usr/bin/python3
""" square module """
import math


"""
Defines a MagicClass class that represents a circle.

Attributes:
    radius (int or float): The radius of the circle.

Methods:
    __init__(self, radius=0): Initializes a new MagicClass instance.
    area(self): Returns the area of the circle.
    circumference(self): Returns the circumference of the circle.
"""


class MagicClass:
    """
    Represents a circle.

    Args:
        radius: The radius of the circle. Defaults to 0.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius: The radius of the circle. Defaults to 0.

        Raises:
            TypeError if radius is not an int or float.
        """

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """
    Returns the area of the circle.

    Returns:
        float: The area of the circle.
    """

    def area(self):
        return self.__radius**2 * math.pi

    """
    Returns the circumference of the circle.

    Returns:
        float: The circumference of the circle.
    """

    def circumference(self):
        return 2 * math.pi * self.__radius
