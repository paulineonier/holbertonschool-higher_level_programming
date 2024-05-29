#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject to a file.

        Parameters:
        filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing the object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject from a file.

        Parameters:
        filename (str): The name of the file to load the serialized object from.

        Returns:
        CustomObject: The deserialized instance of CustomObject or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except Exception as e:
            print(f"An error occurred while deserializing the object: {e}")
            return None
