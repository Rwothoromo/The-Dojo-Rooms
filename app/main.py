#!/usr/bin/env python
"""
This file demonstrates the functionality of The Dojo Rooms project.

Usage:
  main.py create_room <room_type> <room_name>...
  main.py add_person <first_name> <last_name> <person_type> [<wants_accommodation>]
  main.py print_room <room_name>
  main.py (-h | --help)

Options:
  -h --help     Show this screen.

"""

from docopt import docopt

# create_room() is used to create rooms in The Dojo Rooms
def create_room(room_type, room_name):
    if room_type.lower() == 'office' or room_type.lower() == 'livingspace':
        for room in room_name:
            print("An {} called {} has been successfully created!".format(room_type.lower(), room))
    """
    For example:
    create_room('office', 'Orange')
    An office called Orange has been successfully created!

    create_room('office', 'Blue', 'Black', 'Brown')
    An office called Blue has been successfully created!
    An office called Black has been successfully created!
    An office called Brown has been successfully created!
    """
    return True

# add_person() is used to add persons in The Dojo Rooms
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

    """
    For example:
    add_person('Neil', 'Armstrong', 'Staff')
    Staff Neil Armstrong has been successfully added.
    Neil has been allocated the office Blue

    add_person('Nelly', 'Armweek', 'Fellow', 'Y')
    Fellow Nelly Armweek has been successfully added.
    Nelly has been allocated the office Blue
    Nelly has been allocated the livingspace Python
    """
    return True


if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called create_room was passed, execute the create_room logic.
    if arguments['create_room']:
        create_room(arguments['<room_type>'], arguments['<room_name>'])
    if arguments['add_person']:
        add_person(arguments['<first_name>'], arguments['<last_name>'], arguments['<person_type>'], arguments['<wants_accommodation>'])
