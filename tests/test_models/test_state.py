#!/usr/bin/python3
"""Unittest for the StateModel"""


from models.state import State
import unittest
import pycodestyle


class TestStateModel(unittest.TestCase):
    """Test cases for the State Model"""

    def setUp(self):
        """setup the user class instance for test cases"""
        self.state = State()

    def test_pycodestyle_guide(self):
        """Test for pep8 style guide in the file"""
        style = pycodestyle.StyleGuide(quite=True)
        result = style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0)

    def test_class_attr(self):
        """test class attributes"""
        self.assertTrue(hasattr(State, "name"))

    def test_str_rep(self):
        """test for string representation of user object"""
        self.assertEqual(self.state.__str__(),
                         "[State] ({}) {}".format(
                          self.state.id, self.state.__dict__))

    def test_for_inheritedMethod(self):
        """test for method inherited from the super class"""
        state_attr = dir(State)
        self.assertTrue("save" in state_attr)
        self.assertTrue("to_dict" in state_attr)
