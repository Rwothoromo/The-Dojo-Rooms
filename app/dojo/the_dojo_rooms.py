#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate
The Dojo Rooms functionality.

Usage:
    create_room office Orange
    create_room office Blue Black Brown
    add_person Neil Armstrong Staff
    add_person Nelly Armweek Fellow Y
    add_person Nelly Armweek Fellow N

    my_program tcp <host> <port> [--timeout=<seconds>]
    my_program serial <port> [--baud=<n>] [--timeout=<seconds>]
    my_program
    my_program (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9690]
    --timeout=<seconds> Time [default: 30]
"""

# import sys
# import cmd
from docopt import docopt, DocoptExit

class Dojo(object):
    def __init__(self):
        self.all_rooms = {}
        self.all_livingspaces = {rooms for rooms in self.all_rooms if self.all_rooms[rooms](0) == 'livingspace'}
        self.all_offices = {rooms for rooms in self.all_rooms if self.all_rooms[rooms](0) == 'livingspace'}
        self.all_persons = {}
        self.all_staff = {persons for persons in self.all_persons if self.all_persons[persons](1) == 'STAFF'}
        self.all_fellows = {persons for persons in self.all_persons if self.all_persons[persons](1) == 'FELLOW'}

    def create_room(self, room_type, room_names):
        initial_room_count = len(self.all_rooms)
        if room_type.lower() == 'office' or room_type.lower() == 'livingspace':
            for room_name in room_names:
                if room_name not in self.all_rooms:
                    self.all_rooms[room_name] = (room_type.lower(), 0)
            new_room_count = len(self.all_rooms)
        room_increment = new_room_count - initial_room_count
        if len(room_names) == room_increment:
            return True
        return False

    def add_person(self, person_name, person_type, wants_accommodation=None):
        if person_type.upper() == 'STAFF':
            if not wants_accommodation:
                self.all_persons[person_name] = (person_type, "Blue")
                print("{} {} has been successfully added.".format(person_type, person_name))
                print("{} has been allocated the office Blue".format(person_name.split(' ')[0]))
                return True
            else:
                print("Person type 'STAFF' cannot seek accomodation")

        elif person_type.upper() == 'FELLOW':

            if wants_accommodation == 'N':
                self.all_persons[person_name] = (person_type, "Blue")
                print("{} {} has been successfully added.".format(person_type, person_name))
                print("{} has been allocated the office Blue".format(person_name.split()[0]))
                return True

            if wants_accommodation == 'Y':
                self.all_persons[person_name] = (person_type, "Blue", "Python")
                print("{} {} has been successfully added.".format(person_type, person_name))
                print("{} has been allocated the office Blue".format(person_name.split()[0]))
                print("{} has been allocated the livingspace Python".format(person_name.split()[0]))
                return True

        else:
            print("Person type must be 'STAFF' or 'FELLOW'")

        return False

class Room(object):
    pass

class Person(object):
    pass

class Office(object):
    pass

class LivingSpace(object):
    pass

class Staff(object):
    pass

class Fellow(object):
    pass

# if __name__ == '__main__':
#     args = docopt(__doc__, sys.argv[1:])
#     print(args)

    # if an argument called create_room was passed, execute the create_room logic.
    # if args['create_room']:
    #     create_room(args['<room_type>'], args['<room_names>'])
    # elif args['add_person']:
    #     add_person(args['<name>'])
