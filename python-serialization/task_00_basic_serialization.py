#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the Python dictionary to a JSON file.

    Parameters:
    data (dict): The Python dictionary to be serialized.
    filename (str): The name of the output JSON file. If the file exists, it will be replaced.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def load_and_deserialize(filename):
    """
    Load and deserialize the JSON file to a Python dictionary.

    Parameters:
    filename (str): The name of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")
        return None

