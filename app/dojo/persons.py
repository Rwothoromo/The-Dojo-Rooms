#-*- coding: utf-8-*-
"""
This module contains the classes used for creating a person in the Dojo.
"""


class Person(object):
    """
    This class is used for creation of people.
    It is the super class for Staff and Fellow classes
    """

    def __init__(self, name):
        self.name = name

class Staff(Person):
    """Staff inherits from Person class"""
    def __init__(self, name):
        self.type = "STAFF"
        super(Staff, self).__init__(name)

class Fellow(Person):
    """Fellow inherits from Person class"""
    def __init__(self, name):
        self.type = "FELLOW"
        super(Fellow, self).__init__(name)
