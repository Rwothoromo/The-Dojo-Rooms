#!/usr/bin/env python
"""
This file demonstrates the functionality of The Dojo Rooms project.

Usage:
  main.py create_room <room_type> <room_name>...
  main.py add_person <first_name> <last_name> <person_type> [<wants_accommodation>]
  main.py print_room <room_name>
  main.py print_allocations [<filename>]
  main.py (-h | --help)

Options:
  -h --help     Show this screen.

"""

from docopt import docopt
from dojo.the_dojo_rooms import Dojo

dojo = Dojo()

# create_room() is used to create rooms in The Dojo Rooms
def create_room(room_type, room_name):
    dojo.create_room(room_type, room_name)

# add_person() is used to add persons in The Dojo Rooms
def add_person(first_name, last_name, person_type, wants_accommodation):
    person_name = str(first_name) + ' ' + str(last_name)
    dojo.add_person(person_name, person_type, wants_accommodation)

# print_room() is used to display the people in a given room
def print_room(room_name):
    dojo.print_room(room_name[0])

def print_allocations(filename):
    dojo.print_allocations(filename)



if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called create_room was passed, execute the create_room logic.
    if arguments['create_room']:
        create_room(arguments['<room_type>'], arguments['<room_name>'])
    if arguments['add_person']:
        add_person(arguments['<first_name>'], arguments['<last_name>'], arguments['<person_type>'], arguments['<wants_accommodation>'])
    if arguments['print_room']:
        print_room(arguments['<room_name>'])
