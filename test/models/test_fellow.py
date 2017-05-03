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
        self.fellow = Fellow('Eli Rwt')

    def test_fellow_has_right_attributes(self):
        self.assertListEqual([self.fellow.name, self.fellow.type], ['Eli Rwt', 'FELLOW'])
