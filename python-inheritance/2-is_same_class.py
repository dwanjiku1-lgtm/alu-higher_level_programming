#!/usr/bin/python3
"""Module that defines an is_same_class function."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class (no subclasses)."""
    return type(obj) == a_class