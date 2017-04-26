from persons import *
from rooms import *

class Dojo(object):
    def __init__(self):
        self.all_rooms = []
        self.all_persons = []

    def create_room(self, room_type, room_name):
        initial_room_count = len(self.all_rooms)

        if not isinstance(room_type, str):
            raise TypeError("Room type must be a string")

        if not isinstance(room_name, list):
            raise TypeError("Room name must be a list")

        if room_type.lower() != 'office' and room_type.lower() != 'livingspace':
            raise ValueError("Please set a room type as office or livingspace")

        if room_type.lower() == 'office':
            for room in room_name:
                if room in self.all_rooms:
                    print("{} room already exists".format(room))
                else:
                    office = Office(room)
                    self.all_rooms.append(office)
                    print("An {} called {} has been successfully created!".format(room_type.lower(), room))

        if room_type.lower() == 'livingspace':
            for room in room_name:
                if room in self.all_rooms:
                    print("{} room already exists".format(room))
                else:
                    livingspace = LivingSpace(room)
                    self.all_rooms.append(livingspace)
                    print("An {} called {} has been successfully created!".format(room_type.lower(), room))

        new_room_count = len(self.all_rooms)
        room_increment = new_room_count - initial_room_count
        if len(room_name) == room_increment:
            return True
        return False

    def add_person(self, person_name, person_type, wants_accommodation=None):
        if person_type.upper() == 'STAFF':
            if not wants_accommodation:
                self.all_persons[person_name] = (person_type.upper(), "Blue")
                print("{} {} has been successfully added.".format(person_type.capitalize(), person_name))
                print("{} has been allocated the office Blue.".format(person_name.split(' ')[0]))
                return True
            else:
                raise ValueError("Person type 'STAFF' cannot seek accomodation")

        if person_type.upper() == 'FELLOW':
            if not wants_accommodation:
                raise ValueError("Person type 'FELLOW' must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation.upper() != 'Y' and wants_accommodation.upper() != 'N':
                raise ValueError("Person type 'FELLOW' must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation == 'N':
                self.all_persons[person_name] = (person_type.upper(), 'Blue', 'Python')
                print("{} {} has been successfully added.".format(person_type.capitalize(), person_name))
                print("{} has been allocated the office Blue.".format(person_name.split(' ')[0]))
                return True

            if wants_accommodation == 'Y':
                self.all_persons[person_name] = (person_type.upper(), "Blue", "Python")
                print("{} {} has been successfully added.".format(person_type.capitalize(), person_name))
                print("{} has been allocated the office Blue.".format(person_name.split(' ')[0]))
                print("{} has been allocated the livingspace Python,".format(person_name.split(' ')[0]))
                return True
        return False

    def print_room(self, room_name):
        if not isinstance(room_name, str):
            raise TypeError

        no_of_persons = 0
        for person in self.all_persons:
            if self.all_persons[person][1] == room_name:
                print(person,'\n')
                no_of_persons += 1

        if not no_of_persons:
            return False
        return True
