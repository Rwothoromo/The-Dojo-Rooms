import unittest
from dojo.the_dojo_rooms import *

class TestDojo(unittest.TestCase):
    def test_create_room_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)

        blue_room = ["Blue"]
        blue_room_type = "office"

        blue_office = dojo.create_room(blue_room_type, blue_room)
        self.assertTrue(blue_office)

        new_room_count = len(dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_multiple_rooms_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)
        multiple_rooms = ["Red", "Green", "Orange"]
        multiple_rooms_type = "office"

        multiple_offices = dojo.create_room(multiple_rooms_type, multiple_rooms)
        self.assertTrue(multiple_offices)

        new_room_count = len(dojo.all_rooms)
        room_increment = len(multiple_rooms)
        self.assertEqual(new_room_count - initial_room_count, room_increment)

    def test_add_person_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)

        person_name1 = "Eli1 Rwt1"
        person_type1 = "STAFF"

        person_name2 = "Eli2 Rwt2"
        person_type2 = "FELLOW"

        person_name3 = "Eli3 Rwt3"
        person_type3 = "Other"

        add_person1 = dojo.add_person(person_name1, person_type1)
        add_person2 = dojo.add_person(person_name2, person_type2, 'Y')
        add_person3 = dojo.add_person(person_name3, person_type3, 'N')

        self.assertTrue(add_person1)
        self.assertTrue(add_person2)
        self.assertFalse(add_person3)


if __name__ == '__main__':
    unittest.main()
