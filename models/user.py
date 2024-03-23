#!/usr/bin/python3

"""Defines a User class, a subclass of BaseModel."""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel):
    """
    A subclass of BaseModel class.
    Public class attributes:
        __tablename__: (str) represents the table name, users
        email:          (str) can't be null
        password:       (str) can't be null
        first_name:     (str) can be null
        last_name:      (str) can be null
        reviews:        (relationship) represents a one-to-many relationship with Review
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")

