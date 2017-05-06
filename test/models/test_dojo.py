#-*- coding: utf-8-*-
"""
This module runs tests on the functionality of the_dojo_rooms.py.
"""

import unittest
from app.models.the_dojo_rooms import Dojo

class TestDojo(unittest.TestCase):
    """
    This class is used for testing The Dojo Rooms functionality based on the unittests module.
    """

    def setUp(self):
        self.dojo = Dojo()
        self.initial_room_count = len(self.dojo.all_rooms)
        self.initial_person_count = len(self.dojo.all_persons)

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
        room_increment = self.dojo.create_room("office", ["White"])[0]
        self.assertTrue(room_increment)

        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - self.initial_room_count, 1)

    def test_create_room_adds_office_successfully(self):
        self.dojo.create_room("office", ["White"])
        self.assertIn("White", self.dojo.all_rooms.keys())
        self.assertEqual(self.dojo.all_rooms["White"].max_occupants, 6)

    def test_create_room_adds_livingspace_successfully(self):
        self.dojo.create_room("livingspace", ["Maroon"])
        self.assertIn("Maroon", self.dojo.all_rooms.keys())
        self.assertEqual(self.dojo.all_rooms["Maroon"].max_occupants, 4)

    def test_create_multiple_offices_successfully(self):
        room_increment = self.dojo.create_room("office", ["Blue", "Green", "Orange"])[0]
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - self.initial_room_count, room_increment)

    def test_create_multiple_livingspaces_successfully(self):
        room_increment = self.dojo.create_room("livingspace", ["D5", "D7"])[0]
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - self.initial_room_count, room_increment)

    def test_create_room_raises_errors_if_wrong_room_name_argument(self):
        with self.assertRaises(AttributeError):
            self.dojo.create_room("office", 4)

    def test_create_room_raises_errors_if_wrong_room_type_argument(self):
        with self.assertRaises(AttributeError):
            self.dojo.create_room(4, "Blue")

    def test_create_room_raises_errors_if_incorrect_room_type_value(self):
        with self.assertRaises(ValueError):
            self.dojo.create_room("other", ["Blue"])

    def test_add_person_successfully(self):
        person_increment = self.dojo.add_person(self.person_name1, self.person_type1)
        self.assertTrue(person_increment)

        new_person_count = len(self.dojo.all_persons)
        self.assertEqual(new_person_count - self.initial_person_count, 1)

    def test_add_person_adds_fellow_successfully(self):
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        self.assertIn(self.person_name2, self.dojo.all_persons.keys())
        self.assertEqual(self.dojo.all_persons[self.person_name2].type, "FELLOW")

    def test_add_person_adds_staff_successfully(self):
        self.dojo.add_person(self.person_name1, self.person_type1)
        self.assertIn(self.person_name1, self.dojo.all_persons.keys())
        self.assertEqual(self.dojo.all_persons[self.person_name1].type, "STAFF")

    def test_add_person_raises_errors_if_wrong_person_type_argument(self):
        self.dojo.create_room("office", ["White"])
        with self.assertRaises(AttributeError):
            self.dojo.add_person(self.person_name1, 4)

    def test_add_person_raises_errors_if_wrong_person_name_argument(self):
        self.dojo.create_room("office", ["White"])
        with self.assertRaises(AttributeError):
            self.dojo.add_person(4, ["Blue"])

    def test_add_person_raises_errors_if_wrong_accomodation_argument(self):
        self.dojo.create_room("office", ["White"])
        with self.assertRaises(AttributeError):
            add_person1 = self.dojo.add_person('Eli Rwt', "Fellow", 4)

    def test_add_person_raises_errors_if_person_already_exists(self):
        self.dojo.create_room("office", ["White"])
        self.dojo.add_person(self.person_name1, self.person_type1)
        with self.assertRaises(ValueError):
            self.dojo.add_person(self.person_name1, self.person_type1)

    def test_create_room_auto_allocates_offices_to_non_allocated_persons(self):
        self.dojo.add_person(self.person_name1, self.person_type1)
        allocated1 = self.dojo.create_room("office", ["White"])[1]
        self.assertTrue(allocated1)

    def test_create_room_auto_allocates_livingspaces_to_non_allocated_fellows(self):
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        allocated2 = self.dojo.create_room("livingspace", ["D8"])[1]
        self.assertTrue(allocated2)

    def test_create_room_does_not_auto_allocate_livingspace_unwanted_accomodation(self):
        self.dojo.add_person(self.person_name3, self.person_type3, 'N')
        allocated3 = self.dojo.create_room("livingspace", ["D11"])[1]
        self.assertFalse(allocated3)

    def test_person_is_assigned_office_on_add_person_if_office_present(self):
        room_occupants_names = []
        self.dojo.create_room("office", ["White"])
        self.dojo.add_person(self.person_name1, self.person_type1)

        room_occupants_names = []
        room_occupants = []

        for room in self.dojo.all_rooms.values():
            room_occupants += room.occupants

        for individual in room_occupants:
            room_occupants_names.append(individual.name)

        self.assertIn(self.person_name1, room_occupants_names)

    def test_person_is_not_assigned_office_on_add_person_if_office_not_available(self):
        room_occupants_names = []
        self.dojo.add_person(self.person_name1, self.person_type1)

        room_occupants = []

        for room in self.dojo.all_rooms.values():
            room_occupants += room.occupants

        for individual in room_occupants:
            room_occupants_names.append(individual.name)

        self.assertNotIn(self.person_name1, room_occupants_names)

    def test_fellow_is_assigned_livingspace_on_add_person_if_livingspace_present(self):
        room_occupants_names = []
        self.dojo.create_room("livingspace", ["Homely"])
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')

        room_occupants = []

        for room in self.dojo.all_rooms.values():
            room_occupants += room.occupants

        for individual in room_occupants:
            room_occupants_names.append(individual.name)

        self.assertIn(self.person_name2, room_occupants_names)

    def test_fellow_is_not_assigned_livingspace_on_add_person_if_livingspace_not_available(self):
        room_occupants_names = []
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')

        room_occupants = []

        for room in self.dojo.all_rooms.values():
            room_occupants += room.occupants

        for individual in room_occupants:
            room_occupants_names.append(individual.name)

        self.assertNotIn(self.person_name2, room_occupants_names)

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
        self.dojo.create_room("office", ["Blue", "Green", "Orange"])
        self.dojo.create_room("livingspace", ["Purple", "Pink"])

        self.dojo.add_person(self.person_name1, self.person_type1)
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        self.dojo.add_person(self.person_name3, self.person_type3, 'N')
        self.dojo.add_person(self.person_name4, self.person_type4, 'Y')
        self.dojo.add_person(self.person_name5, self.person_type5)

        self.assertTrue(self.dojo.print_allocations()[0])

    def test_print_allocations_raises_error_if_wrong_filename(self):
        self.dojo.create_room("office", ["White"])
        self.dojo.add_person(self.person_name1, self.person_type1)
        self.assertRaises(AttributeError, self.dojo.print_allocations, 4)

    def test_print_allocations_writes_to_file(self):
        self.dojo.create_room("office", ["Blue"])
        self.dojo.add_person("Eli Rwt", "staff")
        self.dojo.add_person("Eli1 Rwt1", "fellow", 'n')
        self.assertTrue(self.dojo.print_allocations('room_occupants.txt')[1])

    def test_print_allocations_does_not_write_to_file_if_no_file_needed(self):
        self.dojo.create_room("office", ["Blue"])
        self.dojo.add_person("Eli Rwt", "staff")
        self.dojo.add_person("Eli1 Rwt1", "fellow", 'n')
        self.assertFalse(self.dojo.print_allocations()[1])

    def test_print_unallocated_successfully(self):
        self.dojo.add_person(self.person_name1, self.person_type1)
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        self.dojo.add_person(self.person_name3, self.person_type3, 'N')

        person_increment = len(self.dojo.all_persons) - self.initial_person_count
        self.assertEqual(len(self.dojo.print_unallocated()[0]), person_increment)

    def test_print_unallocated_writes_to_file(self):
        self.dojo.add_person(self.person_name1, self.person_type1)
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        self.dojo.add_person(self.person_name3, self.person_type3, 'N')

        self.assertTrue(self.dojo.print_unallocated('non_room_occupants.txt')[1])

    def test_print_unallocated_does_not_write_to_file_if_no_file_needed(self):
        self.dojo.add_person(self.person_name1, self.person_type1)
        self.dojo.add_person(self.person_name2, self.person_type2, 'Y')
        self.dojo.add_person(self.person_name3, self.person_type3, 'N')

        self.assertFalse(self.dojo.print_unallocated()[1])

    def test_print_unallocated_raises_error_if_wrong_filename(self):
        self.dojo.add_person(self.person_name1, self.person_type1)
        self.assertRaises(AttributeError, self.dojo.print_unallocated, 4)

    def test_reallocate_person_changes_staff_to_another_office(self):
        self.dojo.create_room("office", ["White"])
        self.dojo.add_person("John Doe", "staff")
        self.dojo.create_room("office", ["Grey"])
        reallocated = self.dojo.reallocate_person("John Doe", "Grey")

        #compare tuples as (old_room, new_room)
        self.assertEqual(("White", "Grey"), reallocated)

    def test_reallocate_person_changes_fellow_to_another_office(self):
        self.dojo.create_room("office", ["White"])
        self.dojo.add_person("John Doe", "fellow", 'Y')
        self.dojo.create_room("office", ["Grey"])
        reallocated = self.dojo.reallocate_person("John Doe", "Grey")

        #compare tuples as (old_room, new_room)
        self.assertEqual(("White", "Grey"), reallocated)

    def test_reallocate_person_changes_fellow_to_another_livingspace(self):
        self.dojo.create_room("livingspace", ["Maroon"])
        self.dojo.add_person("John Doe", "fellow", 'Y')
        self.dojo.create_room("livingspace", ["Homely"])
        reallocated = self.dojo.reallocate_person("John Doe", "Homely")

        #compare tuples as (old_room, new_room)
        self.assertEqual(("Maroon", "Homely"), reallocated)

    def test_reallocate_person_does_not_allocate_staff_to_livingspace(self):
        self.dojo.create_room("office", ["White"])
        self.dojo.add_person("John Doe", "staff")
        self.dojo.create_room("livingspace", ["Homely"])
        reallocated = self.dojo.reallocate_person("John Doe", "Homely")
        self.dojo.print_allocations()

        #compare tuples as (old_room, new_room)
        self.assertNotEqual(("White", "Homely"), reallocated)

    def test_load_people_adds_persons_to_dojo(self):
        add_people = self.dojo.load_people("persons.txt")
        person_increment = len(self.dojo.all_persons) - self.initial_person_count

        self.assertEqual((person_increment, "persons.txt"), add_people)

    def test_load_people_raises_error_if_wrong_filename(self):
        self.assertRaises(AttributeError, self.dojo.load_people, 4)


if __name__ == '__main__':
    unittest.main()
