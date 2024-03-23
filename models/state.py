#!/usr/bin/python3

"""defines a State class, a subclass of BaseModel."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    A subclass of BaseModel class
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: id, created_at, updated_at, name
        """
        super().__init__(*args, **kwargs)

