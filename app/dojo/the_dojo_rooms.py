from persons import *
from rooms import *
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from dojo_declarative_sqlalchemy import Staffs, Fellows, LivingSpaces, Offices
import random

# engine = create_engine('sqlite:///dojo_rooms.db')
"""
Bind the engine to the metadata of the Base class so that the
declaratives can be accessed through a DBSession instance
"""
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
"""
A DBSession() instance establishes all conversations with the database
and represents a "staging zone" for all the objects loaded into the
database session object. Any change made against the objects in the
session won't be persisted into the database until you call
session.commit(). If you're not happy about the changes, you can
revert all of them back to the last commit by calling
session.rollback()
"""
# session = DBSession()

# Insert a Staff into the staffs table
# new_staff = Staffs(staff_name='', office_id='')
# session.add(new_staff)

# Insert a Fellow into the fellows table
# new_fellow = Fellows(staff_name='', office_id='', livingspace_id='')
# session.add(new_fellow)

# session.commit()

class Dojo(object):
    def __init__(self):
        self.all_rooms = {}
        self.allocated_rooms = {}
        self.unallocated_rooms = {}

        self.all_persons = {}
        # self.allocated_persons = {}
        # self.unallocated_persons = {}

    # Creates rooms in the Dojo.
    def create_room(self, room_type, room_name):
        initial_room_count = len(self.all_rooms)
        room_increment = 0

        if not isinstance(room_type, str):
            raise TypeError("Room type must be a string")

        if not isinstance(room_name, list):
            raise TypeError("Room name must be a list")

        if room_type.lower() != 'office' and room_type.lower() != 'livingspace':
            raise ValueError("Please set a room type as office or livingspace")

        if room_type.lower() == 'office':
            for room in room_name:
                if room in self.all_rooms.keys():
                    print("{} room already exists".format(room))
                else:
                    office = Office(room)
                    self.all_rooms[room] = office
                    self.unallocated_rooms[room] = office

                    # Insert an Office into the offices table
                    # new_office = Offices(office_name=room)
                    # session.add(new_office)
                    # session.commit()

                    print("An {} called {} has been successfully created!".format(room_type.lower(), room))

        if room_type.lower() == 'livingspace':
            for room in room_name:
                if room in self.all_rooms.keys():
                    print("{} room already exists".format(room))
                else:
                    livingspace = LivingSpace(room)
                    self.all_rooms[room] = livingspace
                    self.unallocated_rooms[room] = livingspace

                    # Insert a LivingSpace into the livingspaces table
                    # new_livingspace = LivingSpaces(livingspace_name=room)
                    # session.add(new_livingspace)
                    # session.commit()
                    print("A {} called {} has been successfully created!".format(room_type.lower(), room))

        new_room_count = len(self.all_rooms)
        room_increment = new_room_count - initial_room_count
        return room_increment

    # Adds a person to the system and allocates the person to a random room.
    def add_person(self, person_name, person_type, wants_accommodation=None):
        if person_name in self.all_persons.keys():
            return("{} already exists".format(person_name))

        if person_type.upper() == 'STAFF':
            if not wants_accommodation:
                if not self.unallocated_rooms:
                    return "No Room space available"

                staff = Staff(person_name)
                self.allocate_office(staff)
                self.all_persons[person_name] = staff

                print("{} {} has been successfully added.".format(person_type.capitalize(), person_name))
                return True
            else:
                raise ValueError("Person type 'STAFF' cannot seek accomodation")

        if person_type.upper() == 'FELLOW':
            if not wants_accommodation:
                raise ValueError("Person type 'FELLOW' must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation.upper() != 'Y' and wants_accommodation.upper() != 'N':
                raise ValueError("Person type 'FELLOW' must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation.upper() == 'N':
                if not self.unallocated_rooms:
                    return "No Room space available"

                fellow = Fellow(person_name)
                allocated_office_name = self.allocate_office(fellow)
                self.all_persons[person_name] = fellow
                print("{} {} has been successfully added.".format(person_type.capitalize(), person_name))
                return True

            if wants_accommodation.upper() == 'Y':
                if not self.unallocated_rooms:
                    return "No Room space available"

                fellow = Fellow(person_name)
                self.allocate_office(fellow)
                self.allocate_livingspace(fellow)

                self.all_persons[person_name] = fellow
                print("{} {} has been successfully added.".format(person_type.capitalize(), person_name))
                return True
        return False

    # assign an Office to a person
    def allocate_office(self, person):
        first_name = person.person_name.split(' ')[0]
        offices_list = [room for room in self.unallocated_rooms.values() if isinstance(room, Office)]

        if not offices_list:
            return None

        random_office = random.choice(offices_list)
        random_office.add_occupant(person)

        self.allocated_rooms[random_office.room_name] = random_office
        self.all_rooms[random_office.room_name] = random_office
        self.unallocated_rooms.pop(random_office.room_name)

        print("{} has been allocated the office {}.".format(first_name, random_office.room_name))
        return True

    # assign a LivingSpace to a person
    def allocate_livingspace(self, person):
        first_name = person.person_name.split(' ')[0]
        livingspaces_list = [room for room in self.unallocated_rooms.values() if isinstance(room, LivingSpace)]

        if not livingspaces_list:
            return None

        random_livingspace = random.choice(livingspaces_list)
        random_livingspace.add_occupant(person)

        self.allocated_rooms[random_livingspace.room_name] = random_livingspace
        self.all_rooms[random_livingspace.room_name] = random_livingspace
        self.unallocated_rooms.pop(random_livingspace.room_name)

        print("{} has been allocated the livingspace {}.".format(first_name, random_livingspace.room_name))
        return True

    # check which are rooms allocated or not
    def check_room_allocations(self):
        # self.allocated_rooms = []
        # self.unallocated_rooms = []

        for room in self.all_rooms.keys():
            if self.check_room_availability():
                self.unallocated_rooms[room] = self.all_rooms[room]
            else:
                self.allocated_rooms[room] = self.all_rooms[room]
        return True

    # Prints the names of all the people in a specified room, onto the screen.
    def print_room(self, room_name):
        if not isinstance(room_name, str):
            raise TypeError

        if room_name not in self.all_rooms.keys():
            print("{} does not exist in rooms!".format(room_name))
            return False

        room_occupants = self.all_rooms[room_name].occupants
        for individual in room_occupants:
            print(individual.person_name, '\n')
        return True

    # Prints a list of allocations onto the screen.
    def print_allocations(self, filename=None):
        if not self.allocated_rooms:
            return "No Rooms allocated!"

        for room in self.allocated_rooms.keys():
            print(room.upper(), '\n', '-'*30)
            room_occupants = self.allocated_rooms[room].occupants

            for room_occupant in room_occupants:
                print("MEMBER ,".format(room_occupant.person_name.capitalize()))
            print('\n\n')
        return True

if __name__ == '__main__':
    main()
