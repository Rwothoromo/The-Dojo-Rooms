#!/usr/bin/env python
"""
Usage:
  TheDojoRooms create_room <room_type> <room_name>...
  TheDojoRooms add_person <first_name> <last_name> <person_type> [<wants_accommodation>]
  TheDojoRooms print_room <room_name>
  TheDojoRooms print_allocations [<filename>]
  TheDojoRooms print_unallocated [<filename>]
  TheDojoRooms
  TheDojoRooms (-h | --help)

Options:
  -i --interactive Interactive Mode
  -h --help     Show this screen.

"""

import sys
import cmd
from docopt import docopt
from dojo.the_dojo_rooms import Dojo

dojo = Dojo()

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
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return

        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class TheDojoRooms (cmd.Cmd):
    intro = 'Welcome to The Dojo Rooms!' \
        + ' Product by Rwothoromo Elijah (www.github.com/Rwothoromo)' \
        + ' (type help for a list of commands.)'
    prompt = '(TheDojoRooms) '
    file = None

    # create_room() is used to create rooms in The Dojo Rooms
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]
        dojo.create_room(room_type, room_name)

    # add_person() is used to add persons in The Dojo Rooms
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <person_type> [<wants_accommodation>]"""
        person_name = str(arg["<first_name>"]) + ' ' + str(arg["<last_name>"])
        person_type = arg["<person_type>"]
        wants_accommodation = arg["<wants_accommodation>"]
        dojo.add_person(person_name, person_type, wants_accommodation)

    # print_room() is used to display the people in a given room
    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg["<room_name>"]
        dojo.print_room([room_name])

    # print_allocations is used to print a list of allocations onto the screen.
    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<filename>]"""
        filename = arg["<filename>"]
        dojo.print_allocations(filename)

    # print_unallocated is used to print a list of people without room allocations, onto the screen.
    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<filename>]"""
        filename = arg["<filename>"]
        dojo.print_unallocated(filename)

    def do_quit(self, arg):
            """Quits out of Interactive Mode."""
            print('Thank you for stopping by!')
            exit()

opt = docopt(__doc__, sys.argv[1:])
TheDojoRooms().cmdloop()
