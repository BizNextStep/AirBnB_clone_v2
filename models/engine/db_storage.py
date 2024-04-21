#!/usr/bin/python3
""" Module for DBStorage class """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the DBStorage instance """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                     format(getenv('HBNB_MYSQL_USER'),
                                            getenv('HBNB_MYSQL_PWD'),
                                            getenv('HBNB_MYSQL_HOST'),
                                            getenv('HBNB_MYSQL_DB')),
                                     pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries all objects of a given class """
        objs = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """ Adds a new object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the specified object from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database and creates the current database session """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Closes the SQLAlchemy session."""
        if self.__session is not None:
            self.__session.remove()  # Explicitly remove the session from scope
            self.__session = None

