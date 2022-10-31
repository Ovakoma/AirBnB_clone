#!/usr/bin/python3
"""file contains City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits from the BaseModel class"""
    state_id = ""
    name = ""
