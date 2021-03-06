# The Dojo Rooms

[![Build Status](https://travis-ci.org/Rwothoromo/The-Dojo-Rooms.svg?branch=master)](https://travis-ci.org/Rwothoromo/The-Dojo-Rooms)

This system will be used to automatically allocate room space to people at random.

## UML - Unified Modelling Language Design

This [design](/designs) structure shows the relationship between the classes used in The Dojo Rooms.

## Technologies

* Python 2.7
* Sqlite database

## Requirements

* Install [Python 2.7](https://www.python.org/downloads/)
* Install [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## Setup

* Run `git clone` for this repository on git bash and `cd` into the project root.
* Run `virtualenv venv` on command prompt
* Run `venv\Scripts\activate.bat`
* Run `pip install -r requirements.txt` on command prompt
* Run `python main.py` on command prompt
* You will see a prompt, `The Dojo Rooms:`
* Fully setup!

## App Usage

* Activate the virtual environment (See previous section)
* Run `python main.py -h` on command prompt for a list of commands
* Run `python main.py` to start
* Type `help` on the prompt, `The Dojo Rooms: `
* All you need to know is displayed


Unittests
=========
* Run `pytest`


Python Shell or Console
=======================
Below is a sample input/output expectation if you run The Dojo Rooms
on a Python Shell or Console.

* Run `python app/dojo/the_dojo_rooms.py`

The steps to follow are numbered.

1. `dojo = Dojo()`
2. `multiple_offices = dojo.create_room("office", ["Blue", "Green", "Orange"])`
An office called Blue has been successfully created!
An office called Green has been successfully created!
An office called Orange has been successfully created!
3. `multiple_livingspaces = dojo.create_room("livingspace", ["Python", "Django"])`
An livingspace called Python has been successfully created!
An livingspace called Django has been successfully created!
4. `add_person1 = dojo.add_person("Eli1 Rwt1", 'staff')`
Eli1 has been allocated the office Green.
Staff Eli1 Rwt1 has been successfully added.
5. `add_person2 = dojo.add_person("Eli2 Rwt2", 'fellow', 'Y')`
Eli2 has been allocated the office Green.
Eli2 has been allocated the livingspace Python.
Fellow Eli2 Rwt2 has been successfully added.
6. `print_room("Green")`
7. `print_allocations("room_allocations.txt")`
8. `print_unallocated("non_allocated.txt")`
9. `reallocate("Eli2 Rwt2", "Blue")`
10. `load_people("persons.txt")`
11. `save_state()`
12. `load_state()`
