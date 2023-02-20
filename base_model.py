#!/usr/bin/python3
"""file contains BaseModel class"""

import uuid
from datetime import datetime, time, date
import models


class BaseModel():
    '''This class defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        """args isn't used, re-creates an instance with this dictionary
        representation"""
        if kwargs:
            for key, value in kwargs.items():
                """iterates through the attributes of instance in the dict"""
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    """the datetime is converted from str to object format"""
                if key == "__class__":
                    continue
                """The class key is not added"""
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at with the
        current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__
        of the instance'''
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': __class__.__name__})
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
