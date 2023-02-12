#!/usr/bin/python3
"""file contains test suit for Review class"""

import unittest
from models.review import Review
import pycodestyle


class TestReviewClass(unittest.TestCase):
    """class contains test cases for Review class"""

    def setUp(self):
        """setup method for class"""
        self.inst = Review()

    def tearDown(self):
        """tear down method for class"""
        del self.inst

    def test_pycodestyle_guide(self):
        """tests if code complies with pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0)

    def test_class_attr(self):
        """tests class attributes"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_attr_type(self):
        """tests attribute types"""
        self.assertTrue(type(self.inst.place_id), str)
        self.assertTrue(type(self.inst.user_id), str)
        self.assertTrue(type(self.inst.text), str)
