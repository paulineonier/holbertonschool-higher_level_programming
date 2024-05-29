#!/usr/bin/python3
from abc import ABC, abstractmethod

# Define the abstract base class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Define the Dog subclass
class Dog(Animal):

    def sound(self):
        return "Bark"

# Define the Cat subclass
class Cat(Animal):

    def sound(self):
        return "Meow"

# Example usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(f"Dog: {dog.sound()}")
    print(f"Cat: {cat.sound()}")

