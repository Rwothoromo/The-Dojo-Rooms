# The_Dojo_Rooms
==============

This system will be used to automatically allocate spaces to people at random, at The Dojo, one of Andela Kenya’s facilities.

UML - Unified Modelling Language
================================
Location: /designs
This design structure shows the relationship between the classes involved in The Dojo Rooms project.
It also provides a basis for a later database design/structure.

Docopt
======
Run the command:
python app/main.py

to test The Dojo Rooms functionality.

Unittests
=========
Run the command:
pytest app/test/test_dojo_unittests.py

to run unittests on The Dojo Rooms functionality.

The Dojo Rooms
==============
Run the command:
pytest app/dojo/the_dojo_rooms.py

to run The Dojo Rooms application.

Python Shell or Console
=======================
Below is a sample input/output expectation if you run The Dojo Rooms
on a Python Shell or Console

>>> dojo = Dojo()
>>> multiple_offices = dojo.create_room("office", ["Blue", "Green", "Orange"])
An office called Blue has been successfully created!
An office called Green has been successfully created!
An office called Orange has been successfully created!
>>> multiple_livingspaces = dojo.create_room("livingspace", ["Python", "Django"])
An livingspace called Python has been successfully created!
An livingspace called Django has been successfully created!
>>> add_person1 = dojo.add_person("Eli1 Rwt1", 'staff')
Eli1 has been allocated the office Green.
Staff Eli1 Rwt1 has been successfully added.
>>> add_person2 = dojo.add_person("Eli2 Rwt2", 'fellow', 'Y')
Eli2 has been allocated the office Green.
Eli2 has been allocated the livingspace Python.
Fellow Eli2 Rwt2 has been successfully added.
>>> add_person3 = dojo.add_person("Eli3 Rwt3", 'fellow', 'N')
Eli3 has been allocated the office Orange.
Fellow Eli3 Rwt3 has been successfully added.
>>> add_person4 = dojo.add_person("Eli4 Rwt4", 'fellow', 'Y')
Eli4 has been allocated the office Orange.
Eli4 has been allocated the livingspace Python.
Fellow Eli4 Rwt4 has been successfully added.
>>> add_person5 = dojo.add_person("Eli5 Rwt5", 'staff')
Eli5 has been allocated the office Green.
Staff Eli5 Rwt5 has been successfully added.
>>> add_person6 = dojo.add_person("Eli6 Rwt6", 'staff')
Eli6 has been allocated the office Green.
Staff Eli6 Rwt6 has been successfully added.
>>> add_person7 = dojo.add_person("Eli7 Rwt7", 'fellow', 'N')
Eli7 has been allocated the office Green.
Fellow Eli7 Rwt7 has been successfully added.
>>> add_person8 = dojo.add_person("Eli8 Rwt8", 'fellow', 'Y')
Eli8 has been allocated the office Green.
Eli8 has been allocated the livingspace Python.
Fellow Eli8 Rwt8 has been successfully added.
>>> add_person9 = dojo.add_person("Eli9 Rwt9", 'staff')
Eli9 has been allocated the office Orange.
Staff Eli9 Rwt9 has been successfully added.
>>>
