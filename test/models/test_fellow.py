#-*- coding: utf-8-*-
"""
This module runs tests on the Fellow class.
"""

import unittest
from app.models.persons import Fellow


class TestFellow(unittest.TestCase):
    """
    Testing The Fellow class functionality based on the unittests module.
    """

    def setUp(self):
        self.fellow = Fellow('Eli Rwt', wants_accomodation=False)
        self.fellow1 = Fellow('Eli1 Rwt1', wants_accomodation=True)

    def test_fellow_has_right_attributes(self):
        self.assertListEqual([self.fellow.name, self.fellow.type, self.fellow.wants_accomodation], ['Eli Rwt', 'FELLOW', False])
        self.assertListEqual([self.fellow1.name, self.fellow1.type, self.fellow1.wants_accomodation], ['Eli1 Rwt1', 'FELLOW', True])
