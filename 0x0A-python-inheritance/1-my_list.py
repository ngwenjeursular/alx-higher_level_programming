#!/usr/bin/python3
"""
====================================
class MyList that inherits from list
====================================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))
