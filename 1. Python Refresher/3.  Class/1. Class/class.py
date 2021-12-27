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

"""
Let’s look at an example for how to create an instance of the Person class using the class template above. We can then access that Person’s name:
"""

bob = Person('Bob', 32)
print(bob.getName())
# prints Bob

"""
Currently, we have one function for getting the class’s variable. This is called an Accessor. The other function that the class has is actually modifying one of the class’ variables, and that is called a Mutator. We can make our Person older by calling birthday()
"""

