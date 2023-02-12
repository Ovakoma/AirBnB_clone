#!/usr/bin/python3
"""file contains test suit for User class"""

import unittest
from models.user import User
import pycodestyle


class TestUserClass(unittest.TestCase):
    """class contains test cases for User class"""

    def setUp(self):
        """setup method for User class"""
        self.inst = User()

    def tearDown(self):
        """tear down method for User class"""
        del self.inst

    def test_pycodestyle_guide(self):
        """test for compliance with pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0)

    def test_attr(self):
        """test class attributes"""
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_str_rep(self):
        """tests string rep of user"""
        self.assertEqual(self.inst.__str__(),
                         "[User] ({}) {}".format(self.inst.id,
                                                 self.inst.__dict__))
