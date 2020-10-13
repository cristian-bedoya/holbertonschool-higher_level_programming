#!/usr/bin/python3
"""Module base."""

import json
import os


class Base():
    """ Class Basse:
    Private attribute __nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ method Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries."""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file."""

        if list_objs is None or list_objs == []:
            j_str = "[]"
        else:
            j_str = cls.to_json_string([o.to_dictionary() for o in list_objs])
        new_file = cls.__name__ + ".json"
        with open(new_file, 'w') as f:
            f.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            obj_dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj_dummy = cls(1)
        obj_dummy.update(**dictionary)
        return obj_dummy

    @classmethod
    def load_from_file(cls):
        """Returns an instance with all attributes already set."""
        file_1 = cls.__name__ + '.json'
        if not os.path.exists(file_1):
            return []
        list_dict = []
        with open(file_1, 'r') as f:
            str1 = f.read()
            list_dict = cls.from_json_string(str1)
        return [cls.create(**d) for d in list_dict]
