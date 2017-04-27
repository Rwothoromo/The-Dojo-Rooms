from abc import ABCMeta

class Room(object):
    __metaclass__ = ABCMeta
    max_occupants = 0

    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []

    def check_room_availability(self):
        return len(self.occupants) < self.max_occupants

    def add_occupant(self, person_object):
        if self.check_room_availability():
            self.occupants.append(person_object)
            return True
        else:
            return False

class Office(Room):
    max_occupants = 6

class LivingSpace(Room):
    max_occupants = 4
