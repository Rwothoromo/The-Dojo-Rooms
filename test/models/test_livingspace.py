#-*- coding: utf-8-*-
"""
This module runs tests on the LivingSpace class.
"""

import unittest
from app.models.rooms import LivingSpace


class TestLivingSpace(unittest.TestCase):
    """
    Testing The LivingSpace class functionality based on the unittests module.
    """

    def setUp(self):
        self.livingspace = LivingSpace('White')

    def test_livingspace_has_right_attributes(self):
        self.assertListEqual([self.livingspace.name, self.livingspace.max_occupants], ['White', 4])
