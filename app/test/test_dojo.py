#-*- coding: utf-8-*-
"""
This module runs tests on the functionality of the_dojo_rooms.py.
"""

import unittest
from app.dojo.the_dojo_rooms import Dojo

class TestDojo(unittest.TestCase):
    """
    This class is used for testing functionality based on the unittests module.
    """

    def setUp(self):
        self.dojo = Dojo()
        self.initial_room_count = len(self.dojo.all_rooms)

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

    def test_create_room_successfully(self):
        room_increment = self.dojo.create_room("office", ["White"])
        self.assertTrue(room_increment)

        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - self.initial_room_count, 1)

    def test_create_multiple_rooms_successfully(self):
        room_increment = self.dojo.create_room("office", ["Blue", "Green", "Orange"])
        self.assertTrue(room_increment)

        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - self.initial_room_count, room_increment)

    def test_create_room_raises_errors_if_wrong_room_name_argument(self):
        with self.assertRaises(AttributeError):
            add_room = self.dojo.create_room("office", 4)

    def test_create_room_raises_errors_if_wrong_room_type_argument(self):
        with self.assertRaises(AttributeError):
            add_room = self.dojo.create_room(4, "Blue")

    def test_create_room_raises_errors_if_incorrect_room_type_value(self):
        with self.assertRaises(ValueError):
            add_room = self.dojo.create_room("other", ["Blue"])

    def test_add_person_successfully(self):
        # self.dojo.create_room("office", ["Blue", "Green", "Orange"])
        # self.dojo.create_room("livingspace", ["Purple", "Pink"])

        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        self.assertTrue(add_person1)

        add_person2 = self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        self.assertTrue(add_person2)

    def test_add_person_raises_errors_if_wrong_person_type_argument(self):
        self.dojo.create_room("office", ["White"])
        with self.assertRaises(AttributeError):
            add_person1 = self.dojo.add_person(self.person_name1, 4)

    def test_add_person_raises_errors_if_wrong_person_name_argument(self):
        self.dojo.create_room("office", ["White"])
        with self.assertRaises(AttributeError):
            add_person1 = self.dojo.add_person(4, ["Blue"])

    def test_add_person_raises_errors_if_wrong_accomodation_argument(self):
        self.dojo.create_room("office", ["White"])
        with self.assertRaises(AttributeError):
            add_person1 = self.dojo.add_person('Eli Rwt', "Fellow", 4)

    def test_add_person_raises_errors_if_person_already_exists(self):
        self.dojo.create_room("office", ["White"])
        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        with self.assertRaises(ValueError):
            add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)

    def test_print_room_successfully(self):
        self.dojo.create_room("office", ["Blue"])
        self.dojo.create_room("livingspace", ["Homer"])

        self.dojo.add_person("Eli Rwt", "staff")
        self.dojo.add_person("Eli1 Rwt1", "fellow", "Y")

        rooms_print1 = self.dojo.print_room("Blue")
        rooms_print2 = self.dojo.print_room("Homer")

        self.assertTrue(rooms_print1)
        self.assertTrue(rooms_print2)

    def test_print_room_raises_error_if_wrong_room_name_argument(self):
        self.dojo.create_room("office", ["White"])
        self.assertRaises(AttributeError, self.dojo.print_room, 4)

    def test_print_room_raises_key_error_if_incorrect_room_name_value(self):
        self.dojo.create_room("office", ["White"])
        self.assertRaises(KeyError, self.dojo.print_room, "Unknown")

    def test_print_allocations_successfully(self):
        # self.dojo.create_room("office", ["Blue", "Green", "Orange"])
        # self.dojo.create_room("livingspace", ["Purple", "Pink"])

        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        add_person2 = self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        add_person3 = self.dojo.add_person(self.person_name3, self.person_type3, 'N')
        add_person4 = self.dojo.add_person(self.person_name4, self.person_type4, 'Y')
        add_person5 = self.dojo.add_person(self.person_name5, self.person_type5)

        allocations = self.dojo.print_allocations()
        self.assertTrue(allocations)

    def test_print_allocations_raises_error_if_wrong_filename(self):
        self.dojo.create_room("office", ["White"])
        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        self.assertRaises(AttributeError, self.dojo.print_allocations, 4)

    def test_print_allocations_writes_to_file(self):
        self.dojo.create_room("office", ["Blue"])
        self.dojo.add_person("Eli Rwt", "staff")
        self.dojo.add_person("Eli1 Rwt1", "fellow", 'n')
        self.assertTrue(self.dojo.print_allocations('room_occupants.txt'))

    def test_print_unallocated_successfully(self):
        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        add_person2 = self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        add_person3 = self.dojo.add_person(self.person_name3, self.person_type3, 'N')
        add_person4 = self.dojo.add_person(self.person_name4, self.person_type4, 'Y')
        add_person5 = self.dojo.add_person(self.person_name5, self.person_type5)

        non_allocations = self.dojo.print_unallocated()
        self.assertTrue(non_allocations)

    def test_print_unallocated_raises_error_if_wrong_filename(self):
        add_person1 = self.dojo.add_person(self.person_name1, self.person_type1)
        self.assertRaises(AttributeError, self.dojo.print_unallocated, 4)

    def test_print_unallocated_writes_to_file(self):
        self.dojo.add_person("Eli Rwt", "staff")
        self.dojo.add_person("Eli1 Rwt1", "fellow", 'n')
        self.assertTrue(self.dojo.print_unallocated('non_room_occupants.txt'))


if __name__ == '__main__':
    unittest.main()
