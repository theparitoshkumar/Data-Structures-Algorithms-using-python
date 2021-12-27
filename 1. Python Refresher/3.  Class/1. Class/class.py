"""
Below is an example of a basic Person class. The class has two variables for name and age, along with three functions for initializing the class, incrementing the person’s age, and getting the person’s name.
"""

class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name