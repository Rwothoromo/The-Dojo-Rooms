#-*- coding: utf-8-*-
"""
This module runs tests on the Office class.
"""

import unittest
from app.models.rooms import Office


class TestOffice(unittest.TestCase):
    """
    Testing The Office class functionality based on the unittests module.
    """

    def setUp(self):
        self.office = Office('Blue')

    def test_office_has_right_attributes(self):
        self.assertListEqual([self.office.name, self.office.max_occupants], ['Blue', 6])
