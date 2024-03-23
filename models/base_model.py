#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models
from sqlalchemy import Column, String, DateTime
from models.engine.db_storage import Base


class BaseModel:
    """
    Parent class for AirBnB clone project
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: uuid4, dates when class was created/updated.
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    setattr(self, key, datetime.strptime(value, date_format))
                elif "updated_at" == key:
                    setattr(self, key, datetime.strptime(value, date_format))
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return class name, id, and the dictionary.
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        Returns string representation of the object.
        """
        return (self.__str__())

    def save(self):
        """
        Instance method to:
        - update current datetime
        - save to the database
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times.
        """
        dic = self.__dict__.copy()
        dic.pop('_sa_instance_state', None)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

    def delete(self):
        """
        Delete the current instance from the storage.
        """
        models.storage.delete(self)

