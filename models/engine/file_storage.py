#!/usr/bin/python3

""" JSON file """


import json
import os
from models.base_model import BaseModel

Jsondic = {'BaseModel': BaseModel}


class FileStorage:
    """ Class JSON file """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return a dictionary """
        return self.__objects

    def new(self, obj):
        """ Create a new object """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ JSON file """
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(d, f)

    def reload(self):
        """ JSON file Inverse """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(jsondic[value['__class__']](**value))
