class Room(object):
    """
    This class is used for creation of rooms.
    It is the super class for Office and LivingSpace classes
    """
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

# Office inherits from Room class
class Office(Room):
    def __init__(self, room_name):
        self.max_occupants = 6
        super(Office, self).__init__(room_name)

# LivingSpace inherits from Room class
class LivingSpace(Room):
    def __init__(self, room_name):
        self.max_occupants = 4
        super(LivingSpace, self).__init__(room_name)
