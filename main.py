#!/usr/bin/env python
"""The Dojo Rooms

Usage:
  main.py create_room <room_type> <room_name>...
  main.py add_person <first_name> <last_name> <person_type> [<wants_accommodation>]
  main.py print_room <room_name>
  main.py print_allocations [<filename>]
  main.py print_unallocated [<filename>]
  main.py reallocate_person <first_name> <last_name> <room_name>
  main.py
  main.py (-h | --help | --version)

Options:
  -i, --interactive Interactive Mode
  -h, --help  Show this screen and exit.
  --o=<filename>  Filename to save output
  --db=sqlite_database

"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app.models.the_dojo_rooms import Dojo

dojo = Dojo()
# Citation: Source https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
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
# End of Citation

class TheDojoRooms(cmd.Cmd):
    intro = '\n\tWelcome to The Dojo Rooms!\n' \
        + '\tProduct by Rwothoromo Elijah (www.github.com/Rwothoromo)\n' \
        + '\t(type help for a list of commands.)\n'
    prompt = 'The Dojo Rooms: '
    file = None

    # create_room is used to create rooms in The Dojo Rooms
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]
        dojo.create_room(room_type, room_name)

    # add_person is used to add persons in The Dojo Rooms
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <person_type> [<wants_accommodation>]"""
        person_name = str(arg["<first_name>"]) + ' ' + str(arg["<last_name>"])
        person_type = arg["<person_type>"]
        wants_accommodation = arg["<wants_accommodation>"]
        dojo.add_person(person_name, person_type, wants_accommodation)

    # print_room is used to display the people in a given room
    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg["<room_name>"]
        dojo.print_room(room_name)

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

    # reallocate_person is used to reallocate a person from one room to another in The Dojo Rooms
    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <first_name> <last_name> <room_name>"""
        person_name = str(arg["<first_name>"]) + ' ' + str(arg["<last_name>"])
        room_name = arg["<room_name>"]
        dojo.reallocate_person(person_name, room_name)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Thank you for stopping by!')
        exit()

opt = docopt(__doc__, sys.argv[1:])
TheDojoRooms().cmdloop()
