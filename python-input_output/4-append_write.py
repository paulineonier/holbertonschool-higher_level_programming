#!/usr/bin/python3
import json

def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
    my_str (str): A JSON string representing a Python object.

    Returns:
    object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
