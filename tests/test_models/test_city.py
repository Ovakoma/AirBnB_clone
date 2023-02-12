#!/usr/bin/python3
"""class contains test suit for City class"""

from models.city import City
import unittest
import pycodestyle


class TestCity(unittest.TestCase):
    """class contains test cases for City class"""

    def setUp(self):
        """setup method for test suit"""
        self.inst = City()

    def test_pycodestyle(self):
        """tests that code complies with pep8 style guide"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0, "error somewhere")

    def test_types(self):
        """tests the variable types"""
        self.assertTrue(type(self.inst.state_id), str)
        self.assertTrue(type(self.inst.name), str)

    def test_attr(self):
        """tests for class attributes"""
        self.assertTrue(hasattr(self.inst, "state_id"))
        self.assertTrue(hasattr(self.inst, "name"))

    def test_inherited_methods(self):
        """tests for inherited methods"""
        inst_mtds = dir(City)
        self.assertTrue("to_dict" in inst_mtds)
