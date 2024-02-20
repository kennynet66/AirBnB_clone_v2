#!/usr/bin/python3
"""FileStorage class."""
import json
from models.state import State
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.user import User


class FileStorage:
    """
    This module defines the `FileStorage` class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        The `FileStorage` class handles object persistence using JSON files.
        
        Attributes:
        __file_path (string): The path to the JSON file used for storage.
        __objects (dict): A dictionary storing all instances
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for j, i in self.__objects.items():
                if type(i) == cls:
                    cls_dict[j] = i
            return cls_dict
        return self.__objects

    def new(self, obj):
        """ Adds a new object to the storage dictionary.
        Arguments:
            obj: object to be added.
            """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serialization of all objects"""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as ref:
            json.dump(odict, ref)

    def reload(self):
        """Deserialization of objects.
        
        Handles potential file not found errors
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as ref:
                for o in json.load(ref).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a specific object"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """reload"""
        self.reload()
