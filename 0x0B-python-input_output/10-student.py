#!/usr/bin/python3
"""Defines a Class """


class Student:
    """A class defining a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of class Student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
