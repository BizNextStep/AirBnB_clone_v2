#!/usr/bin/python3

"""Defines a City class, a subclass of BaseModel."""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models.base import Base


class City(BaseModel, Base):
    """
    A subclass of BaseModel class
    Public class attributes:
        __tablename__: (str) represents the table name, cities
        name:          (str) represents a column containing a string (128 characters), cannot be null
        state_id:      (str) represents a column containing a string (60 characters), cannot be null
                       foreign key to states.id
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

