#!/usr/bin/python3
"""Defines a Class """


class Student:
    """A class defining a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of class Student"""
        return self.__dict__
