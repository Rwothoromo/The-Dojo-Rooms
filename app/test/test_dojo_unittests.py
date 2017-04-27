import unittest
from dojo.the_dojo_rooms import *

class TestDojo(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.initial_room_count = len(self.dojo.all_rooms)

        self.white_office = ["White"]
        self.white_office_type = "office"

        self.multiple_offices = ["Blue", "Green", "Orange"]
        self.multiple_offices_type = "office"

        self.multiple_livingspaces = ["Python", "Django"]
        self.multiple_livingspaces_type = "livingspace"

        self.person_name1 = "Eli1 Rwt1"
        self.person_type1 = "STAFF"

        self.person_name2 = "Eli2 Rwt2"
        self.person_type2 = "FELLOW"

        self.person_name3 = "Eli3 Rwt3"
        self.person_type3 = "FELLOW"

        self.person_name4 = "Eli4 Rwt4"
        self.person_type4 = "FELLOW"

        self.person_name5 = "Eli5 Rwt5"
        self.person_type5 = "STAFF"

        self.person_name6 = "Eli3 Rwt3"
        self.person_type6 = "Other"

        self.inexistent_room = "A12" # An inexistent room name
        self.wrongly_named_room = 4 #wrong value

    def test_create_room_successfully(self):
        room_increment = self.dojo.create_room(self.white_office_type, self.white_office)
        self.assertTrue(room_increment)

        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - self.initial_room_count, 1)

    def test_create_multiple_rooms_successfully(self):
        room_increment = self.dojo.create_room(self.multiple_offices_type, self.multiple_offices)
        self.assertTrue(room_increment)

        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - self.initial_room_count, room_increment)

    def test_add_person_successfully(self):
        self.dojo.create_room(self.multiple_offices_type, self.multiple_offices)
        self.dojo.create_room(self.multiple_livingspaces_type, self.multiple_livingspaces)

        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        add_person2 = self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        add_person3 = self.dojo.add_person(self.person_name6, self.person_type6, 'N')

        self.assertTrue(add_person1)
        self.assertTrue(add_person2)
        self.assertFalse(add_person3)

    def test_print_room_successfully(self):
        self.dojo.create_room(self.multiple_offices_type, self.multiple_offices)
        self.dojo.create_room(self.multiple_livingspaces_type, self.multiple_livingspaces)

        rooms_print1 = self.dojo.print_room(self.multiple_offices[0])
        rooms_print2 = self.dojo.print_room(self.multiple_offices[1])
        rooms_print3 = self.dojo.print_room(self.multiple_offices[2])
        rooms_print4 = self.dojo.print_room(self.multiple_livingspaces[0])
        rooms_print5 = self.dojo.print_room(self.multiple_livingspaces[1])

        self.assertTrue(rooms_print1)
        self.assertTrue(rooms_print2)
        self.assertTrue(rooms_print3)
        self.assertTrue(rooms_print4)
        self.assertTrue(rooms_print5)
        self.assertFalse(self.dojo.print_room("Unknown"))
        self.assertRaises(TypeError, self.dojo.print_room, self.wrongly_named_room)

    def test_print_allocations_successfully(self):
        self.dojo.create_room(self.multiple_offices_type, self.multiple_offices)
        self.dojo.create_room(self.multiple_livingspaces_type, self.multiple_livingspaces)

        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        add_person2 = self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        add_person3 = self.dojo.add_person(self.person_name3, self.person_type3, 'N')
        add_person4 = self.dojo.add_person(self.person_name4, self.person_type4, 'Y')
        add_person5 = self.dojo.add_person(self.person_name5, self.person_type5)

        allocations = self.dojo.print_allocations()
        self.assertTrue(allocations)

if __name__ == '__main__':
    unittest.main()
