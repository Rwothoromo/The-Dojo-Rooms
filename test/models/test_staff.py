#-*- coding: utf-8-*-
"""
This module runs tests on the Staff class.
"""

import unittest
from app.models.persons import Staff


class TestStaff(unittest.TestCase):
    """
    Testing The Staff class functionality based on the unittests module.
    """

    def setUp(self):
        self.staff = Staff('John Doe')

    def test_staff_has_right_attributes(self):
        self.assertListEqual([self.staff.name, self.staff.type], ['John Doe', 'STAFF'])
