#!/usr/bin/python3
"""file contains Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from the BaseModel class"""

    place_id = ""   # it will be the Place.id
    user_id = ""    # it will be the User.id
    text = ""
