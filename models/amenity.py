#!/usr/bin/python3
"""defines Amenity class, a subclass of BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A subclass of BaseModel class
    Public class attribute:
        name: (str)
    """
    name = ""
