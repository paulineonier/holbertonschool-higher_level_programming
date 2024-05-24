#!/usr/bin/python3
"""
Module 4-inherits_from.py

Contains method inherits_from

Returns True if object is instance of class that it inherits

"""


def inherits_from(obj, a_class):
    """
    use type() to get specific class
    use isinstance() to get class and any parent classes too
    use issubclass() to get what object is a subclass of

    Return:
        True if obj is instance of class that it inherits from or is subcls of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
