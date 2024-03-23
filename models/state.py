#!/usr/bin/python3


"""defines a State class, a subclass of BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A subclass of BaseModel class
    Public class attribute:
        name: (str)
    """
    name = ""
