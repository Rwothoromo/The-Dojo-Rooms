#-*- coding: utf-8-*-
"""
This module contains the classes used for creating a person in the Dojo.
"""
import random
from app.dojo.persons import Fellow, Staff
from app.dojo.rooms import Office, LivingSpace
# from app.dojo.dojo_declarative_sqlalchemy import DojoState


class Dojo(object):
    """
    This class is used for running functions on the Dojo.
    """

    def __init__(self):
        self.all_rooms = {}
        self.allocated_rooms = []
        self.unallocated_rooms = []
        self.all_persons = {}
        self.allocated_persons = []

    def create_room(self, room_type, room_name):
        """Creates rooms in the Dojo."""

        initial_room_count = len(self.all_rooms)
        room_increment = 0

        if not isinstance(room_type, str):
            raise AttributeError("Room type must be a string")

        if not isinstance(room_name, list):
            raise AttributeError("Room name must be a list")

        if room_type.lower() != 'office' and room_type.lower() != 'livingspace':
            raise ValueError("Please set a room type as office or livingspace")

        if room_type.lower() == 'office':
            for room in room_name:
                if room in self.all_rooms.keys():
                    print("{} room already exists".format(room))
                else:
                    office = Office(room)

                    # append room objects to room lists
                    self.all_rooms[room] = office
                    print("An {} called {} has been successfully created!" \
                            .format(room_type.lower(), room))

        if room_type.lower() == 'livingspace':
            for room in room_name:
                if room in self.all_rooms.keys():
                    print("{} room already exists".format(room))
                else:
                    livingspace = LivingSpace(room)

                    # append room objects to room lists
                    self.all_rooms[room] = livingspace
                    print("A {} called {} has been successfully created!" \
                            .format(room_type.lower(), room))

        new_room_count = len(self.all_rooms)
        room_increment = new_room_count - initial_room_count
        return room_increment

    def add_person(self, person_name, person_type, wants_accommodation=None):
        """Adds a person to the Dojo and assigns them a random room."""

        if not isinstance(person_name, str):
            raise AttributeError("Person name must be a string")

        if not isinstance(person_type, str):
            raise AttributeError("Person type must be a string")

        if person_name in self.all_persons.keys():
            raise ValueError("{} already exists".format(person_name))

        if person_type.upper() == 'STAFF':
            person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
            if not wants_accommodation:
                staff = Staff(person_name)

                # append person object to all_persons list
                self.all_persons[person_name] = staff
                print("{} {} has been successfully added.".format(staff.type, staff.name))
                self.allocate_office(staff)
                return True
            else:
                raise AttributeError("Staff cannot seek accomodation")

        if person_type.upper() == 'FELLOW':
            if not wants_accommodation:
                raise ValueError("Fellow must indicate 'Y' or 'N' for accomodation")

            if not isinstance(wants_accommodation, str):
                raise AttributeError("Fellow must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation.upper() != 'Y' and wants_accommodation.upper() != 'N':
                raise ValueError("Fellow must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation.upper() == 'N':
                person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
                fellow = Fellow(person_name)

                # append person object to all_persons list
                self.all_persons[person_name] = fellow
                print("{} {} has been successfully added.".format(fellow.type, fellow.name))
                self.allocate_office(fellow)
                return True

            if wants_accommodation.upper() == 'Y':
                person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
                fellow = Fellow(person_name)

                # append person object to all_persons list
                self.all_persons[person_name] = fellow
                print("{} {} has been successfully added.".format(fellow.type, fellow.name))
                self.allocate_office(fellow)
                self.allocate_livingspace(fellow)
                return True

    def allocate_office(self, person):
        """assign an office to a person"""

        first_name = person.name.split(' ')[0]
        offices_available = [room for room in self.all_rooms.values() \
                            if isinstance(room, Office) and room.check_room_availability()]

        if not offices_available:
            print("No Office space available")
            return False
        else:
            # select a random room object
            random_office = random.choice(offices_available)

            # assign a person a Dojo room
            random_office.add_occupant(person)

            # append person name to list of persons allocated rooms
            self.allocated_persons.append(person.name)

            # append office name to dictionary of rooms
            self.all_rooms[random_office.name] = random_office

            # append person name to dictionary of persons in the Dojo
            self.all_persons[person.name] = person
            print("{} has been allocated the office {}.".format(first_name, random_office.name))
            return True

    def allocate_livingspace(self, person):
        """assign a LivingSpace to a person"""

        first_name = person.name.split(' ')[0]
        livingspaces_available = [room for room in self.all_rooms.values() \
                                if isinstance(room, LivingSpace) and room.check_room_availability()]

        if not livingspaces_available:
            print("No Living space available")
            return False
        else:
            # select a random room object
            random_livingspace = random.choice(livingspaces_available)

            # assign a person a Dojo room
            random_livingspace.add_occupant(person)

            # append person name to list of persons allocated rooms
            self.allocated_persons.append(person.name)

            # append room name to dictionary of rooms in the Dojo
            self.all_rooms[random_livingspace.name] = random_livingspace

            # append person name to dictionary of persons in the Dojo
            self.all_persons[person.name] = person
            print("{} has been allocated the livingspace {}." \
                    .format(first_name, random_livingspace.name))
            return True

    def print_room(self, room_name):
        """Prints the names of all the people in a specified room, onto the screen."""

        if not isinstance(room_name, str):
            raise AttributeError("Room name must be a string.")

        if room_name not in self.all_rooms.keys():
            print("{} does not exist in rooms!".format(room_name))

        # retrieve list or person objects from all Dojo rooms
        room_occupants = self.all_rooms[room_name].occupants
        for individual in room_occupants:
            print('{}\n'.format(individual.name))
        return True

    def print_allocations(self, filename=None):
        """Prints a list of allocations onto the screen."""

        self.allocated_rooms = [room for room in self.all_rooms.values() if room.occupants]
        if not self.allocated_rooms:
            print("No Rooms allocated!")

        if filename and not isinstance(filename, str):
            raise AttributeError("Filename must be a string")

        write_to_file = False
        if isinstance(filename, str):
            if len(filename) > 4 and filename.endswith('.txt'):
                write_to_file = True
                ouput_file = open(filename, 'w')

        # search the rooms with occupants, for room names and occupant names
        for room in self.allocated_rooms:
            print('{}\n{}'.format(room.name.upper(), '-'*30))
            if write_to_file:
                ouput_file.write('{}\n{}'.format(room.name.upper(), '-'*30))

            # search for occupant names in list of room occupant(person) objects
            for room_occupant in room.occupants:
                print("\nMEMBER {},".format(room_occupant.name))
                if write_to_file:
                    ouput_file.write("\nMEMBER {},".format(room_occupant.name))
            print('\n\n')
            if write_to_file:
                ouput_file.write('\n\n')
        if write_to_file:
            ouput_file.close()
            return True
        return True

    def print_unallocated(self, filename=None):
        """Prints a list of unallocated people to the screen."""

        # retrieve list of person objects that are not assigned rooms in the Dojo
        unallocated_persons = [person for person in self.all_persons.keys() \
                                if person not in self.allocated_persons]
        if not unallocated_persons:
            print("No Person is unallocated!")

        if filename and not isinstance(filename, str):
            raise AttributeError("Filename must be a string")

        write_to_file = False
        if isinstance(filename, str):
            if len(filename) > 4 and filename.endswith('.txt'):
                write_to_file = True
                ouput_file = open(filename, 'w')

        # retrieve names of persons without rooms
        for individual in unallocated_persons:
            print("\nMEMBER {},".format(individual))
            if write_to_file:
                ouput_file.write("\nMEMBER {},".format(individual))
        if write_to_file:
            ouput_file.close()
            return True
        return True
