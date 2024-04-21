#!/usr/bin/python3
"""AirBnB clone project FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Storage engine for AirBnB clone project.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        class_dict (dict): A dictionary of all the classes.
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self, cls=None):
        """Returns the list of objects of one type of class."""
        if cls is None:
            return self.__objects
        else:
            return {k: v for k, v in self.__objects.items()
                    if v.__class__.__name__ == cls.__name__}

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def new(self, obj):
        """Sets new __objects to existing dictionary of instances."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes, or converts Python objects into JSON strings."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes, or converts JSON strings into Python objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value["__class__"]](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def close(self):
        """Calls reload method for deserializing the JSON file to objects."""
        self.reload()
