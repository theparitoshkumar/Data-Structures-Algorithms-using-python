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

bob.birthday()
print(bob.person_age)
# prints 33

"""
The birthday function call successfully increments the age of our Person. Also note that we can directly get the age of bob without using a function call. This is because the Person class variables are defined as public, so we can directly access them without a function call. If instead we wanted the Person’s age variable to be private to the class, in Python 3 we could put double underscores in front of the variable: __person_age. Then we would have to use a function call in order to retrieve it.
"""