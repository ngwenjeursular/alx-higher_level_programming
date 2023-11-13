#!/usr/bin/python3
"""" This module defines the base class Base """
import json
import csv
import turtle


class Base:
    """ The Base class
    This class will be the “base” of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): 'id' of the Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dicts to convert to JSON

        Returns:
            str: The JSON string representation of the list of dictionaries.

        Notes:
            If list_dictionaries is None or empty, it returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string repn of a list of objects to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Notes:
            If list_objs is None, it saves an empty list.
            The filename is based on the class name: <Class name>.json.
            The method overwrites the file if it already exists.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representing a list of dicts

        Returns:
            list: The list of dictionaries represented by the JSON string.

        Notes:
            If json_string is None or empty, it returns an empty list.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance and set its attr based on the provided dictionary

        Args:
            **dictionary: A dict containing the attr and values 4 the instance

        Returns:
            object: instance of the class with attr set based on the dict

        Notes:
            a class method, so it returns an instance of the calling class.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file."""

        filename = cls.__name__ + ".json"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Returns:
            If the file does not exist = an empty list.
            Otherwise = a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the Turtle graphics module.
        Args:
            list_rectangles (list): list of Rectangle objects to draw.
            list_squares (list): list of Square objects to draw."""
        turtle.speed(1)
        turtle.bgcolor("white")

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.pencolor("blue")
            turtle.fillcolor("lightblue")
            turtle.begin_fill()

            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)

            turtle.end_fill()

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.pencolor("red")
            turtle.fillcolor("lightcoral")
            turtle.begin_fill()

            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

            turtle.end_fill()

        turtle.done()
