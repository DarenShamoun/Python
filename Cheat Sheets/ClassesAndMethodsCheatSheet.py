#Classes and Methods Cheat Sheet

#Defining classes and methods

"""
class ClassName:
         def method_name(self, other_parameters):
             "body_of_method
"""


# Classes and Instances
# Classes define the behavior of all instances of a specific class.
# Each variable of a specific class is an instance or object.
# Objects can have attributes, which store information about the object.
# You can make objects do work by calling their methods.
# The first parameter of the methods (self) represents the current instance.
# Methods are just like functions, but they can only be used through a class.


#Special methods
#Special methods start and end with __.
#Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.


#Documenting classes, methods and functions
#You can add documentation to classes, methods, and functions by using docstrings right after the definition. Like this:


"""
class ClassName:
    ""Documentation for the class.""
    def method_name(self, other_parameters):
        ""Documentation for the method.""
        body_of_method

def function_name(parameters):
    ""Documentation for the function.""
    body_of_function
"""