#!/usr/bin/env python
"""
This file demonstrates the functionality of The Dojo Rooms project.

Usage:
  main.py create_room <room_type> <room_name>...
  main.py add_person <first_name> <last_name> <person_type> <wants_accommodation>
  main.py print_room <room_name>
  main.py (-h | --help)

Options:
  -h --help     Show this screen.

"""

# import sys
# import cmd
from docopt import docopt, DocoptExit

def create_room(room_type, room_name):
    if room_type.lower() == 'office' or room_type.lower() == 'livingspace':
        for room in room_name:
            print("An {} called {} has been successfully created!".format(room_type.lower(), room))

def add_person(first_name, last_name, person_type, wants_accommodation=None):
    if person_type.upper() == 'STAFF':
        if not wants_accommodation:
            print("{} {} {} has been successfully added.".format(person_type.capitalize(), first_name, last_name))
            print("{} has been allocated the office Blue".format(first_name))
        else:
            print("Person type 'STAFF' cannot seek accomodation")

    elif person_type.upper() == 'FELLOW':
        if not wants_accommodation:
            print("Person type 'FELLOW' must indicate 'Y' or 'N' for accomodation")

        elif wants_accommodation.upper() == 'N':
            print("{} {} {} has been successfully added.".format(person_type.capitalize(), first_name, last_name))
            print("{} has been allocated the office Blue".format(first_name))

        elif wants_accommodation.upper() == 'Y':
            print("{} {} {} has been successfully added.".format(person_type.capitalize(), first_name, last_name))
            print("{} has been allocated the office Blue.".format(first_name))
            print("{} has been allocated the livingspace Python,".format(first_name))

        else:
            print("Person type 'FELLOW' must indicate 'Y' or 'N' for accomodation")



def print_room(room_name):
    print("{} {}".format(room_name))


if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called create_room was passed, execute the create_room logic.
    if arguments['create_room']:
        create_room(arguments['<room_type>'], arguments['<room_name>'])
    elif arguments['add_person']:
        add_person(arguments['<first_name>'], arguments['<last_name>'], arguments['<person_type>'], arguments['<wants_accommodation>'])
    elif arguments['print_room']:
        add_person(arguments['<name>'])
