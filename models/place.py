#!/usr/bin/python3

"""Defines a Place class, a subclass of BaseModel."""
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """
    A subclass of BaseModel class.
    Public class attributes:
        __tablename__:       (str) represents the table name, places
        city_id:             (str) can't be null, foreign key to cities.id
        user_id:             (str) can't be null, foreign key to users.id
        name:                (str) can't be null
        description:         (str) can be null
        number_rooms:        (int) can't be null, default value: 0
        number_bathrooms:    (int) can't be null, default value: 0
        max_guest:           (int) can't be null, default value: 0
        price_by_night:      (int) can't be null, default value: 0
        latitude:            (float) can be null, default value: 0.0
        longitude:           (float) can be null, default value: 0.0
        amenity_ids:         (list) will be Amenity.id
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True, default=0.0)
    longitude = Column(Float, nullable=True, default=0.0)
    amenity_ids = []

    # Establishing relationships
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False) 

