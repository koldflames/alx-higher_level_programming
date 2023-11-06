#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """ this class Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
