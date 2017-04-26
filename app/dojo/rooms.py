class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name

class Office(Room):
    def __init__(self, room_name):
        self.max_occupants = 6

class LivingSpace(Room):
    def __init__(self, room_name):
        self.max_occupants = 4
