#!/usr/bin/env python3
"""file contains test suit for Place class"""

import unittest
import pycodestyle
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """class contains tests case for Place class"""
    def setUp(self):
        """setup method for class"""
        self.inst = Place()

    def tearDown(self):
        """tear down method for class"""
        del self.inst

    def test_pycodestyle_guide(self):
        style = pycodestyle.StyleGuide()
        result = style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0)

    def test_attrs(self):
        """tests class attr"""
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertTrue(hasattr(Place, "number_rooms"))
