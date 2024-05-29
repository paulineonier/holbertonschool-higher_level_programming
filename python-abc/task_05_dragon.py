#!/usr/bin/python3
# Define the SwimMixin class
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Define the FlyMixin class
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Define the Dragon class inheriting from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
