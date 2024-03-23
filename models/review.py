#!/usr/bin/python3
"""Defines a Review class, a subclass of BaseModel."""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from models.base import Base


class Review(BaseModel, Base):
    """
    A subclass of BaseModel class
    Public class attributes:
        __tablename__: (str) represents the table name, reviews
        place_id:      (str) represents a column containing a string (60 characters), cannot be null
                       foreign key to places.id
        user_id:       (str) represents a column containing a string (60 characters), cannot be null
                       foreign key to users.id
        text:          (str) represents a column containing a string (1024 characters), cannot be null
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)


