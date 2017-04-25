#!/usr/bin/env python
# import sys
# import cmd
# from docopt import docopt, DocoptExit

class Dojo(object):
    def __init__(self):
        self.all_rooms = {}
        # self.all_livingspaces = {rooms for rooms in self.all_rooms if self.all_rooms[rooms](0) == 'livingspace'}
        # self.all_offices = {rooms for rooms in self.all_rooms if self.all_rooms[rooms](0) == 'livingspace'}
        self.all_persons = {}
        # self.all_staff = {persons for persons in self.all_persons if self.all_persons[persons](1) == 'STAFF'}
        # self.all_fellows = {persons for persons in self.all_persons if self.all_persons[persons](1) == 'FELLOW'}

    def create_room(self, room_type, room_name):
        initial_room_count = len(self.all_rooms)
        if room_type.lower() == 'office' or room_type.lower() == 'livingspace':
            for room in room_name:
                if room not in self.all_rooms:
                    self.all_rooms[room] = (room_type.lower(), 0)
            new_room_count = len(self.all_rooms)

        room_increment = new_room_count - initial_room_count
        if len(room_name) == room_increment:
            return True
        return False

    def add_person(self, person_name, person_type, wants_accommodation=None):
        if person_type.upper() == 'STAFF':
            if not wants_accommodation:
                self.all_persons[person_name] = (person_type, "Blue")
                return True
            else:
                print("Person type 'STAFF' cannot seek accomodation")

        elif person_type.upper() == 'FELLOW':
            if wants_accommodation == 'N':
                self.all_persons[person_name] = (person_type, "Blue")
                return True

            if wants_accommodation == 'Y':
                self.all_persons[person_name] = (person_type, "Blue", "Python")
                return True

        else:
            print("Person type must be 'STAFF' or 'FELLOW'")

        return False

    def print_room(self, room_name):
        no_of_persons = 0
        for person in self.all_persons:
            if self.all_persons[person][1] == room_name:
                print(person,'\n')
                no_of_persons += 1

        if not no_of_persons:
            return False
        return True

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
    #     create_room(args['<room_type>'], args['<room_name>'])
    # elif args['add_person']:
    #     add_person(args['<name>'])
