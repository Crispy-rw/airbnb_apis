
import os
import json

from models.base_model import BaseModel

class FileStorage():

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """
        sets in _objects the obj with key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + getattr(obj, "id")
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode =  "w", encoding = "utf-8") as f:
            my_dict = {}
            for k , v in self.__objects.items():
                my_dict[k] = v.to_dict()
            f.write(json.dumps(my_dict, default=str))

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        print("Calling reload")
        try:
            with open(self.__file_path, mode='r') as f:
                r = json.load(f)
                for k, v in r.items():
                    cls_name = k.split('.')[0]
                    print("--------->>>>>", k)
                    my_obj = eval(v["__class__"] + "(**v)")

                    self.new(my_obj)
        except FileNotFoundError:
            pass
