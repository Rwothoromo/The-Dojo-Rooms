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

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo.the_dojo_rooms import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DojoInteractive (cmd.Cmd):
    intro = 'Welcome to The Dojo Rooms!' \
        + ' Product by Rwothoromo Elijah (www.github.com/rwothoromo)!' \
        + ' (type help for a list of commands.)'
    prompt = '(main.py) '
    file = None

    @docopt_cmd
    def do_tcp(self, arg):
        """Usage: tcp <host> <port> [--timeout=<seconds>]"""
        print(arg)

    @docopt_cmd
    def do_serial(self, arg):
        """Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]
Options:
    --baud=<n>  Baudrate [default: 9600]
        """
        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Thank you for stopping by! Have a good day!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    DojoInteractive().cmdloop()

print(opt)


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
    return True


if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called create_room was passed, execute the create_room logic.
    if arguments['create_room']:
        create_room(arguments['<room_type>'], arguments['<room_name>'])
    if arguments['add_person']:
        add_person(arguments['<first_name>'], arguments['<last_name>'], arguments['<person_type>'], arguments['<wants_accommodation>'])
