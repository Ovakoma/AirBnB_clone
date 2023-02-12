#!/usr/bin/python3
"""file contains test suit for Amenity class"""

from models.base_model import BaseModel
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class contains test cases for Amenity class"""

    def setUp(self):
        '''setup parameters for tests'''
        self.inst = Amenity()

    def tearDown(self):
        """tearDown after excecuting other fucntions"""
        pass

    def test_superclass(self):
        """tests that Amenity class is subclass of BaseModel class"""
        self.assertTrue(issubclass(self.inst.__class__, BaseModel))

    def test_name_type(self):
        """tests that the data type for name is str"""
        self.assertTrue(isinstance(self.inst.name, str))

    def test_class_attr(self):
        """tests Amenity class attr"""
        self.assertTrue(hasattr(Amenity, "name"))
