#!/usr/bin/python3
"""Module that defines the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the length of each side, must be > 0.
        """
        super().__init__(size, size)
