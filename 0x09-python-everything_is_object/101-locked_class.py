#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Locked class allowing only an attribute named first_name"""
    __slots__ = "first_name",
