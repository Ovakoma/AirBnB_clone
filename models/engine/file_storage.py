#!/usr/bin/python3
"""This module stores all instances of the class"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''This class serializes instances to a JSON file and deserializes
    JSON file to instances'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''This function returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'w') as file:
            dic_t = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic_t, file)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)'''
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                dic_t = json.loads(file.read())
                for k, v in dic_t.items():
                    self.__objects[k] = eval(k.split(".")[0])(**v)
