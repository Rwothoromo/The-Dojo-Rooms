class Room(object):
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
    def __init__(self, room_name):
        self.max_occupants = 6
        self.occupants = []
        self.room_name = room_name
        super(Office, self).__init__(room_name)

class LivingSpace(Room):
    def __init__(self, room_name):
        self.max_occupants = 4
        self.occupants = []
        self.room_name = room_name
        super(LivingSpace, self).__init__(room_name)
