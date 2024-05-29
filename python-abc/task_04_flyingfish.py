#!/usr/bin/python3
# Define the Fish class
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

# Define the Bird class
class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

# Define the FlyingFish class inheriting from Fish and Bird
class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
