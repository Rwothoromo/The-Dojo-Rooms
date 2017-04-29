#-*- coding: utf-8-*-
"""
This module contains the classes used for creating a room in the Dojo.
"""


class Room(object):
    """
    This class is used for creation of rooms.
    It is the super class for Office and LivingSpace classes
    """

    def __init__(self, name):
        self.name = name
        self.occupants = []
        self.max_occupants = 0

    def check_room_availability(self):
        """check if the room has space for another occupant"""
        return len(self.occupants) < self.max_occupants

    def add_occupant(self, person_object):
        """add a person to the room"""
        if self.check_room_availability():
            self.occupants.append(person_object)
            return True
        else:
            return False

class Office(Room):
    """Office inherits from Room class"""
    def __init__(self, name):
        self.max_occupants = 6
        super(Office, self).__init__(name)

class LivingSpace(Room):
    """LivingSpace inherits from Room class"""
    def __init__(self, name):
        self.max_occupants = 4
        super(LivingSpace, self).__init__(name)
