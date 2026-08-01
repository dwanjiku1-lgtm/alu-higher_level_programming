#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.

    Returns False if obj is an instance of a_class itself (exact match),
    only True if obj's class is a subclass (direct or indirect) of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
