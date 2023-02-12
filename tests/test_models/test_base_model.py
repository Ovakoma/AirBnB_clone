#!/usr/bin/python3
"""file contains test suit for BaseModel class"""

from datetime import datetime, date, time
import time
import unittest
import uuid
import os
from models.base_model import BaseModel
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """class contains methods testing BaseModel instances"""

    def setUp(self):
        """prepare test fixtures"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.tmp")

    def tearDown(self):
        """delete temp json file and return original file"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.tmp"):
            os.rename("file.json.tmp", "file.json")

    def test_doc_module(self):
        '''tests that the doc module length is greater than 1'''
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_pycodestyle_check(self):
        '''tests that code complies with pycodestyle guide'''
        style = pycodestyle.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                        "code doesn't comply with pycodestyle")

    def test_class_attr(self):
        """tests the various instance attributes in BaseModel class"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.age = 30
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "name"))
        self.assertTrue(hasattr(my_model, "my_number"))
        self.assertTrue(hasattr(my_model, "age"))

    def test_class_attr_types(self):
        """tests for the various instance attribute types"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.id), str)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertTrue(type(my_model.updated_at), datetime)

    def test_class_dict(self):
        """tests the to_dict methood of BaseModel class"""
        my_model_json = BaseModel().to_dict()
        self.assertTrue(isinstance(my_model_json, dict))
        self.assertTrue("id" in my_model_json)
        self.assertTrue("created_at" in my_model_json)
        self.assertTrue("__class__" in my_model_json)
        self.assertTrue("updated_at" in my_model_json)

    def test_datetime_attr(self):
        """tests two BaseModel instances for different datetime
        objects"""
        time_1 = datetime.now()
        inst_1 = BaseModel()
        time_2 = datetime.now()
        self.assertTrue(time_1 <= inst_1.created_at <= time_2)
        time.sleep(1e-4)
        time_1 = datetime.now()
        inst_2 = BaseModel()
        time_2 = datetime.now()
        self.assertTrue(time_1 <= inst_2.created_at <= time_2)
        self.assertNotEqual(inst_1.created_at, inst_2.created_at)
        self.assertNotEqual(inst_1.updated_at, inst_2.updated_at)


if __name__ == "__main__":
    unittest.main()
