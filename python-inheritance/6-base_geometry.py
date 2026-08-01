#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an exception since area() is not implemented here."""
        raise Exception("area() is not implemented")
