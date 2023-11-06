#!/usr/bin/python3
"""
This is a lookup module that returns the list of 
available attributes and methods of an object.
"""

def lookup(obj):
    """lookup method
    Returns: a list of available attributes and methods of an object"""
    return dir(obj)
